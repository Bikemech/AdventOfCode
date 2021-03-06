from knothash import KnotHash

class kh(KnotHash):
    def __init__(self, data):
        super().__init__()

        self.auto_knot(data + [17, 31, 73, 47, 23])


    def binary(self):
        string = ""
        for i in self.dense_hash():
            string += bin(int(i, 16))[2:].zfill(4)
        return string

puzzle_input = "ljoxqyyw-"


data = [ord(i) for i in puzzle_input]

t = kh(data)
h = t.dense_hash()

strings = []

for i in range(128):
    puz = puzzle_input + "%d"%i
    data = [ord(i) for i in puz]

    strings.append(kh(data).binary())

count = 0
for i in strings:
    for j in i:
        if j == "1":
            count += 1

print(count)