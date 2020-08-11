from tkinter import Canvas, Tk, ALL
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

def erase_zone(space, x, y):
    if space[x][y] == "0":
        return

    else:
        space[x][y] = "0"

    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i and not j) or (j and not i):
                if (x + i >= 0 and x + i < 128) and (y + j >= 0 and y + j < 128):
                    erase_zone(space, x + i, y + j)



puzzle_input = "ljoxqyyw-"

data = [ord(i) for i in puzzle_input]

t = kh(data)
h = t.dense_hash()

strings = []

for i in range(128):
    puz = puzzle_input + "%d"%i
    data = [ord(i) for i in puz]

    strings.append(list(kh(data).binary()))


root = Tk()
frame = Canvas(root, height = 512, width = 512, bg = "#000000")
frame.pack()

count = 0

for i, p in enumerate(strings):
    for j, q in enumerate(p):
        if q == "1":
            erase_zone(strings, i, j)
            count += 1

print(count)