from tkinter import Canvas, Tk

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

    strings.append(list(kh(data).binary()))

root = Tk()
frame = Canvas(root, height = 600, width = 600, bg = "#000000")
frame.pack()

for i, p in enumerate(strings):
    for j, q in enumerate(p):
        if q == "1":
            frame.create_rectangle(i * 4, j * 4, i * 4 + 3, j * 4 + 3, fill = "#ff0000", outline = "#ff0000")


frame.mainloop()
