from math import sqrt, ceil
from collections import deque

class MatrixMemory:
    def __init__(self, maxel):
        self.len = ceil(sqrt(maxel))

        self.matrix = [deque([int() for i in range(self.len)]) for j in range(self.len)]
        self.head = 0

    def __repr__(self):
        string = ""
        for i in self.matrix:
            string += i.__repr__()[6:-1]
            string += "\n"

        return string

    def __getitem__(self, item):
        assert(type(item) == type(int()))

        if item < self.head and item >= 0:
            return self.matrix[item//self.len][item % self.len]

        if item < 0:
            return self[self.head + item]

        else:
            return None

    def __len__(self):
        return self.head

    def __setitem__(self, key, value):
        print("tjo", key, value)


    def insert(self, index, val):
        if index > self.head:
            return

        x, y = index % self.len, index//self.len

        self.matrix[y].insert(x, val)
        self.__shift_check__()
        self.head += 1

    def index(self, key):
        for i, row in enumerate(self.matrix):
            if key in row:
                return self.len * i + row.index(key)

        return None

    def __shift_check__(self, index = 0):
        for i in range(index, self.len):
            if len(self.matrix[i]) > self.len:
                if i == self.len - 1:
                    self.matrix[i].pop()
                else:
                    self.matrix[i + 1].appendleft(self.matrix[i].pop())

        if self.head == self.len**2:
            self.head -= 1

