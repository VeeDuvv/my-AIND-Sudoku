from time import gmtime, strftime

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
	"""Cross product of elements in A and elements in B."""
	return [s+t for s in A for t in B]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

# add the diagonal units in unit list and peers
diagonal_units = [[r+c for r, c in zip(rows, cols)],[r + c for r, c in zip(rows, cols[::-1])]]

#diagonal_units = [['A1','B2','C3','D4','E5','F6','G7','H8','I9'],['A9','B8','C7','D6','E5','F4','G3','H2','I1']]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
	"""
	Please use this function to update your values dictionary!
	Assigns a value to a given box. If it updates the board record it.
	"""

	# Don't waste memory appending actions that don't actually change any values
	if values[box] == value:
		return values

	values[box] = value
	if len(value) == 1:
		assignments.append(values.copy())
	return values

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Input: A grid in string form.
    Output: A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value,
	eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def naked_twins(values):
	"""Eliminate values using the naked twins strategy.
	Args:
		values(dict): a dictionary of the form {'box_name': '123456789', ...}
	Returns:
		the values dictionary with the naked twins eliminated from peers.
	"""
	row = ['A','B','C','D','E','F','G','H','I']
	traversed = []
	for box, value in values.items():
		# if the box is not solved and value is of length two [because naked twins requires two boxes to have values of length 2]
		if len(value) == 2:
			# find box's row and column unit index
			box_row_idx = rows.index(box[:1])
			box_column_idx = int(box[1:]) - 1

			# find box's square unit index
			for idx, unit in enumerate(square_units):
				if box in unit:
					box_square_idx = idx
					break

			# create list of peers using only the unit index for the box
			row_peers = row_units[box_row_idx]
			column_peers = column_units[box_column_idx]
			square_peers = square_units[box_square_idx]

			diagonal_peers = []
			if box in diagonal_units[0]:
				diagonal_peers = diagonal_units[0]
			elif box in diagonal_units[1]:
				diagonal_peers = diagonal_units[1]

			all_peers = column_peers + row_peers + square_peers + diagonal_peers

			# for box's peers
			for peer in all_peers:
				if box != peer and values[box] == values[peer] and [box, peer] not in traversed:
					# don't do redundant traversing
					traversed.append([box, peer])
					traversed.append([peer, box])
					#print("\nfound naked twin", box, peer, values[box])

					# find all new peers only in the section relevant for the twins
					new_all_peers = []
					if box in column_peers and peer in column_peers:
						new_all_peers = new_all_peers + column_peers

					if box in row_peers and peer in row_peers:
						new_all_peers = new_all_peers + row_peers

					if box in square_peers and peer in square_peers:
						new_all_peers = new_all_peers + square_peers

					if box in diagonal_peers and peer in diagonal_peers:
						new_all_peers = new_all_peers + diagonal_peers

					for new_peer in new_all_peers:
						if new_peer == box or new_peer == peer:
							#print("\t", box, peer, new_peer, "box or original peer")
							continue
						elif len(values[new_peer]) < len(values[box]):
							#print("\t", new_peer, values[new_peer]," value smaller")
							continue
						else:
							#print("\t", new_peer, values[new_peer])
							for s in values[box]:
								if s in values[new_peer]:
									#print("\treplacing:", new_peer, values[new_peer], values[new_peer].replace(s,""))
									assign_value(values, new_peer, values[new_peer].replace(s,""))
								#else:
									#print("\t", new_peer, "[",values[new_peer],"]does not contain", s)

	return values
	# Eliminate the naked twins as possibilities for their peers

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
	"""
	Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
	If the sudoku is solved, return the sudoku.
	If after an iteration of both functions, the sudoku remains the same, return the sudoku.
	Input: A sudoku in dictionary form.
	Output: The resulting sudoku in dictionary form.
	"""
	solved_values = [box for box in values.keys() if len(values[box]) == 1]
	stalled = False
	while not stalled:
		solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
		values = eliminate(values)
		values = naked_twins(values)
		values = only_choice(values)
		solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
		stalled = solved_values_before == solved_values_after
		if len([box for box in values.keys() if len(values[box]) == 0]):
			return False
	return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
	"""
	Find the solution to a Sudoku grid.
	Args:
		grid(string): a string representing a sudoku grid.
			Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
	Returns:
		The dictionary representation of the final sudoku grid. False if no solution exists.
	"""
	values = search(grid_values(grid))
	return values

if __name__ == '__main__':
	print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

	# original problem
	#diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

	# grid to solve for diagnoal problem
	diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'

	# grid recived from error when submitting using 'udacity submit'
	#diag_sudoku_grid = '..7.1.......................981.5.2....2.49131..9....6........................1.9'

	display(solve(diag_sudoku_grid))
	try:
		from visualize import visualize_assignments
		visualize_assignments(assignments)
	except SystemExit:
		pass
	except:
		print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
