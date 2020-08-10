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

def mutate(string, inst):
    if inst[0] == "s":
        string.sX(int(inst[1:]))

    if inst[0] == "x":
        nums = inst[1:].split("/")
        string.xAB(int(nums[0]), int(nums[1]))

    if inst[0] == "p":
        names = inst[1:].split("/")
        string.pAB(names[0], names[1])


t = perm()

instructions = [inst for inst in open("d16.input", "r").read().split(",")]
states = [t.__repr__()]
count = 0

while True:
    for inst in instructions:
        mutate(t, inst)

    count += 1
    string = t.__repr__()
    if string in states:
        index = states.index(string)
        break
    states.append(string)


rest = (10**9 - index) % count
for _ in range(rest):
    for inst in instructions:
        mutate(t, inst)

print(t)