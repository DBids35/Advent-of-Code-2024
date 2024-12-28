
from itertools import groupby
# locks: top filled and bottom empty
# keys: bottom filled and top empty

def get_input() -> list[str]:
	with open("d25.txt", "r") as file:
		return [x for x in file.read().splitlines()]
	

def input_to_list_of_lists(input):
	return [list(group) for key, group in groupby(input, key=lambda x: x != '') if key]

def format_keys(keys:list[list[str]]) -> list[list[list[int]]]:
	return [[row.count("#") for row in zip(*key[:-1][::-1])] for key in keys]

def format_locks(locks:list[list[str]]) -> list[list[list[int]]]:
	# top row will be full
	# remove top row
	# rotate 2d array
	return [[row.count("#") for row in zip(*lock[1:][::-1])] for lock in locks]

def input_to_keys_and_locks(input: list[list[str]]) -> tuple[list[list[list[int]]], list[list[list[int]]]]:
	keys = [x for x in input if x[0] == "....." and x[6] == "#####"]
	locks = [x for x in input if x not in keys]

	return format_keys(keys), format_locks(locks)

def main():
	input = get_input()
	input = input_to_list_of_lists(input)
	keys, locks = input_to_keys_and_locks(input)
	print(locks)
	return keys, locks

if __name__ == "__main__":
	keys, locks = main()