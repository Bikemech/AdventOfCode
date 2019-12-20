import re
sides = re.compile(r'(\d+)x(\d+)x(\d+)')

def parse(dim):
	x, y, z = sides.match(dim).groups()
	return sorted([int(x), int(y), int(z)])

def bow(dim):
	x, y, z = parse(dim)
	return 2 * (x + y) + x * y * z

ribbon = 0
for i in open("d02", "r").readlines():
	ribbon += bow(i)

print(ribbon)