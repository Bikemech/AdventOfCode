from collections import Counter

class node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.subweight = 0
        self.parent = None
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        child.parent = self

    def setParent(self, parent):
        self.parent = parent

    def findRoot(self):
        if self.parent is None:
            return self
        return self.parent.findRoot()

    def sumSubBranches(self):
        total = self.weight
        for c in self.children:
            total += c.sumSubBranches()

        self.subweight = total
        return total

    def oddOneOut(self):
        count = Counter([c.subweight for c in self.children])

        if len(count) == 1:
            return self

        for w, c in count.items():
            if c == 1:
                break

        for ptr in self.children:
            if ptr.subweight == w:
                ptr.unbalanced = True
                return ptr.oddOneOut()

    def getSiblings(self):
        if self.parent is None:
            return []

        siblings = []
        for c in self.parent.children:
            if c is not self:
                siblings.append(c)

        return siblings



    def __repr__(self):
        string = self.id + "(%d) "%self.weight
        if self.parent:
            string += " {%s} "%self.parent.id
        if self.children:
            string += "->"
            for c in self.children:
                string += " %s,"%c.id

        return string[:-1]


def clean(line):
    lines = line.split()
    new = []
    for string in line.split():
        new.append(string.strip(",.()\n"))

    return new


data = [clean(line) for line in open("d07.input", "r").readlines()]
nodes = {line[0] : node(line[0], int(line[1])) for line in data}

for string in data:
    for c in string[3:]:
        nodes[string[0]].addChild(nodes[c])

root = nodes[data[0][0]].findRoot()
root.sumSubBranches()

unbal = root.oddOneOut()

diff = unbal.getSiblings()[0].subweight - unbal.subweight

print(unbal.weight + diff)

