def read_instruction(head, inst):
	if inst.startswith('L'):
		head *= (0 + 1j)
	else:
		head *= (0 - 1j)

	return head, head * int(inst[1:])

instructions = [i for i in open("d01.puz", "r").read().split(', ')]

head = 1 + 0j
position = 0 + 0j

for inst in instructions:
	head, walks = read_instruction(head, inst)
	position += walks

print(abs(position.real) + abs(position.imag))