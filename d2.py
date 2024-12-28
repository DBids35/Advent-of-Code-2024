from itertools import pairwise

def safe_jump(l, r):
	# right must be at least 1 more than left, but no more than 3 more than left
	if 1 <= r-l <= 3:
		return True
	return False
	
def check_safe(report):
	safe_sum = 0
	for pair in pairwise(report):
		safe_sum += safe_jump(pair[0], pair[1])
	if safe_sum == len(report)-1:
		return True
	return False

with open("d2.txt", "r") as file:
	reports = []
	for line in file:
		reports.append(list(map(int, line.split())))

# safe = 0

# for report in reports:
# 	if check_safe(report) or check_safe(report[::-1]):
# 		safe +=1
# print(safe)

####################################################################
# Part 2

def remove_one(report):
	combinations = []
	for i in range(len(report)):
		combinations.append([num for idx, num in enumerate(report) if idx != i])
	return combinations

safe = 0

for report in reports:
	# get all combinations of removing one value
	combinations = remove_one(report)

	good = 0
	# for each of those combinations
	for combo in combinations:
		if check_safe(combo) or check_safe(combo[::-1]):
			good += 1
	if good > 0:
		safe +=1
print(safe)
