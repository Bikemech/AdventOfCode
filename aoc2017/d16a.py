from collections import deque

class perm(deque):
    def __init__(self):
        super().__init__()
        for i in range(16):
            self.append(chr(i + 97))

    def __repr__(self):
        string = ""
        for i in self:
            string += i
        return string

    def sX(self, x):
        que = deque()
        for i in range(x):
            que.append(self.pop())
        self.extendleft(que)

    def xAB(self, A, B):
        self[A], self[B] = self[B], self[A]

    def pAB(self, A, B):
        indexA = self.index(A)
        indexB = self.index(B)

        self.xAB(indexA, indexB)

t = perm()

for inst in open("d16.input", "r").read().split(","):
    if inst[0] == "s":
        t.sX(int(inst[1:]))

    if inst[0] == "x":
        nums = inst[1:].split("/")
        t.xAB(int(nums[0]), int(nums[1]))

    if inst[0] == "p":
        names = inst[1:].split("/")
        t.pAB(names[0], names[1])

print(t)