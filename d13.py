from math import gcd

def get_input() -> list[str]:
	with open("d13.txt", "r") as file:
		return [x for x in file.read().splitlines()]
		

def button_str_to_tuple(button_str:str) -> tuple[int, int]:
	# split on comma
	button_vals:list = button_str.split(",")
	# get what's after the + in each
	button_vals:list = [int(x[x.index("+"):]) for x in button_vals]
	# add to tuple   
	return (button_vals[0], button_vals[1])

def target_str_to_tuple(target_str:str) -> tuple[int, int]:
	PART_TWO_NUM = 10000000000000
	# PART_TWO_NUM = 0
    # split on comma
	target_vals:list = target_str.split(",")
	# get what's after the + in each
	target_vals:list = [int(x[x.index("=")+1:]) for x in target_vals]
	# add to tuple   
	return (target_vals[0] + PART_TWO_NUM, target_vals[1] + PART_TWO_NUM)

def input_to_machines(lines:list[str]):
	machines = []
	for i in range((len(lines)//4)+1):
		machines.append((button_str_to_tuple(lines[4*i]), button_str_to_tuple(lines[4*i+1]), target_str_to_tuple(lines[4*i+2])))
	return machines

def check_if_possible(a,b,t):
	# Compute the gcd of A and B
    d = gcd(a, b)
    # Check if d divides C
    return (t % d == 0)

def handle_machine(machine):
	(ax, ay), (bx,by), (Tx, Ty) = machine

	if check_if_possible(ax, bx, Tx) and check_if_possible(ay, by, Ty):
		# do the logic
		# max iterations of b such that total x and y are under target
		# min of the max of x and y
		# max_b = min((Tx//bx), (Ty//by))
		# for Cb in range(max_b, 0, -1):
		# 	remaining_x = Tx - (Cb*bx)
		# 	remaining_y = Ty - (Cb*by)
		# 	if remaining_x > ax and remaining_y > ay and remaining_x % ax == 0 and remaining_y % ay == 0 and remaining_x/ax == remaining_y/ay:
		# 		return (remaining_x//ax, Cb)

		Cb, Rb = divmod((ax*Ty - ay*Tx), (ax*by - bx*ay))
		if Rb == 0:
			Ca, Ra = divmod((Tx*by - bx*Ty), (ax*by - bx*ay))
			if Ra == 0:
				return (Ca,Cb)

	return None

def result_to_tokens(result):
	return 3*result[0] + result[1]
	
if __name__ == "__main__":
	input = get_input()
	machines = input_to_machines(input)
	# what do we want one machine's info to look like
	# ((ax,ay), (bx,by), (target_x, target_y))

	total_tokens = 0
	# for machine in machines:
	for machine in machines:
		result = handle_machine(machine)
		if result is not None:
			total_tokens += result_to_tokens(result)
	print(total_tokens)