from knothash import KnotHash

class kh(KnotHash):
    def binary(self):
        string = ""
        for i in self.dense_hash():
            string += bin(int(i, 16))[2:].zfill(4)
        return string

#puzzle_input = "ljoxqyyw"
puzzle_input = "flqrgnkx"


strings = []

test = [ord(i) for i in puzzle_input.upper()]
test.append(ord("-"))

for i in range(8):
    knot = kh()
    test[-1] = i
    knot.auto_knot(test)
    strings.append(knot.binary())



string = ""
for i in range(8):
    for j in range(8):
        if strings[i][j] == "1":
            string += "#"
        else:
            string += "."
    string += "\n"

print(string)