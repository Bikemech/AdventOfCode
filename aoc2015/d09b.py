from itertools import permutations as perm

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

def calc_path(pm_nodes):
	total = 0
	ptr = pm_nodes[0]
	for i in pm_nodes[1:]:
		total += ptr.connections[i]
		ptr = i

	return total

nodes = dict()

for i in open("d09", "r").readlines():
	town = i.split()
	if town[0] not in nodes:
		nodes[town[0]] = node(town[0])

	if town[2] not in nodes:
		nodes[town[2]] = node(town[2])

	nodes[town[0]].connect(nodes[town[2]], int(town[-1]))

towns = [nodes[i] for i in nodes]

times = []
for i in perm(towns):
	times.append(calc_path(i))


print(sorted(times)[-1])