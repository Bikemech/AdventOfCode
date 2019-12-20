def move(head, isct):
    if isct[0] == "U":
        return (head[0], head[1] + int(isct[1:])), \
        (head[0], head[1], head[0], head[1] + int(isct[1:]))
    if isct[0] == "D":
        return (head[0], head[1] - int(isct[1:])), \
        (head[0], head[1], head[0], head[1] - int(isct[1:]))
    if isct[0] == "R":
        return (head[0] + int(isct[1:]), head[1]), \
        (head[0], head[1], head[0] + int(isct[1:]), head[1])
    if isct[0] == "L":
        return (head[0] - int(isct[1:]), head[1]), \
        (head[0], head[1], head[0] - int(isct[1:]), head[1])

def intersect(line1, line2):
    if line1[0] == line1[2]:
        if line2[0] == line2[2]:
            return None
        else:
            return intersect(line2, line1)

    # Line1 should now be horizontal

    X, Y = line2[0], line1[1]
    x0, x1 = sorted([line1[0], line1[2]])
    y0, y1 = sorted([line2[1], line2[3]])

    if X in range(x0, x1 + 1) and Y in range(y0, y1 + 1):
        return (X, Y)

    return None

def get_distance(x):
    return abs(x[0]) + abs(x[1])

path1, path2 = [[i for i in j.split(",")] for j in open("d03", "r").readlines()]

head = (0, 0)
trail1 = []
for i in path1:
    head, step = move(head, i)
    trail1.append(step)

head = (0, 0)
trail2 = []
for i in path2:
    head, step = move(head, i)
    trail2.append(step)

dist = []

for i in trail1[1:]:
    for j in trail2:
        a = intersect(i, j)
        if a:
            dist.append(get_distance(a))

print(min(dist))
print(len(dist))
