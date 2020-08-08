gates = [(int(line.split(":")[0]), int(line.split(":")[1])) \
         for line in open("d13.input", "r").readlines()]

delay = 3943250
flag = True

while flag:
    delay += 1
    for i, j in gates:
        if (delay + i) % (2 * (j - 1)) == 0:
            break
    else:
        break

print(delay)

'''
3943253
5384693
6826133
8267573
9709013
11150453
12591893
'''

print(5384693 - 3943253)
print(8267573 - 6826133)