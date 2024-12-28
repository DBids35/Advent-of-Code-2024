import re


PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"

def input_to_string():
	
	with open("d3.txt", "r") as file:
		lines = []
		for line in file:
			lines.append(line)

	combined = "".join(lines)
	return combined

def string_to_matches(combined):
	matches = re.findall(PATTERN, combined)
	return matches


# combined = input_to_string()
# matches = string_to_matches(combined)

# sum = 0

# for match in matches:
# 	sum += (int(match[0])*int(match[1]))
# print(sum)

################################################################
# Part 2

extra_pattern = r"don't\(\).*?do\(\)"
test_combined = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# filter out bad pattern
combined = input_to_string()
result = re.sub(extra_pattern, "", combined)
# print(result)
matches = string_to_matches(result)

sum = 0

for match in matches:
	sum += (int(match[0])*int(match[1]))
print(sum)