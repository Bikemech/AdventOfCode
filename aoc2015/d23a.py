registers = {'a':0, 'b':0}
ptr = 0

instructions = [tuple(i.split()) for i in open("d23.puz", "r").readlines()]


while ptr >= 0 and ptr < len(instructions):
	inst = instructions[ptr][0]

	if inst == "hlf":
		tar = instructions[ptr][1][0]
		registers[tar] = registers[tar] // 2

	if inst == "tpl":
		tar = instructions[ptr][1][0]
		registers[tar] = registers[tar] * 3

	if inst == "inc":
		tar = instructions[ptr][1][0]
		registers[tar] += 1

	if inst == "jie":
		tar = instructions[ptr][1][0]
		if registers[tar] % 2 == 0:
			ptr += int(instructions[ptr][2]) - 1
		
	if inst == "jio":
		tar = instructions[ptr][1][0]
		if registers[tar] == 1:
			ptr += int(instructions[ptr][2]) - 1

	if inst == "jmp":
		ptr += int(instructions[ptr][1]) - 1

	ptr += 1

print(registers)