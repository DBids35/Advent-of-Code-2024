
def input_to_list():
	with open("d6.txt", "r") as file:
		lines = file.read().splitlines()
	return lines

def list_to_2d(lines):
	return [list(x) for x in lines]


def find_security_start(cleaned):
	# Character to find
	target = '^'

	# Find the character
	for row_idx, row in enumerate(cleaned):
		for col_idx, char in enumerate(row):
			if char == target:
				return (row_idx, col_idx)
			
def position_in_map(position, map_rows, map_columns):
	if type(position) != tuple:
		print(position)
	return 0 <= position[0] < map_rows and 0 <= position[1] < map_columns
			
def find_next_position(current_position, current_direction, cleaned_map):
	
	next_desired_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
	
	# position out of map
	if not position_in_map(next_desired_position, len(cleaned_map), len(cleaned_map[0])):
		# return the out of map position
		return next_desired_position, current_direction
	
	next_desired_position_ok = cleaned_map[next_desired_position[0]][next_desired_position[1]] != "#"

	# position in map and not #
	if next_desired_position_ok:
		return next_desired_position, current_direction
	
	# position in map and #
	else:
		return current_position, direction_to_new_direction(current_direction)

def direction_to_new_direction(direction):
	# if direction is up
	if direction == (-1,0):
		# return right
		return (0,1)
	elif direction == (0,1):
		return (1,0)
	elif direction == (1,0):
		return (0,-1)
	elif direction == (0,-1):
		return (-1,0)
	else:
		print("Bad direction inputted")

original_map = list_to_2d(input_to_list())

def get_squares_touched(cleaned_map):
	# Directions:
	# - Up: (-1, 0)
	# - Right: (0, 1)
	# - Down: (1, 0)
	# - Left: (0, -1)
	current_direction = (-1,0)

	current_position = find_security_start(cleaned_map)

	squares_touched = set()
	loop = False
	while position_in_map(current_position, len(cleaned_map), len(cleaned_map[0])):
		# algorithm to proceed through
		squares_touched.add((current_position[0], current_position[1], current_direction[0], current_direction[1]))

		current_position, current_direction = find_next_position(current_position, current_direction, cleaned_map)

		# if the position is in the set of positions touched and the direction is the same as the last position (not just rotated)
		if (current_position[0], current_position[1], current_direction[0], current_direction[1]) in squares_touched:
			loop = True
			break
	squares_touched = list(set([(x,y) for x, y, d1, d2 in squares_touched]))
	return squares_touched, loop

################################
# Part 2
# make a list of all coordinates that contain "."
# iterate through that, adding a #

touched, loop = get_squares_touched(original_map)

start = find_security_start(original_map)

loop_created = 0
for coordinate in [x for x in touched if x != start]:
	# replace the . with a # at the coordinate
	original_map[coordinate[0]][coordinate[1]] = "#"

	touched, loop = get_squares_touched(original_map)
	if loop:
		loop_created +=1
	
	original_map[coordinate[0]][coordinate[1]] = "."
print(loop_created)