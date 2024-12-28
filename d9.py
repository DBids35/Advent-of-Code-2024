def get_disk_map() -> list[int]:
	with open("d9.txt", "r") as file:
		return [int(x) for x in list(file.read())]
	
def disk_map_to_storage_view(disk_map:list[int]) -> list:
	storage_view = []
	for i, num in enumerate(disk_map):
		# if i is even:
		if i%2 == 0:
			# append to string i repeated num times
			for j in range(num):
				storage_view.append(int(i/2))
		else:
			for k in range(num):
				storage_view.append(".")
	return storage_view

def compress(storage_view:list) -> list:
	periods = storage_view.count('.')
	just_characters_to_insert = [x for x in storage_view if x != '.'][:-(periods+1):-1]
	
	for char in just_characters_to_insert:
		# insert into first place in storage view that contains a .
		# Original list

		# Replace the first instance of 2 with "."
		if '.' in storage_view:
			index = storage_view.index('.')  # Find the index of the first instance of 2
			storage_view[index] = char     # Replace it with "."

	return storage_view[:-periods]

def first_space_big_enough(storage_view, size_needed):
	periods = ["." for i in range(size_needed)]
	for i in range(len(storage_view) - len(periods) + 1):
		if storage_view[i:i + len(periods)] == periods:
			return i
	return -1  # Return -1 if not found

def compress2(storage_view:list) -> list:
	# create a list of ids from max to min

	unique_ints = {x for x in storage_view if x != "."}
	unique_ints = sorted(unique_ints)[::-1]
	print(storage_view)
	# for each id:
	for id in unique_ints:
		# count how many show up
		id_count = storage_view.count(id)
		# find the first instance of that many or more periods
		first_space = first_space_big_enough(storage_view, id_count)
		id_index = storage_view.index(id)
		if -1 < first_space < id_index:
			
			for i in range(id_count):
				# delete the old instance
				storage_view[id_index + i] = '.'
				# add the new instance
				storage_view[first_space + i] = id

	return storage_view

def checksum(compressed:list) -> int:
	sum = 0

	for i, num in enumerate([int(x) if x != '.' else 0 for x in compressed]):
		sum+=(i*num)
	return sum

disk_map = get_disk_map()
storage_view = disk_map_to_storage_view(disk_map)
compressed = compress2(storage_view)
print(checksum(compressed))
