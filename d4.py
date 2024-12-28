
def input_to_array():
	with open("d4.txt", "r") as file:
		lines = []
		for line in file:
			line = line.replace("\n", "")
			lines.append([c for c in line])
	return lines

def rotate_2d_list(lines, num=1):

	for i in range(num):
		lines = list(zip(*lines[::-1]))
	return lines

def check_right(lines):
	total = 0
	# for every row
	for i in range(len(lines)):
		# for every column except the last three
		for j in range(len(lines[0])-3):
			if lines[i][j] == 'X' and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
				total+=1
	return total

def check_diagonal(lines):
	total = 0
	# for every row
	for i in range(len(lines)-3):
		# for every column except the last three
		for j in range(len(lines[0])-3):
			if lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
				total+=1
	return total

def check_mas(lines):
	total = 0
	# for every row
	for i in range(len(lines)-2):
		# for every column except the last three
		for j in range(len(lines[0])-2):
			# L -> R, L -> R
			#M S
			# A
			#M S
			if lines[i][j] == 'M' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'S' and lines[i+2][j] == 'M' and lines[i][j+2] == "S":
				total+=1

			#M M
			# A
			#S S
			elif lines[i][j] == 'M' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'S' and lines[i+2][j] == 'S' and lines[i][j+2] == "M":
				total+=1

			#S S
			# A
			#M M
			elif lines[i][j] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'M' and lines[i+2][j] == 'M' and lines[i][j+2] == "S":
				total+=1
			
			#S M
			# A
			#S M
			elif lines[i][j] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'M' and lines[i+2][j] == 'S' and lines[i][j+2] == "M":
				total+=1
			
	return total

lines = input_to_array()
# right_total = check_right(lines) + check_right(rotate_2d_list(lines, 1)) + check_right(rotate_2d_list(lines, 2)) + check_right(rotate_2d_list(lines, 3))
# diagonal_total = check_diagonal(lines) + check_diagonal(rotate_2d_list(lines, 1)) + check_diagonal(rotate_2d_list(lines, 2)) + check_diagonal(rotate_2d_list(lines, 3))

# print(right_total + diagonal_total)
print(check_mas(lines))