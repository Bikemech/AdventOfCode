from math import sqrt

def triangle(x):
	return (x**2 + x) // 2

def steps(target):
	side = int(sqrt(target - 1)) + 2
	side -= 1 - (side %2)
	corner_distance = side - 1

	rest = side**2 - target
	rest = rest % (side - 1)

	print(corner_distance)


target = 368078
target = 76