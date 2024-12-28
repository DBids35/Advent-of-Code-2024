from collections import Counter
from functools import reduce
from operator import mul

GRID_WIDTH = 101
GRID_HEIGHT = 103

def get_input() -> list[str]:
	with open("d14.txt", "r") as file:
		return [x for x in file.read().splitlines()]
	
def input_to_robots(input:list[str]) -> list:
	# split on space,
	# then get what's after the =, 
	# then split on , 
	# then convert to int
	result = [
    tuple(
        tuple(map(int, pair.split('=')[1].split(','))) 
        for pair in s.split()
		)
		for s in input
	]

	return result

def robot_to_position(robot:tuple[tuple[int, int], tuple[int, int]], iterations) -> tuple[int, int]:
	(px, py), (vx,vy) = robot

	open_px = px + iterations*vx
	open_py = py + iterations*vy
	
	final_px = open_px % GRID_WIDTH
	final_py = open_py % GRID_HEIGHT

	return (final_px, final_py)

def position_to_quadrant(position:tuple[int, int]):
	half_x = GRID_WIDTH // 2
	half_y = GRID_HEIGHT // 2

	x,y = position

	print(position)

	if x < half_x and y < half_y:
		return 0
	if x < half_x and y > half_y:
		return 1
	if x > half_x and y < half_y:
		return 2
	if x > half_x and y > half_y:
		return 3
	return None
	

def positions_to_safety_factor(positions:list[tuple[int, int]]) -> int:
	
	qs = []

	for position in positions:
		qs.append(position_to_quadrant(position))
	qs_counter = Counter([x for x in qs if x is not None])
	print(qs_counter)
	return reduce(mul, qs_counter.values(), 1)

def is_symmetric_vertical(arr):
    # Check each row for symmetry
    for row in arr:
        length = len(row)
        # Compare elements from left and right moving towards the center
        for j in range(length // 2):
            if row[j] != row[length - j - 1]:
                return False
    return True

def final_positions_to_count_grid(final_positions):
	# Initialize a 2D list with zero counts
	count_grid = [[0]*(GRID_HEIGHT+1) for _ in range(GRID_WIDTH+1)]

	# Populate the grid
	for x, y in final_positions:
		count_grid[x][y] += 1
	
	return count_grid

if __name__ == "__main__":
	input = get_input()
	robots = input_to_robots(input)
	
	for i in range(10000000):
		print(i)
		final_positions = []
		for robot in robots:
			final_positions.append(robot_to_position(robot, i))
		if max(Counter(final_positions).values()) == 1:
			break
	print(i)

		