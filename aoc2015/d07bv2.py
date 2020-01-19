import re

rxtoken = re.compile(r'(NOT|OR|AND|RSHIFT|LSHIFT)')
rxname = re.compile(r'([a-z0-9]+)')

def parse(line):
	prime = rxname.findall(line)[0]

	if rxtoken.findall(line):
		token = rxtoken.findall(line)[0]
	else:
		token = None

	if token is None or token == 'NOT':
		return (token, prime, None)

	second = rxname.findall(line)[1]

	return (token, prime, second)

def NOT(x):
	return ~x % (1 << 16)

def AND(x, y):
	return (x & y) % (1 << 16)

def OR(x, y):
	return (x | y) % (1 << 16)

def LSHIFT(x, y):
	return (x << y) % (1 << 16)

def RSHIFT(x, y):
	return (x >> y) % (1 << 16)

def examine(cc, p):
	token = cc[0]
	prm = cc[1]
	sec = cc[2]

	if prm in evaluated:
		prm = str(evaluated[prm])

	if prm.isdigit():
		if token is None:
			evaluated[p] = prm
			data[p] = (token, prm, sec)
			return

		if token == "NOT":
			evaluated[p] = NOT(int(prm))
			data[p] = (token, prm, sec)
			return

	if token == "NOT" or token is None:
		return

	if sec in evaluated:
		sec = str(evaluated[sec])

	if sec.isdigit() and prm.isdigit():
		if token == "AND":
			evaluated[p] = AND(int(prm), int(sec))

		if token == "OR":
			evaluated[p] = OR(int(prm), int(sec))

		if token == "LSHIFT":
			evaluated[p] = LSHIFT(int(prm), int(sec))

		if token == "RSHIFT":
			evaluated[p] = RSHIFT(int(prm), int(sec))

	data[p] = (token, prm, sec)


data = dict()
for n in open("d07.puz", "r").readlines():
	data[n.split()[-1]] = parse(n)

evaluated = dict()

while len(evaluated) != len(data):
	for i in data:
		examine(data[i], i)



data = dict()
for n in open("d07.puz", "r").readlines():
	data[n.split()[-1]] = parse(n)

data['b'] = (None, str(evaluated['a']), None)
evaluated = dict()

while len(evaluated) != len(data):
	for i in data:
		examine(data[i], i)

print(evaluated['a'])