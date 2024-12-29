def get_input():
	with open("d22.txt", "r") as file:
		return  [int(x) for x in file.read().splitlines()]
	
def mix(val:int, secret_number: int) -> int:
	return val ^ secret_number

def prune(secret_number:int) -> int:
	return secret_number % 16777216

def secretize(secret_number: int) -> int:
	val = secret_number * 64
	num = mix(val, secret_number)
	num = prune(num)
	val = num // 32
	num = mix(val, num)
	num = prune(num)
	val = num * 2048
	num = mix(val, num)
	return prune(num)

def n_secretizes(n, secret_num):
	for i in range(n):
		secret_num = secretize(secret_num)
	return secret_num

def main():
	input = get_input()
	good = []
	for num in input:
		res = n_secretizes(2000, num)
		good.append(res)
	print(sum(good))

def p2():
	# create a master dictionary to hold sequences and their occurrences
	# for each monkey:
	#	convert secret numbers to prices, then differences
	# 	create a set of sequences that appear
	#	update the master dictionary with the results of the set (add key if it's a new sequence, add one if it's already in)
	# iterate through the dictionary to find the sequence where the the sum of the differences * count is highest
	pass

if __name__ == "__main__":
	main()


