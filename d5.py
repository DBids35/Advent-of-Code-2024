from collections import defaultdict, deque

def input_to_list():
	lines = []

	with open("d5.txt", "r") as file:
		for line in file:
			lines.append(line)

	return lines

def clean_rules(rules):
	return [[int(y) for y in x.split('|')] for x in rules]

def clean_updates(updates):
	return [[int(y) for y in x.split(",")] for x in updates]

def input_to_rules_and_updates():

	rules = []
	updates = []

	for line in input_to_list():
		line = line.replace("\n", "")
		if line == "":
			continue
		elif "|" in line:
			rules.append(line)
		else:
			updates.append(line)

	rules = clean_rules(rules)
	updates = clean_updates(updates)

	return rules, updates

rules, updates = input_to_rules_and_updates()

#####################################
# Part 1:

def check_rule_met(rule, update):
	if rule[0] in update and rule[1] in update:
		if update.index(rule[0]) > update.index(rule[1]):
			return False
	return True

def find_middle(update):
	middleIndex = len(update)//2
	return update[middleIndex]

middle_sum = 0
bad_updates = []
for update in updates:
	middle = find_middle(update)
	failed = False
	# go through all rules, for relevant ones, check if they are met
	for rule in rules:
		if not check_rule_met(rule, update):
			failed = True
	if not failed:
		middle_sum += middle
	else:
		bad_updates.append(update)
# print(middle_sum)


def reorder_bad_update(rules, all_numbers):
	# Build graph and in-degree dictionary
	graph = defaultdict(list)
	in_degree = {num: 0 for num in all_numbers}  # Ensure all numbers are initialized

	# Add rules to the graph
	for x, y in rules:
		if x in all_numbers and y in all_numbers:
			graph[x].append(y)
			in_degree[y] += 1

	# Perform topological sorting using Kahn's algorithm
	queue = deque([node for node in in_degree if in_degree[node] == 0])  # Nodes with in-degree 0
	sorted_order = []

	while queue:
		current = queue.popleft()
		sorted_order.append(current)
		for neighbor in graph[current]:
			in_degree[neighbor] -= 1
			if in_degree[neighbor] == 0:
				queue.append(neighbor)

	return sorted_order


reordered_middle_sum = 0
for update in bad_updates:
	good_update = reorder_bad_update(rules, update)
	reordered_middle_sum += find_middle(good_update)

print(reordered_middle_sum)