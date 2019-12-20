visited = set()
santa = [0, 0]
robos = [0, 0]

p = 1

for i in open("d03", "r").read():
	p = p^1

	visited.add((santa[0], santa[1]))
	visited.add((robos[0], robos[1]))

	if i == "^":
		if p:
			santa[1] += 1
		else:
			robos[1] += 1

	if i == "v":
		if p:
			santa[1] -= 1
		else:
			robos[1] -= 1

	if i == ">":
		if p:
			santa[0] += 1
		else:
			robos[0] += 1

	if i == "<":
		if p:
			santa[0] -= 1
		else:
			robos[0] -= 1

visited.add((santa[0], santa[1]))
visited.add((robos[0], robos[0]))
print(len(visited))