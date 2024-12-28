def get_topo_map() -> list[list[int]]:
	with open("d10.txt", "r") as file:
		topo_map:list = []
		for line in file.read().splitlines():
			topo_map.append([int(x) for x in list(line)])
		return topo_map
	
def get_points_of_one_elevation(elevation:int, topo_map:list[list[int]]) -> set[tuple]:
	indices = set()
	for i, row in enumerate(topo_map):
		for j, value in enumerate(row):
			if value == elevation:
				indices.add((i, j))
	return indices

def check_coord(coord:tuple, elevation:int, topo_map:list[list[int]]) -> bool:
	x,y = coord
	up = topo_map[x][y]
	if up == elevation + 1:
		return True
	return False

def coord_to_new_options(coord:tuple, topo_map:list[list[int]]) -> set[tuple]:
	x, y = coord
	elevation = topo_map[x][y]

	new_options = set()
	
	#check up
	if x != 0:
		if check_coord((x-1, y), elevation, topo_map):
			new_options.add((x-1, y))

	# check down
	if x != len(topo_map)-1:
		if check_coord((x+1, y), elevation, topo_map):
			new_options.add((x+1, y))
	
	# check left
	if y != 0:
		if check_coord((x, y-1), elevation, topo_map):
			new_options.add((x, y-1))
	# check right
	if y != len(topo_map[0])-1:
		if check_coord((x, y+1), elevation, topo_map):
			new_options.add((x, y+1))
	return new_options

def trailhead_to_num_peaks(trailhead:tuple, topo_map:list[list[int]]) -> int:
	last_elevation_coords = {trailhead}

	# for elevation in range 0 to 9
	for elevation in range(1,10):
		this_elevation_coords = set()

		# get new_options and add them to accessible
		for coord in last_elevation_coords:
			this_elevation_coords.update(coord_to_new_options(coord, topo_map))
		last_elevation_coords = this_elevation_coords
	return len(this_elevation_coords)

# for each trailhead, 
# search everywhere on the map I can get to
# how many peaks can I get to?

topo_map:list[list[int]] = get_topo_map()
trailheads: set[tuple] = get_points_of_one_elevation(0, topo_map)

def part_1(trailheads, topo_map):
	sum_peaks = 0
	for trailhead in trailheads:
		sum_peaks += trailhead_to_num_peaks(trailhead, topo_map)
	print(sum_peaks)

def find_trailhead_to_peak_paths(trailhead, peak, topo_map):
	pass

def part_2(trailheads:set[tuple], topo_map:list[list[int]]):
	# get all peaks
	peaks: set[tuple] = get_points_of_one_elevation(9, topo_map)
	# for trailhead in trailhead
	for trailhead in trailheads:
		# for peak in peaks
		for peak in peaks:
			# find the paths from trailhead to peak
			paths = find_trailhead_to_peak_paths(trailhead, peak, topo_map)
			# count them
	pass
