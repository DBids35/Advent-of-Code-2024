import itertools


def process_input(lines):
	processed_lines = {}
	for line in lines:
		line = line.split(':')
		ans = int(line[0])
		# TODO: are these answers unique?
		# Assumption made that all answers are unique, must update dict to list if not
		processed_lines[ans] = [int(x) for x in line[1].split(" ")[1:]]
	return processed_lines, len(lines)

def get_input():
	with open("d7.txt", "r") as file:
		lines = file.read().splitlines()
	lines, original_len = process_input(lines)
	return lines, original_len

def val_len_to_symbol_list(val_len):
	all_permutations = [list(seq) for seq in itertools.product(["+", "*"], repeat=val_len -1 )]
	return all_permutations

def compute_row(vals, symbol_permutation):
	assert(len(vals)==len(symbol_permutation) + 1)
	total = vals[0]
	for i, symbol in enumerate(symbol_permutation):
		assert symbol in ("+", "*")
		if symbol == "*":
			total = total * vals[i+1]
		elif symbol == "+":
			total = total + vals[i+1]
	return total

def try_combos(ans, vals):
	symbol_permutations = val_len_to_symbol_list(len(vals))
	for perm in symbol_permutations:
		if compute_row(vals, perm) == ans:
			return True
	# try each permutation of + and * in between the vals
		# create a list of permutations of the symbols for the length of row (length - 1)
		# write a function that takes the list of numbers and a list of symbols and computes the answer
	# return True as soon as one works
	# return False at the end
	return False

# input_dict, original_len = get_input()
# assert(len(input_dict) == original_len)
# success = 0
# # iterate through dictionary
# for ans, vals in input_dict.items():
# 	if try_combos(ans, vals):
# 		success += ans
# print(success)

##############################################################
# Part 2


def val_len_to_symbol_list(val_len):
	all_permutations = [list(seq) for seq in itertools.product(["+", "*", "|"], repeat=val_len -1 )]
	return all_permutations

def compute_row(vals, symbol_permutation):
	assert(len(vals)==len(symbol_permutation) + 1)
	total = vals[0]
	for i, symbol in enumerate(symbol_permutation):
		assert symbol in ("+", "*", "|")
		if symbol == "*":
			total = total * vals[i+1]
		elif symbol == "+":
			total = total + vals[i+1]
		elif symbol == "|":
			total = int(str(total) + str(vals[i+1]))
	return total

input_dict, original_len = get_input()
assert(len(input_dict) == original_len)
success = 0
# iterate through dictionary
for ans, vals in input_dict.items():
	if try_combos(ans, vals):
		success += ans
print(success)
