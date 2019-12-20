visited = set()
santa = [0, 0]

for i in open("d03", "r").read():
	visited.add((santa[0], santa[1]))
	if i == "^":
		santa[1] += 1

	if i == "v":
		santa[1] -= 1

	if i == ">":
		santa[0] += 1

	if i == "<":
		santa[0] -= 1

visited.add((santa[0], santa[1]))
print(len(visited))