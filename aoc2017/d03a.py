from math import sqrt

target = 368078

def find_pos(target):
	a = int(sqrt(target))
	b = target - a**2

	if a % 2 == 0:
		y = a//2
		x = (-a//2 + 1)
	else:
		y = (-a//2 + 1)
		x = a//2


	if x <= 0: # integer root is even
		if b > 0:
			b -= 1
			x -= 1

		if b > 1 * a:
			b -= 1 * a
			y -= 1 * a
		else:
			y -= b
			b = 0

		x += b

	else:
		if b > 0: # interger root is odd
			b -= 1
			x += 1

		if b > 1 * a:
			b -= 1 * a
			y += 1 * a
		else:
			y += 1
			b = 0

		x -= b
	return x, y

for i in range(1, 10):
	print(find_pos(i**2), i**2)
