class KnotHash(list):
    def __init__(self, it):
        for i in range(it):
            self.append(i)

        self.index = 0
        self.skip = 0

    def __knot__(self, i, j):
        k = len(self)

        while i < j:
            self[i % k], self[j % k] = self[j % k], self[i % k]
            i += 1
            j -= 1

    def knot(self, step):
        i = self.index
        j = i + step

        self.__knot__(i, j - 1)
        self.index += step + self.skip
        self.skip += 1


data = [int(i) for i in open("d10.input", "r").read().split(",")]

t = KnotHash(256)
for i in data:
    t.knot(i)

print(t[0] * t[1])