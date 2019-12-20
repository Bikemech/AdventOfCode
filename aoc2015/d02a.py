import re
sides = re.compile(r'(\d+)x(\d+)x(\d+)')

def parse(dim):
	x, y, z = sides.match(dim).groups()
	return sorted([int(x), int(y), int(z)])

def paper(dim):
	x, y, z = parse(dim)
	return 2 * (x*y + x*z + y*z) + x * y

area = 0
for i in open("d02", "r").readlines():
	area += paper(i)

print(area)