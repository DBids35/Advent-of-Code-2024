def get_raw_input() -> list[str]:
	with open("d24.txt", "r") as file:
		return [x for x in file.read().splitlines()]
	
def process_gate_str(gate_str:str) -> tuple[str, str, str, str]:
	split = gate_str.split(" ")
	return (split[0], split[1], split[2], split[4])

def raw_input_to_input(raw_input:list[str]):
	split_index = raw_input.index("")
	wires = raw_input[:split_index]
	wires_dict = {x.split(":")[0]: int(x.split(":")[1]) for x in wires}
	gates = raw_input[split_index + 1:]
	gates = [process_gate_str(x) for x in gates]
	return wires_dict, gates
	
def p1(input):
	# create a dict of knowns filled with initial knowns
	pass

if __name__ == "__main__":
	raw_input = get_raw_input()
	wires, gates = raw_input_to_input(raw_input) 
	print(wires, gates)
	p1(input)
