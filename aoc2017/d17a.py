from time import time
from matrixmemory import *

class circ_buff:
    def __init__(self, step):
        self.pos = 0
        self.step = step
        self.buff = MatrixMemory(2017)
        self.buff.head = 1
        self.index = 1

    def spin(self, count = 1):
        for _ in range(count):
            self.pos = (self.pos + self.step) % len(self.buff)
            self.buff.insert(self.pos + 1, self.index)
            self.pos += 1
            self.index += 1

    def __repr__(self):
        return self.buff.__repr__()




# 359 is the puzzle input
spinner = circ_buff(359)
print("setup finished")

start = time()

# for i in range(5*10**7):
for i in range(2017):
    if i % 10**5 == 0:
        print(i, time() - start)
    spinner.spin()

print("\n", time() - start)

print("\n\n\n")
i = spinner.buff.index(2017) + 1
print(spinner.buff[i])

print(spinner.buff)