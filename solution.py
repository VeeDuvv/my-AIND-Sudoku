from time import gmtime, strftime

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
	return [s+t for s in A for t in B]

naked_twin_test_problem = {'A1':'2345689', 'A2':'234568', 'A3':'7',
'A4':'34568', 'A5':'1', 'A6':'23689', 'A7':'234568', 'A8':'345689',
'A9':'2458', 'B1':'2345689', 'B2':'1234568', 'B3':'1234569', 'B4':'345678',
'B5':'23456789', 'B6':'236789', 'B7':'2345678', 'B8':'3456789', 'B9':'124578',
'C1':'2345689', 'C2':'1234568', 'C3':'1234569', 'C4':'345678', 'C5':'23456789',
'C6':'236789', 'C7':'2345678', 'C8':'3456789', 'C9':'124578', 'D1':'36',
'D2':'9', 'D3':'8', 'D4':'1', 'D5':'36', 'D6':'5', 'D7':'47', 'D8':'2',
'D9':'47', 'E1':'567', 'E2':'567', 'E3':'56', 'E4':'2', 'E5':'678', 'E6':'4',
'E7':'9', 'E8':'1', 'E9':'3', 'F1':'1', 'F2':'24', 'F3':'24', 'F4':'9',
'F5':'37', 'F6':'37', 'F7':'58', 'F8':'58', 'F9':'6', 'G1':'23456789',
'G2':'12345678', 'G3':'1234569', 'G4':'345678', 'G5':'23456789',
'G6':'1236789', 'G7':'2345678', 'G8':'345678', 'G9':'24578', 'H1':'23456789',
'H2':'12345678', 'H3':'1234569', 'H4':'345678', 'H5':'23456789',
'H6':'1236789', 'H7':'2345678', 'H8':'345678','H9':'24578', 'I1':'2345678',
'I2':'2345678', 'I3':'23456', 'I4':'345678', 'I5':'2345678', 'I6':'23678',
'I7':'1', 'I8':'345678', 'I9':'9'}

naked_twin_test_solution = {'A1':'2345689', 'A2':'234568', 'A3':'7',
'A4':'34568', 'A5':'1', 'A6':'23689', 'A7':'234568', 'A8':'345689',
'A9':'2458', 'B1':'2345689', 'B2':'1234568', 'B3':'1234569', 'B4':'345678',
'B5':'23456789', 'B6':'236789', 'B7':'2345678', 'B8':'3456789', 'B9':'124578',
'C1':'2345689', 'C2':'1234568', 'C3':'1234569', 'C4':'345678', 'C5':'23456789',
'C6':'236789', 'C7':'2345678', 'C8':'3456789', 'C9':'124578', 'D1':'36',
'D2':'9', 'D3':'8', 'D4':'1', 'D5':'6', 'D6':'5', 'D7':'47', 'D8':'2',
'D9':'47', 'E1':'567', 'E2':'567', 'E3':'56', 'E4':'2', 'E5':'68', 'E6':'4',
'E7':'9', 'E8':'1', 'E9':'3', 'F1':'1', 'F2':'24', 'F3':'24', 'F4':'9',
'F5':'37', 'F6':'37', 'F7':'58', 'F8':'58', 'F9':'6', 'G1':'23456789',
'G2':'12345678', 'G3':'1234569', 'G4':'345678', 'G5':'23456789',
'G6':'1236789', 'G7':'2345678', 'G8':'345678', 'G9':'24578', 'H1':'23456789',
'H2':'12345678', 'H3':'1234569', 'H4':'345678', 'H5':'23456789',
'H6':'1236789', 'H7':'2345678', 'H8':'345678','H9':'24578', 'I1':'2345678',
'I2':'2345678', 'I3':'23456', 'I4':'345678', 'I5':'2345678', 'I6':'23678',
'I7':'1', 'I8':'345678', 'I9':'9'}


boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
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

def cross(A, B):
	"""Cross product of elements in A and elements in B."""
	return [s+t for s in A for t in B]

def grid_values(grid):

	"""
	Convert grid into a dict of {square: char} with '123456789' for empties.
	Args:
		grid(string) - A grid in string form.
	Returns:
		A grid in dictionary form
			Keys: The boxes, e.g., 'A1'
			Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
	"""
	# print("In grid_values")
	# create an empty dictionary
	dict_grid={}
	#iterate over te grid, and for each element in the grid, insert the in the dictionary
	for i in range(len(grid)):
		# if value of box is empty "." then replace it with "123456789"
		if grid[i] == '.':
			dict_grid.update({boxes[i]:'123456789'})
		else:
			dict_grid.update({boxes[i]:grid[i]})

	return dict_grid

def display(values):
	"""
	Display the values as a 2-D grid.
	Args:
		values(dict): The sudoku in dictionary form
	"""

	# count of boxes traversed
	num_boxes = 0
	print_value = ""
	#print(values)

	for box, value in values.items():
		print_value = print_value + value + "\t"
		if num_boxes > 0 and (num_boxes+1) %9 == 0:
			print (print_value)
			print_value = ""
		num_boxes += 1
	#pass

def eliminate(values):
	"""
	For boxes with correct values, eliminate those values from the row, column, square and diagonal peers.
	Args:
		values(dict): The sudoku in dictionary form.
	Returns:
		the values dictionary after eliminating all obvious choices.
	"""
	#print("In eliminate")
	row=['A','B','C','D','E','F','G','H','I']

	# for each box in the dictionary
	for box, value in values.items():
		# if the box is solved
		if len(value) == 1:
			# find box's row and column unit index
			box_row_idx = rows.index(box[:1])
			box_column_idx = int(box[1:]) - 1

			# find box's square unit index
			for idx, unit in enumerate(square_units):
				if box in unit:
					box_square_idx = idx
					break
			if box in diagonal_units[0]:
				peers = list(set().union(row_units[box_row_idx], column_units[box_column_idx], square_units[box_square_idx], diagonal_units[0]))
			elif box in diagonal_units[1]:
				peers = list(set().union(row_units[box_row_idx], column_units[box_column_idx], square_units[box_square_idx], diagonal_units[1]))
			else:
				peers = list(set().union(row_units[box_row_idx], column_units[box_column_idx], square_units[box_square_idx]))
			# for each peer, if it's unsolved, remove box's value from peer's value options
			for peer in peers:
				old_peer_value = values[peer]
				if box != peer and len(old_peer_value) > 1:
					new_peer_value = old_peer_value.replace(value,"")
					assign_value(values, peer, new_peer_value)
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
	For each unit, count the possible values for each digit.
	Then for the boxes with only one possible value, assign it to the dictionary
	Args:
		values(dict): The sudoku in dictionary form.
	Returns:
		the values dictionary after looking for only choices.
	"""
	#print("In only_choice")
	all_units = row_units + column_units + square_units + diagonal_units

	# check each unit
	for a_unit in all_units:

		# for each unit, initialize the number count
		dict_n_count = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

		for box in a_unit:
			box_val = values[box]
			for s in box_val:
				dict_n_count[s] = int(dict_n_count[s]) + 1

		# entering some random comment
		for key, value in dict_n_count.items():
			if value == 1:
				for box in a_unit:
					if key in values[box]:
						assign_value(values, box, key)

	return values

def reduce_puzzle(values):
	"""Reduce puzzle by calling eliminate and only_choice until stalled.
	Display the values as a 2-D grid.
	Args:
		values(dict): The sudoku in dictionary form.
	Returns:
		the values dictionary after reducing puzzle.
	"""

	stalled = False
	while not stalled:
		# Check how many boxes have a determined value
		solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

		values = eliminate(values) # eliminate value
		values = naked_twins(values) # implement naked twins
		values = only_choice(values) # prune using only choice

		# Check how many boxes have a determined value, to compare
		solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])

		# If no new values were added, stop the loop.
		stalled = solved_values_before == solved_values_after

		# Sanity check, return False if there is a box with zero available values:
		if len([box for box in values.keys() if len(values[box]) == 0]):
			return False
	return values

def search(values):
	"""Using depth-first search and propagation, try all possible values.
	Args:
		values(dict): The sudoku in dictionary form
	Returns:
		the values dictionary with depth first search done.
	"""
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
	return values

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

	"""
	print("\n\nOriginal Problem")
	display(naked_twin_test_problem)
	values = naked_twins(naked_twin_test_problem)
	print("\n\nPriting my solution")
	display(values)
	print("\n\nPriting naked_twin_test_solution")
	display(naked_twin_test_solution)
	print("\n\nPriting my solution again\n")
	"""

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
