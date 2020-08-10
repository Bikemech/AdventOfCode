from knothash import KnotHash

data = [ord(i) for i in open("d10.input", "r").read()]
suffix = [17, 31, 73, 47, 23]
data += suffix

t = KnotHash()

t.auto_knot(data)

print(t.dense_hash())