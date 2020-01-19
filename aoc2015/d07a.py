'''		BROKEN		'''

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


def eval(x):
	print(x)
	sleep(.2)

	token = x[0]

	if x[1].isdigit():
		primexp = int(x[1])

	else:
		primexp = eval(data[x[1]])

	if token is None:
		return primexp

	if token == 'NOT':
		return NOT(primexp)

	if x[2].isdigit():
		secondexp = int(x[2])

	else:
		secondexp = eval(data[x[2]])

	if token == "OR":
		return OR(primexp, secondexp)

	if token == "AND":
		return AND(primexp, secondexp)

	if token == "LSHIFT":
		return LSHIFT(primexp, secondexp)

	if token == "RSHIFT":
		return RSHIFT(primexp, secondexp)

data = dict()
for line in open("d07.puz", "r").readlines():
	data[line.split()[-1]] = parse(line)

print(eval(data['a']))