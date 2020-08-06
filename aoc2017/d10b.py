class KnotHash(list):
    def __init__(self):
        for i in range(256):
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

    def dense_hash(self):
        string = ""
        for i in range(0, 256, 16):
            num = self[i]
            for j in range(1, 16):
                num = num ^ self[i + j]

            string += hex(num)[2:].zfill(2)

        return string


data = [ord(i) for i in open("d10.input", "r").read()]
suffix = [17, 31, 73, 47, 23]
data += suffix

t = KnotHash()

for k in range(64):
    for i in data:
        t.knot(i)

print(t.dense_hash())