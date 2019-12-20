import re


ton = re.compile(r'(turn on)')
toff = re.compile(r'(turn off)')
togg = re.compile(r'(toggle)')
coords = re.compile(r'(\d+)')

def process(string):
	cor = tuple([int(i) for i in coords.findall(string)])
	if ton.match(string):
		return turn_on(*cor)

	if toff.match(string):
		return turn_off(*cor)

	if togg.match(string):
		return toggle(*cor)


grid = [[0 for i in range(1000)] for j in range(1000)]

def turn_on(x1, y1, x2, y2):
	for i in range(x1, x2 + 1):
		for j in range(y1, y2 + 1):
			grid[i][j] += 1

def turn_off(x1, y1, x2, y2):
	for i in range(x1, x2 + 1):
		for j in range(y1, y2 + 1):
			if grid[i][j] > 0:
				grid[i][j] -= 1

def toggle(x1, y1, x2, y2):
	for i in range(x1, x2 + 1):
		for j in range(y1, y2 + 1):
			grid[i][j] += 2

def count(x):
	tot = 0
	for i in x:
		for j in i:
			tot += j

	return tot

for line in open("d06", "r").readlines():
	process(line)

print(count(grid))