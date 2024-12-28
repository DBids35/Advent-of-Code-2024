def get_input() -> list[str]:
	with open("d17.txt", "r") as file:
		return [x for x in file.read().splitlines()]
	
def input_to_registers_and_program(input:list[str]):
	registers = {}
	for letter, row in zip(['A','B','C'], input[:3]):
		registers[letter] = int(row[row.index(": ")+2:])

	# 
	program_str:str = input[-1]
	program:list[int] = [int(x) for x in program_str[program_str.index(":") + 2:].split(",")]
	program_tuple:list[tuple[int,int]] = [(program[i], program[i+1]) for i in range(0, len(program) - 1, 2)]
	return registers, program

def combo(operand, registers) -> int:
	if operand < 4:
		return operand
	if operand == 4: 
		return registers["A"]
	if operand == 5:
		return registers["B"]
	if operand == 6:
		return registers["C"]
	print("Uhoh")
	return 0

def main():
	input = get_input()
	registers, program = input_to_registers_and_program(input)
	for i in range(200000000, 999999999999):
		# print(i)
		registers["A"] = i
		output = []
		i=0
		while i < len(program)-1:
			instruction = program[i]
			operand = program[i+1]
			# print(instruction, operand)
			# print(registers["A"], registers["B"], registers["C"])

			if instruction == 0: 
				registers["A"] = registers["A"]//(2**combo(operand, registers))

			elif instruction == 1:
				registers["B"] = registers["B"]^operand

			elif instruction == 2:
				registers["B"] = combo(operand, registers)%8

			elif instruction == 3:
				if registers["A"] != 0:
					i = operand
					continue

			elif instruction == 4:
				registers["B"] = registers["B"] ^ registers["C"]

			elif instruction == 5:
				output.append(str(combo(operand, registers)%8))
				if output != program[:len(output)]:
					break

			elif instruction == 6:
				registers["B"] = registers["A"]//2**combo(operand, registers)

			elif instruction == 7:
				registers["C"] = registers["A"]//2**combo(operand, registers)

			i += 2
		if output == program:
			print(i)
			return i

if __name__ == "__main__":
	print(main())
