"""   BROKEN    """

class node:
	def __init__(self, name):
		self.name = name
		self.connections = dict()
		self.weight = 2**32
		self.unvisited = True

	def __gt__(self, other):
		return self.weight > other.weight

	def __repr__(self):
		string = "### %s ###\n"%self.name
		for i in self.connections:
			string += "%s: %d\n"%(i.name, self.connections[i])

		return string

	def connect(self, other, dist):
		self.connections[other] = dist
		other.connections[self] = dist

	def drop(self, item):
		if item in self.connections:
			item.unvisited = False

	def restore(self):
		self.weight = 2**32
		self.unvisited = True

	def relax(self):
		for i in self.connections:
			if i.unvisited:
				if i.weight > self.weight + self.connections[i]:
					i.weight = self.weight + self.connections[i]
					i.unvisisted = False


nodes = dict()

for i in open("d09", "r").readlines():
	town = i.split()
	if town[0] not in nodes:
		nodes[town[0]] = node(town[0])

	if town[2] not in nodes:
		nodes[town[2]] = node(town[2])

	nodes[town[0]].connect(nodes[town[2]], int(town[-1]))


times = []

for name in nodes:

	nodes[name].weight = 0
	Que = []
	for i in nodes:
		Que.append(nodes[i])
	while Que:
		Que = sorted(Que)
		for i in Que[1:]:
			i.weight = 2**32

		ptr = Que.pop(0)
		ptr.relax()

		for i in nodes:
			nodes[i].drop(nodes[ptr.name])

print(ptr.weight)
