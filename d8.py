import itertools
from fractions import Fraction
def get_input() -> list[list[str]]:
	with open("d8.txt", "r") as file:
		lines = file.read().splitlines()
	return [list(line) for line in lines]

def get_frequencies(city_map:list[list[str]]) -> set:
	all_vals = [x for row in city_map for x in row]
	unique_chars = set(all_vals)
	unique_chars.remove('.')
	return unique_chars

def find_antenna_locations(freq:str, city_map:list[list[str]]) -> set:
	indices = set()
	for i, row in enumerate(city_map):
		for j, value in enumerate(row):
			if value == freq:
				indices.add((i, j))
	return indices

def find_pairs_of_antennas(antenna_locations:set) -> set:
	return set(itertools.combinations(antenna_locations, 2))

def find_possible_antinodes(pair) -> set:
	((pair_a_x, pair_a_y), (pair_b_x, pair_b_y)) = pair

	step_x: int = pair_a_x - pair_b_x
	step_y: int = pair_a_y - pair_b_y



	# antinode closer to the first antenna
	# ((2,2), (3,3)) -> (1,1)
	# ((3,3), (2,2)) -> (4,4)
	antinodeOne = (pair_a_x + step_x, pair_a_y + step_y)

	# antinode closer to the second antenna
	# ((2,2), (3,3)) -> (4,4)
	# ((3,3), (2,2)) -> (1,1)
	antinodeTwo = (pair_b_x - step_x, pair_b_y - step_y)
	return {antinodeOne, antinodeTwo}

def in_map(coord: tuple, map_rows: int, map_columns: int) -> bool:
	return 0 <= coord[0] < map_rows and 0 <= coord[1] < map_columns

def find_antinodes(pair, map_rows: int, map_colums: int) -> set:
	possibilities = find_possible_antinodes(pair)
	return {x for x in possibilities if in_map(x, map_rows, map_colums)}

def line_coordinates(p1, p2, x_max, y_max) -> set:
	"""
	Returns a set of all integer coordinate points (x, y)
	that lie on the line passing through p1 and p2,
	where p1 and p2 are tuples like (x1, y1) and (x2, y2).
	Both x and y must be within [0, x_max] and [0, y_max], respectively.
	Excludes the original two points.
	"""

	x1, y1 = p1
	x2, y2 = p2

	coords = set()

	# Handle the vertical line case
	if x1 == x2:
		# Line is x = x1
		if 0 <= x1 <= x_max:
			for y in range(y_max):
				# Exclude the original points
				if not ((x1 == x1 and y == y1) or (x1 == x2 and y == y2)):
					coords.add((x1, y))
		return coords

	# For non-vertical lines, find slope (m) and intercept (c): y = m*x + c
	m = Fraction(y2 - y1, x2 - x1)
	c = y1 - m * x1

	# Check each x in [0, x_max] and see if it produces an integer y on the line
	for x in range(x_max):
		y = m * x + c
		print(y)
		# Check if y is effectively an integer
		if y % 1 == 0:
			print("good")
			y_int = int(round(y))
			if 0 <= y_int <= y_max -1:
				coords.add((x, y_int))
	return coords


def handle_freq(freq:str, city_map:list[list[str]])->set:
	antinodes: set = set()
	# find locations of the particular frequency. 
	antenna_locations = find_antenna_locations(freq, city_map)
	
	pairs_of_antennas = find_pairs_of_antennas(antenna_locations)
	# for each pair of locations:
	for pair in pairs_of_antennas:
		antinodes.update(line_coordinates(pair[0], pair[1], len(city_map), len(city_map[0])))
		# antinodes.update(find_antinodes(pair, len(city_map), len(city_map[0])))
	# find the valid antinodes
	return antinodes

def pretty_print_city_map(city_map:list[list[str]], antinodes:set):
	for i, row in enumerate(city_map):
		for j, val in enumerate(row):
			if (i,j) in antinodes and city_map[i][j] == ".":
				city_map[i][j] = "#"
	for row in ["".join(x) for x in city_map]:
		print(row)

def part_2() -> int:
	city_map:list[list[str]] = get_input()
	freqs:set = get_frequencies(city_map)
	print(freqs)
	# NOTE: An antinode on top of an antenna counts
	# NOTE: We're looking for the number of unique antinode locations within the map

	antinodes:set = set()
	#for freq in freqs
	for freq in freqs:
		antinodes.update(handle_freq(freq, city_map))
	print(sorted(antinodes))
	#pretty_print_city_map(city_map, antinodes)
	return len(antinodes)

if __name__ == "__main__":
	print(part_2())
	# assert(line_coordinates((3,1), (1,3), 5, 5) == {(0,4), (2,2), (4,0)})
