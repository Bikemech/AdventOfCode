from collections import deque

class KnotHash:
    def __init__(self):
        self.string = deque([i for i in range(256)])
        self.skip = 0
        self.total_shift = 0

    def __lshift__(self, other):
        for i in range(other):
            self.string.append(self.string.popleft())

        self.total_shift += 1

    def __rshift__(self, other):
        for i in range(other):
            self.string.appendleft(self.string.pop())

        self.total_shift -= 1

    def reverse(self, index):
        snippet = deque()
        for i in range(index):
            snippet.append(self.string.popleft())

        self.string.extendleft(snippet)

    def hash_sequence(self, sequence):
        for i, j in enumerate(sequence):
            self.reverse(j)
            self << (j + self.skip)
            self.skip += 1

    def origo(self):
        self << self.total_shift

data = [int(i) for i in open("d10.input").read().split(",")]

p = KnotHash()

p.hash_sequence(data)
print(p.string[p.total_shift] *  p.string[p.total_shift + 1])
p.origo()
print(p.string[0] * p.string[1])
print(p.total_shift)
