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

def check_for_z_gate(gates:list[tuple[str,str,str,str]]):
	remaining_targets = {x[3][0] for x in gates}
	
	return "z" in remaining_targets

def process_gate(val1, operator, val2):
	match operator:
		case "AND":
			return val1 & val2
		case "OR":
			return val1 | val2
		case "XOR":
			return val1 ^ val2
		case _:
			print("pooped the bed")
			return 

	
def p1(wires:dict, gates):
	# while gates contains a gate with a target value starting with z
	while check_for_z_gate(gates):
		# for gate in gates:
		for gate in gates:
			in1, operator, in2, target = gate
			# if this gate can be handled by known wires
			if in1 in wires.keys() and in2 in wires.keys():
				# handle
				# add result to wires
				wires[target] =  process_gate(wires[in1], operator, wires[in2])

				# remove from gates
				gates.pop(gates.index(gate))
	return wires

def parse_output_wires(wires):
	z_wires = sorted({key:val for key, val in wires.items() if key[0] == "z"}.items())
	print(z_wires)
	binary_str = ""
	for wire in z_wires:
		binary_str+=str(wire[1])
	print(binary_str)
	return int(binary_str[::-1], 2)

if __name__ == "__main__":
	raw_input = get_raw_input()
	wires, gates = raw_input_to_input(raw_input) 
	wires = p1(wires, gates)
	print(parse_output_wires(wires))
