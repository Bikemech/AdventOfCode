from knothash import KnotHash

data = [int(i) for i in open("d10.input", "r").read().split(",")]

t = KnotHash()
for i in data:
    t.knot(i)

print(t[0] * t[1])