floor = 0
for i, f in enumerate(open("d01", "r").read()):
	floor -= 2 * ord(f) - 81
	if floor == -1:
		break
print(i + 1)