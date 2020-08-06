class HexagonalPosition:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def move(self, direction):
        if direction == "n":
            self.x -= 1
            self.y += 1

        if direction == "ne":
            self.x -= 1
            self.z += 1

        if direction == "nw":
            self.y += 1
            self.z -= 1

        if direction == "s":
            self.x += 1
            self.y -= 1

        if direction == "se":
            self.y -= 1
            self.z += 1

        if direction == "sw":
            self.x += 1
            self.z -= 1

    def __sub__(self, other):
        assert(type(other) == type(self))
        return (abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z))//2

hp = HexagonalPosition()
dummy = HexagonalPosition()

for m in open("d11.input", "r").read().split(","):
    hp.move(m)

print(hp - dummy)