data = "cqjxjnds"
pw = [ord(i) - 97 for i in data]

def inc(pw):
	ptr = len(pw) - 1
	pw[ptr] += 1

	while pw[ptr] > 25:
		pw[ptr] = 0
		ptr -= 1
		pw[ptr] += 1

		if ptr < 0:
			break
	return pw

def check(pw):
	c = 1
	straight = False
	duba = None
	dubb = None

	for i, ptr in enumerate(pw):

		if ptr + 97 in [ord("i"), ord("o"), ord("l")]:
			return False

		if i > 0:
			if ptr == pw[i - 1] + 1:
				c += 1
			else:
				c = 1

			if ptr == pw[i - 1]:
				if duba is not None:
					dubb = ptr
				else:
					duba = ptr
		if c == 3:
			straight = True

	if duba is not None and dubb is not None and duba != dubb:
		return straight
	return False

while True:
	if check(pw):
		break
	inc(pw)

string = ""
for i in pw:
	string += chr(i + 97)

print(string)