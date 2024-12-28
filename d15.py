def get_input():
	with open("d15.txt", "r") as file:
		return [x for x in file.read().splitlines()]

def input_to_grid_and_directions(input):
	# up: (-1, 0)
	# down: (1, 0)
	# left: (0, -1)
	# right: (0, 1)
	split_index = input.index("")

	# Slice into two lists: before and after the empty string
	grid = input[:split_index]
	sequence = "".join(input[split_index+1:])
	
	sequence = [(-1,0) if x == "^" else (1,0) if x=="v" else (0,-1) if x=="<" else (0,1) if x==">" else None for x in list(sequence)]
	grid = [list(x) for x in grid]
	return grid, sequence

def find_robot(grid) -> tuple[int, int]:
	for i, row in enumerate(grid):
		for j, val in enumerate(row):
			if val == "@":
				return (i, j)
	print("Find Robot Failed")
	return (-999,-999)

def get_robot_view(robot, grid, direction) -> list:

	rx, ry = robot
	dx, dy = direction
	view = []
	for i in range(len(grid)):
		tile = grid[rx + i*dx][ry + i*dy]
		if tile == "#":
			return view
		if tile == ".":
			view.append(tile)
			return view
		view.append(tile)
	print("Couldn't find wall")
	return view

def get_robot_view_p2(robot, grid, direction):
	
	'''
	#
	[]
	.[]
	..[]
	.[]
	.@

	Up

	[
	["@", "[", "."]
	["X", "]", "["]
	["X", "X", "]"]
	]'''
	# this is only handling up and down directions
	rx, ry = robot
	dx, dy = direction
	# views will look like {(0,1): ["[", ".", "["]}
	incomplete_views = {(rx, ry):["@"]}
	complete_views = {}
	i = 1
	while incomplete_views:

		for key in list(incomplete_views.keys()):
			# if robot starts at 3,3
			# direction is up
			# hits "[" right away (2,3) i is 1
			# new view that starts at 2,4
			# i is 2
			# want to be checking 1,4 in the new view

			current_x = key[0]+ len(incomplete_views[key])*dx
			current_y = key[1]+len(incomplete_views[key])*dy
			# update phase
			val_to_consider = grid[current_x][current_y]

			if val_to_consider == "#":
				return {}
			
			if val_to_consider == ".":
				# Remove the key-value pair from dict1 and store the value
				complete_views[key] = incomplete_views.pop(key, None)
				

			elif val_to_consider == "[":
				# if direction is down and current_x
				# create a new incomplete view that starts one to the right of the current coords
				incomplete_views[(current_x, current_y + 1)]=["]"]

				# append val_to_consider to the incomplete view
				incomplete_views[key].append(val_to_consider)

			elif val_to_consider == "]":
				# create a new incomplete view that starts one to the right of the current coords
				incomplete_views[(current_x, current_y - 1)]=["["]
				# append val_to_consider to the incomplete view
				incomplete_views[key].append(val_to_consider)

		i +=1
	# if we get past the while, all views have been completed
	# this means that every box can move

	return complete_views

def modify_grid_with_view(grid, view, direction, robot):
	rx, ry = robot
	dx, dy = direction
	grid[rx][ry] = "."
	for i, val in enumerate(view):
		grid[rx+(i+1)*dx][ry+(i+1)*dy] = val
	return grid

def modify_grid_with_view_p2(grid, view, direction, start):
	rx, ry = start
	dx, dy = direction
	for i, val in enumerate(view):
		grid[rx+(i)*dx][ry+(i)*dy] = val
	return grid

def horizontal(grid, direction, robot):
	view = get_robot_view(robot, grid, direction)

	if "." not in view:
		return grid, robot
	# all the following have a space
	# view will be some combination of boxes and/or spaces
	first_space = view.index(".")
	view[:first_space+1] = view[:first_space]
	grid = modify_grid_with_view(grid, view, direction, robot)
	return grid, (robot[0]+direction[0], robot[1]+direction[1])

def merge_views(views, direction):
	# {(4, 4): ['@', '[', '['], (3, 5): [']', ']'], (2, 5): [']'], (2, 4): ['[']}
	# the last two views add no information, should be removed
	# view into a list of coordinates
	coords_seen = set()

	good_views = {}
	for key, val in views.items():
		if key not in coords_seen:
			good_views[key] = val
		for i in range(len(views[key])):
			coords_seen.add((key[0] + direction[0]*i, key[1] + direction[1]*i))

	return good_views

def vertical(grid, direction, robot):
	views = get_robot_view_p2(robot, grid, direction)

	if views == {}:
		return grid, robot
	
	views = merge_views(views, direction)

	for key, view in views.items():
		view.insert(0, ".")
		grid = modify_grid_with_view_p2(grid, view,  direction, key)

	return grid, (robot[0]+direction[0], robot[1]+direction[1])

def step(grid, direction, robot):
	# create a list of characters between the robot and the next wall in the direction
	# call this "view"
	if direction[0] == 0:
		grid, robot = horizontal(grid, direction, robot)
	else: 
		grid, robot = vertical(grid, direction, robot)

	return grid, robot

	

def grid_to_sum(grid):
	sum = 0
	for i, row in enumerate(grid):
		for j, val in enumerate(row):
			if val == "[":
				sum += i*100 + j
	return sum

def grid_to_p2_grid(grid):
	new_grid = []
	for row in grid:
		new_row = []
		for val in row:
			if val == "#":
				new_row.append("#")
				new_row.append("#")
			elif val == "O":
				new_row.append("[")
				new_row.append("]")
			elif val == ".":
				new_row.append(".")
				new_row.append(".")
			elif val == "@":
				new_row.append("@")
				new_row.append(".")
			else:
				print("uhoh")
				new_row.append(val)
		new_grid.append(new_row)

	return new_grid

if __name__ == "__main__":
	inp = get_input()
	grid, directions = input_to_grid_and_directions(inp)

	grid = grid_to_p2_grid(grid)

	robot = find_robot(grid)
	for direction in directions:
		# return where robot ended and pass it in
		grid, robot = step(grid, direction, robot)
		
	sum = grid_to_sum(grid)
	print(sum)

	# views = {(4, 4): ['@', '[', '['], (3, 5): [']', ']'], (2, 5): [']'], (2, 4): ['[']}
	# print(merge_views(views, (-1,0)))
	