assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
	return [s+t for s in A for t in B]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [['A1','B2','C3','D4','E5','F6','G7','H8','I9'],['A9','B8','C7','D6','E5','F4','G3','H2','I1']]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
						'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
						'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23', 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
						'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'A4': '2357', 'A7': '27',
						'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
						'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2',
						'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379', 'F1': '6',
						'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9',
						'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17', 'D3': '2379', 'B4': '27',
						'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279',
						'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
possible_solutions_1 = [
	{'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9', 'G3': '1', 'G2': '8', 'G1': '7', 'G9': '5', 'G8': '4', 'C9': '1',
	 'C8': '5', 'C3': '8', 'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6', 'C5': '37', 'A4': '2357', 'A9': '8',
	 'A8': '6', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9',
	 'F9': '7', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6', 'C4': '4',
	 'B8': '3', 'B9': '4', 'I9': '9', 'I8': '7', 'I1': '23', 'I3': '23', 'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1',
	 'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9', 'E8': '1', 'A7': '27', 'A6': '257', 'E5': '347',
	 'E4': '6', 'E7': '345', 'E6': '579', 'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2', 'H9': '3', 'H2': '9',
	 'H3': '5', 'H1': '4', 'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6', 'D8': '8', 'D9': '6', 'D6': '279',
	 'D7': '34', 'D4': '237', 'D5': '347', 'D2': '1', 'D3': '79', 'D1': '5'},
	{'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1', 'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8', 'H5': '6', 'F9': '7',
	 'G7': '6', 'G6': '3', 'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8', 'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
	 'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5', 'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237', 'A5': '9',
	 'A4': '2357', 'A7': '27', 'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579', 'C7': '9', 'C6': '6',
	 'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2', 'F6': '125',
	 'A9': '8', 'G4': '9', 'A8': '6', 'E7': '345', 'E3': '79', 'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
	 'F5': '8', 'E2': '3', 'F7': '35', 'F8': '9', 'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9', 'H4': '17',
	 'D3': '79', 'B4': '27', 'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5', 'B3': '6',
	 'D6': '279', 'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4', 'D1': '5'}
	]

before_naked_twins_2 = {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
						'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
						'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '379',
						'C6': '2379', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8', 'D2': '17', 'D3': '9',
						'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
						'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9',
						'F1': '4', 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
						'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345',
						'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7', 'H2': '2', 'H3': '4', 'H4': '9',
						'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3', 'I3': '5',
						'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
possible_solutions_2 = [
	{'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
	 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
	 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
	 'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
	 'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
	 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
	 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
	 'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
	 'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'},
	{'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6', 'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9', 'A9': '1', 'B1': '6',
	 'B2': '9', 'B3': '8', 'B4': '4', 'B5': '3', 'B6': '1', 'B7': '237', 'B8': '5', 'B9': '237', 'C1': '23',
	 'C2': '5', 'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79', 'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
	 'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6', 'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357', 'E1': '5',
	 'E2': '6', 'E3': '2', 'E4': '8', 'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1', 'E9': '9', 'F1': '4',
	 'F2': '17', 'F3': '3', 'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6', 'F8': '8', 'F9': '257', 'G1': '1',
	 'G2': '8', 'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34', 'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
	 'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1', 'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6', 'I1': '9', 'I2': '3',
	 'I3': '5', 'I4': '7', 'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4', 'I9': '8'}
]


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

def only_choice(values):
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
		#print(dict_n_count)

		# entering some random comment
		for key, value in dict_n_count.items():
			if value == 1:
				for box in a_unit:
					if key in values[box]:
						#values[box] = key
						assign_value(values, box, key)

	return values

def reduce_puzzle(values):
	"""Reduce puzzle by calling eliminate and only_choice until stalled."""
	#print("reduce puzzle")
	stalled = False
	while not stalled:
		# Check how many boxes have a determined value
		solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
		# Your code here: Use the Eliminate Strategy
		eliminate(values)
		# Your code here: Use the Only Choice Strategy
		only_choice(values)
		# Check how many boxes have a determined value, to compare
		solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
		# If no new values were added, stop the loop.
		stalled = solved_values_before == solved_values_after
		# Sanity check, return False if there is a box with zero available values:
		if len([box for box in values.keys() if len(values[box]) == 0]):
			return False
	return values

def search(values):
	"""Using depth-first search and propagation, try all possible values."""

	# First, reduce the puzzle using the previous function
	#print("In Search")
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

def naked_twins(values):
	"""Eliminate values using the naked twins strategy.
	Args:
		values(dict): a dictionary of the form {'box_name': '123456789', ...}

	Returns:
		the values dictionary with the naked twins eliminated from peers.
	"""
	row = ['A','B','C','D','E','F','G','H','I']
	#print("\nBefore:")
	#display(values)
	for box, value in values.items():
		# if the box is solved
		if len(value) > 1:
			# find box's row and column unit index
			box_row_idx = rows.index(box[:1])
			box_column_idx = int(box[1:]) - 1

			# find box's square unit index
			for idx, unit in enumerate(square_units):
				if box in unit:
					box_square_idx = idx
					break
			# create list of peers using only the unit index for the box
			#peers = list(set().union(row_units[box_row_idx], column_units[box_column_idx], square_units[box_square_idx]))
			row_peers = row_units[box_row_idx]
			column_peers = column_units[box_column_idx]
			square_peers = square_units[box_square_idx]
			all_peers = [column_peers, row_peers, square_peers]

			# for box's peers
			for set_of_peers in all_peers:
				for peer in set_of_peers:
					#if its value is equal to box's and it isn't the box itself
					if box != peer and values[box] == values[peer]:
						# found naked twin
						# print("Found naked twin", box, peer)
						for new_peer in set_of_peers:
							if len(values[new_peer]) <= len(values[box]):
								#print("length of new row peer value is not LTEQ box value")
								continue
							elif new_peer == box:
								#print("same as naked twins")
								continue
							else:
								#print("\nbox:",box, values[box], "row_peer:", row_peer, values[row_peer], "new_row_peer:", new_row_peer, values[new_row_peer])
								count_in_peer = 0
								for s in values[box]:
									if s in values[new_peer]:
#										count_in_peer += 1
#								if count_in_peer == len(values[box]):
#									for s in values[box]:
										assign_value(values, new_peer, values[new_peer].replace(s,""))
								#print("\tnew peer value", values[new_row_peer])
	#print("\nAfter:")
	#display(values)
	return values
	# Eliminate the naked twins as possibilities for their peers

def solve(grid):
	"""
	Find the solution to a Sudoku grid.
	Args:
		grid(string): a string representing a sudoku grid.
			Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
	Returns:
		The dictionary representation of the final sudoku grid. False if no solution exists.
	"""
	#print("In solve")

	"""
	values = grid_values(grid)
	values = search(values)
	return values

	"""

	print("\n\nOriginal Problem")
	display(before_naked_twins_2)
	print("\n\ncalling naked twins")
	values = naked_twins(before_naked_twins_2)
	print("\n\nPriting my solution")
	display(values)
	#print("\n\n")
	print("\n\nPrinting correct solution #1")
	display(possible_solutions_2[0])
	print("\n\nPrinting correct solution #2")
	display(possible_solutions_2[1])
	print("\n\nDone printing")
	return values

if __name__ == '__main__':
	#diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
	diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
	display(solve(diag_sudoku_grid))
	try:
		from visualize import visualize_assignments
		visualize_assignments(assignments)
	except SystemExit:
		pass
	except:
		print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
