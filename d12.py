def get_garden() -> list[list[str]]:
	with open("d12.txt", "r") as file:
		garden:list = []
		return [list(x) for x in file.read().splitlines()]
	
def coord_to_plot(coord:tuple[int,int], garden:list[list[str]]):
	x,y = coord
	rows = len(garden)
	cols = len(garden[0]) if rows > 0 else 0

	# Directions for neighbors: up, down, left, right
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	# plot will contain (x, y, perimeter)
	plot:set[tuple[int,int, int]] = set()
	visited:set[tuple[int,int]] = set()
	edges:list[tuple[int, int, tuple[int, int]]] = []

	def dfs(r, c, current_value):
		# current_path: list of (r, c) coordinates visited so far
		# current_value: value we expect at this step
		
		# If we reached 9, we have a complete sequence from 0 to 9
		if (r,c) in visited:
			return
		
		visited.add((r,c))
		
		if garden[r][c] == current_value:
			matches = 0
			for dr, dc in directions:
				edges.append((r, c, (dr, dc)))
				nr, nc = r + dr, c + dc
				if 0 <= nr < rows and 0 <= nc < cols:
					if garden[nr][nc] == current_value:
						edges.remove((r, c, (dr, dc)))
						dfs(nr, nc, current_value)
			plot.add((r,c, 4-matches))

	dfs(x, y, garden[x][y])

	return plot, edges
	
def garden_to_plots(garden:list[list[str]]):
	# create a set of all coordinates in the garden
	coords_not_in_plot:set[tuple[int, int]] = {(i, j) for i in range(len(garden)) for j in range(len(garden[i]))}
	plots = []
	all_edges = []
	# for coord in coordinates:
	while coords_not_in_plot:
		coord = coords_not_in_plot.pop()
		coords_in_plot, edges = coord_to_plot(coord, garden)
		plots.append(coords_in_plot)
		all_edges.append(edges)
		for coord in coords_in_plot:
			coords_not_in_plot.discard((coord[0], coord[1]))
	return plots, all_edges

def edges_to_directions(edges):
	# convert to North list and West list
	# North is (-1,0)
	# South is (1,0)
	# West is (0,-1)
	# East is (0,1)	

	north_list = []
	south_list = []
	west_list = []
	east_list = []
	for edge in edges:
		x,y,dir = edge
		# if north
		if dir == (-1,0):
			north_list.append((x,y))
		# south
		if dir == (1,0):
			south_list.append((x, y))
		# west
		if dir == (0,-1):
			west_list.append((x,y))
		# east
		if dir == (0,1):
			east_list.append((x,y))
	return north_list, south_list, west_list, east_list

def north_list_to_north_dict(north_list):
	north_dict = {}
	for coord in north_list:
		x,y = coord
		if x in north_dict.keys():
			north_dict[x].append(y)
		else:
			north_dict[x] = [y]
	return north_dict

def west_list_to_west_dict(west_list):
	west_dict = {}
	for coord in west_list:
		x,y = coord
		if y in west_dict.keys():
			west_dict[y].append(x)
		else:
			west_dict[y] = [x]
	return west_dict


def north_dict_to_sides(north_dict):
	sides = []
	for x, ys in north_dict.items():
		# x will be an int
		# ys will be a list of ints
		# we want to reduce ys down to values that don't have the y-1
		new_ys = [y for y in ys if y-1 not in ys]
		for y in new_ys:
			sides.append((x,y))
	return sides

def west_dict_to_sides(west_dict):
	sides = []
	for y, xs in west_dict.items():
		# x will be an int
		# ys will be a list of ints
		# we want to reduce ys down to values that don't have the y-1
		new_xs = [x for x in xs if x-1 not in xs]
		for x in new_xs:
			sides.append((x,y))
	return sides

def edges_to_sides(edges:list[tuple[int,int,tuple[int,int]]]):
	north_list, south_list, west_list, east_list = edges_to_directions(edges)
	north_dict = north_list_to_north_dict(north_list)
	south_dict = north_list_to_north_dict(south_list)
	west_dict = west_list_to_west_dict(west_list)
	east_dict = west_list_to_west_dict(east_list)
	north_sides = north_dict_to_sides(north_dict)
	south_sides = north_dict_to_sides(south_dict)
	west_sides = west_dict_to_sides(west_dict)
	east_sides = west_dict_to_sides(east_dict)
	return len(north_sides) + len(west_sides) + len(south_sides) + len(east_sides)

def plots_to_cost(plots:list[set[tuple[int, int, int]]], all_edges) -> int:
	total = 0
	for plot, edges in zip(plots, all_edges):
		total += len(plot) * edges_to_sides(edges)
	return total

if __name__ == "__main__":
	garden: list[list[str]] = get_garden()
	plots, all_edges = garden_to_plots(garden)
	print(plots_to_cost(plots, all_edges))

	# edges_should_yield_12 = [(0, 0, (-1, 0)), (0, 0, (0, -1)), (0, 1, (-1, 0)), (2, 1, (1, 0)), (0, 2, (-1, 0)), (0, 3, (-1, 0)), (0, 3, (1, 0)), (0, 4, (-1, 0)), (0, 4, (1, 0)), (0, 5, (-1, 0)), (5, 5, (1, 0)), (3, 4, (-1, 0)), (3, 3, (-1, 0)), (5, 3, (1, 0)), (5, 2, (-1, 0)), (5, 2, (1, 0)), (5, 1, (-1, 0)), (5, 1, (1, 0)), (5, 0, (1, 0)), (5, 0, (0, -1)), (4, 3, (0, -1)), (3, 3, (0, -1)), (5, 4, (1, 0)), (5, 5, (0, 1)), (4, 5, (0, 1)), (3, 5, (0, 1)), (2, 5, (0, -1)), (2, 5, (0, 1)), (1, 5, (0, -1)), (1, 5, (0, 1)), (0, 5, (0, 1)), (1, 2, (0, 1)), (2, 2, (1, 0)), (2, 2, (0, 1)), (1, 0, (0, -1)), (2, 0, (0, -1)), (3, 0, (0, -1)), (3, 0, (0, 1)), (4, 0, (0, -1)), (4, 0, (0, 1))]
	# print(sorted(edges_should_yield_12))
	# # print(edges_to_sides(edges_should_yield_12))