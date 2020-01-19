import re

rgnum = re.compile(r'(\d+)')

def getobjs(string, ptr = 0):
	stack = 0
	start = string[ptr:].find('{') + ptr
	ptr = start

	while ptr < len(string):
		if string[ptr] == '{':
			stack += 1

		if string[ptr] == '}':
			stack -= 1

		if stack == 0:
			return start, ptr + 1

		ptr += 1
	return (-1, -1)

def remove_sub(string):
	start = string[1:].find('{')
	if start < 0:
		return string

	end = len(string) - string[:-1][::-1].find('}')
	return string[:start] + "-||-" + string[end:]



source = open("d12.puz", "r").read()

objs = []

a = 0
score = 0

while '{' in source[a + 1:]:
	a, b = getobjs(source, a + 1)
	string = remove_sub(source[a:b])
	if "red" in string:
		a = b
	else:
		score += sum([int(i) for i in rgnum.findall(string)])
		print(string)

print(score)