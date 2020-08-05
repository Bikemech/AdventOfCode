from math import sqrt, ceil

def steps(n):
	if n == 1:
		return 0

	outer = ceil(sqrt(n))
	if not outer % 2:
		outer += 1

	minstep = outer // 2
	maxstep = outer - 1

	rest = n - (outer - 2)**2
	count = rest // (outer - 1)
	local_rest = rest - count * (outer - 1)
	if local_rest > (outer - 1)//2:
		return maxstep - (outer - 1 - local_rest)
	return maxstep - (local_rest)


target = 368078

print(steps(target))