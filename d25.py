
from itertools import groupby
# locks: top filled and bottom empty
# keys: bottom filled and top empty

def get_input() -> list[str]:
	with open("d25.txt", "r") as file:
		return [x for x in file.read().splitlines()]
	

def input_to_list_of_lists(input):
	return [list(group) for key, group in groupby(input, key=lambda x: x != '') if key]

def keys_format(keys:list[list[str]]) -> list[list[int]]:
	pass

def input_to_keys_and_locks(input: list[str]) -> tuple[list[list[int]], list[list[int]]]:
	list_of_lists = input_to_list_of_lists(input)
	keys = [x for x in list_of_lists if x[0] == "....." and x[6] == "#####"]
	locks = [x for x in list_of_lists if x not in keys]

	return [[1]], [[3]]

def main():
	input = get_input()

	return input

if __name__ == "__main__":
	print(main())