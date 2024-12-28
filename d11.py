import functools

def get_stones():
	with open("d11.txt", "r") as file:
		return [int(x) for x in file.read().split(" ")]
	
def part_1(stones:list[int]):
	found = {0:1}
	for j in range(75):
		print(j)
		newStones = []
		for stone in stones:
			
			stoneStr = str(stone)
			stoneChars = len(stoneStr)

			if stone in found.keys():
				val = found[stone]
				if type(val) == tuple:
					newStones.append(val[0])
					newStones.append(val[1])
				else:
					newStones.append(val)

			elif stoneChars % 2 == 0:
				firstHalf = int(stoneStr[:stoneChars//2])
				secondHalf = int(stoneStr[stoneChars//2:])
				newStones.append(firstHalf)
				newStones.append(secondHalf)
				found[stone] = (firstHalf, secondHalf)
			
			else:
				newStones.append(stone * 2024)
				found[stone] = stone * 2024
		stones = newStones
			
			
		
	print(len(stones))


from multiprocessing import Pool

def handle_stone(stone):
	stones = [stone]
	for i in range(75):
		print(i)
		newStones = []
		for stone in stones:
			
			stoneStr = str(stone)
			stoneChars = len(stoneStr)

			if stone == 0:
				newStones.append(1)

			elif stoneChars % 2 == 0:
				firstHalf = int(stoneStr[:stoneChars//2])
				secondHalf = int(stoneStr[stoneChars//2:])
				newStones.append(firstHalf)
				newStones.append(secondHalf)
			
			else:
				newStones.append(stone * 2024)
		stones = newStones
	return len(stones)

def part_2(stones):
	with Pool() as pool:
		results = pool.map(handle_stone, stones)
	print(sum(results))

@functools.cache
def blink_stone_once(stone):
	stoneStr = str(stone)
	stoneChars = len(stoneStr)

	if stone == 0:
		return (1, None)

	elif stoneChars % 2 == 0:
		firstHalf = int(stoneStr[:stoneChars//2])
		secondHalf = int(stoneStr[stoneChars//2:])
		return (firstHalf, secondHalf)
	else:
		return(stone * 2024, None)
	
@functools.cache	
def count_blinks(stone, depth):
	left, right = blink_stone_once(stone)
	if depth == 1:
		if right is not None:
			return 2
		return 1
	else:
		output = count_blinks(left, depth - 1)
		if right is not None:
			output += count_blinks(right, depth-1)
		return output

if __name__ == "__main__":	
	stones = get_stones()
	# part_2(stones)
	total = 0
	for stone in stones:
		total += count_blinks(stone, 75)
	print(total)