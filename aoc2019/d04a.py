target = "134792-675810"
A, B = [int(i) for i in target.split("-")]

def check(x):
	flag = 0
	for i, num in enumerate(x):
		if i > 0:
			if num < x[i - 1]:
				return 0
			if x[i - 1] == num:
				flag = 1
	return flag

def tolist(x):
	return [int(i) for i in str(x)]

c = 0

for i in range(A, B + 1):
	c += check(tolist(i))

print(c)