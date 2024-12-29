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
	secret_nums = [secret_num]
	for i in range(n):
		secret_num = secretize(secret_num)
		secret_nums.append(secret_num)
	return secret_nums

def main():
	input = get_input()
	good = []
	for num in input:
		res = n_secretizes(2000, num)
		good.append(res)
	print(sum(good))

def secret_nums_to_prices(secret_nums):
	return [x % 10 for x in secret_nums]

def prices_to_diffs(prices):
	return [0] + [j - i for i, j in zip(prices[:-1], prices[1:])]

def diffs_to_set_of_sequences(diffs):
	return {tuple(diffs[i:i+4]) for i in range(len(diffs) - 3)}

def p2():

	input = get_input()

	# create a master dictionary to hold sequences and their occurrences
	master_seqs = {}
	# for each monkey:
	for secret_num_start in input:
		secret_nums = n_secretizes(2000, secret_num_start)
		# convert secret numbers to prices, then differences
		prices = secret_nums_to_prices(secret_nums)
		diffs = prices_to_diffs(prices)
		# create a set of sequences that appear
		seqs = diffs_to_set_of_sequences(diffs)
		# update the master dictionary with the results of the set (add key if it's a new sequence, add one if it's already in)
		for seq in seqs:
			if seq not in master_seqs.keys():
				master_seqs[seq] = 1
			else:
				master_seqs[seq] += 1
	# iterate through the dictionary to find the sequence where the the sum of the differences * count is highest
	seqs_score = {key: sum(key) * val for key, val in master_seqs.items()}
	print(sorted(seqs_score.items(), key=lambda item: item[1], reverse=True)[:10])

if __name__ == "__main__":
	p2 ()


