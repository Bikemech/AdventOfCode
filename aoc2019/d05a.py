# param 	A B C D E	DE	: opcode
#			| | | | |	C	: param mode
#			0 1 0 0 2	A	: param mode

def opcode(arg):
	code = arg % 100
	p2 = (arg//100) % 2
	p1 = (arg//1000) % 2
	p = 0

	if code == 1 or code == 2:
		p = 2
	if code == 3 or code == 4:
		p = 1

	return code, p2, p1, p

def run(data, input):
	ptr = 0
	op = opcode(data[ptr])
	

for i in [1002, 1101, 103, 4, 99999]:
	print(opcode(i))
	
