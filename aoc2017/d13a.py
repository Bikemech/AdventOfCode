gates = {int(line.split(":")[0]):int(line.split(":")[1]) for line in open("d13.input", "r").readlines()}

count = 0
p = 0
for i in gates:
    if i % (2 * (gates[i] - 1)) == 0:
        count += i * gates[i]
        p += 1

print(count, p)