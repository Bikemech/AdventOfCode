class node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
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

print(nodes[data[100][0]].findRoot())