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

def pt_on_line(p, line):
    x0, x1 = sorted([line[0], line[2]])
    y0, y1 = sorted([line[1], line[3]])
    if p[0] not in range(x0, x1 + 1) or p[1] not in range(y0, y1 + 1):
        return False

    if line[1] == line[3]: # horizontal
        return abs(p[0] - line[0])
    else:
        return abs(p[1] - line[1])

def get_lenght(line):
    if line[0] == line[2]:
        return abs(line[1] - line[3])
    else:
        return abs(line[0] - line[2])


path1, path2 = [[i for i in j.split(",")] for j in open("scrap", "r").readlines()]
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

intersections = dict()
dists = []

distance = 0
for i in trail1:
    for j in trail2:
        a = intersect(i, j)
        if a:
            intersections[a] = (distance + pt_on_line(a, i), None)
    distance += get_lenght(i)


t = []

distance = 0
for i in trail2:
    d = 0
    for j in trail1:
        a = intersect(i, j)
        if a:
            intersections[a] = (intersections[a][0], distance + pt_on_line(a, i))
        d += get_lenght(j)
    distance += get_lenght(i)


for i in intersections:
    print(i, sum(intersections[i]))

dist = [sum(intersections[i]) for i in intersections]
print(sorted(dist))