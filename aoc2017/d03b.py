target = 368078

class pt_set:
    def __init__(self):
        self.pts = {(0, 0):1} # at origo
        self.head = [0, 0]
        self.growth = 1 # amount of steps before direction is changed
        self.local_step = 0
        self.dir = 0 # 0=+x, 1=+y, 2=-x, 3=-y

        self.val = 1

    def getNeighborValues(self):
        val = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i or j):
                    test_head = (self.head[0] + i, self.head[1] + j)

                    if test_head in self.pts:
                        val += self.pts[test_head]
        return val


    def step(self):


        if self.local_step == self.growth:
            self.dir += 1
            self.local_step = 0

            if self.dir % 2 == 0:
                self.growth += 1

        if self.dir % 4 == 0:
            self.head[0] += 1

        if self.dir % 4 == 1:
            self.head[1] += 1

        if self.dir % 4 == 2:
            self.head[0] -= 1

        if self.dir % 4 == 3:
            self.head[1] -= 1

        self.local_step += 1

        self.val = self.getNeighborValues()
        self.pts[tuple(self.head)] = self.val


t = pt_set()

while t.val < target:
    t.step()

print("\n\n")

print(t.val)

