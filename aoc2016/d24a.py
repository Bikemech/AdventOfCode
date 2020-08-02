import os
from hashlib import md5


class maze:
	def __init__(self, string):
		self.obstacles = set()
		self.nodes = dict()

		rows = string.split("\n")
		for j, y in enumerate(rows):
			for i, x in enumerate(y):
				if x == "#":
					self.obstacles.add((i, j))
				elif x.isdigit():
					self.nodes.update({int(x):(i, j)})


class crawler:
	def __init__(self, id, maze):
		self.id = id
		self.maze = maze
		self.targets = dict()
		self.home = self.maze.nodes[self.id]

	def crawl(self):
		index = 1
		path = {self.home:0}
		que = {self.home}
		obs = self.maze.obstacles
		target_keys = {self.maze.nodes[k]: k for k in self.maze.nodes}

		next_que = set()


		while que:
			for q in que:

				for i in range(-1, 2):
					for j in range(-1, 2):

						if (i and not j) or (j and not i):
							new_pt = (q[0] + i, q[1] + j)
							if not new_pt in (obs | set(path.keys())):
								next_que.add(new_pt)
								path[new_pt] = index

							
			index += 1
			que = next_que
			next_que = set()

		for tar in target_keys:
			self.targets[target_keys[tar]] = path[tar]

		# for i in range(10):
		# 	for j in range(10):
		# 		if (j, i) in target_keys:
		# 			print("(%d)"%target_keys[(j, i)], end = "")
		# 		elif (j, i) in path:
		# 			print(" %d "%path[(j, i)], end = "")
		# 		else:
		# 			print("   ", end = "")

		# 	print()


		del self.targets[self.id]


class node:
	def __init__(self, id):
		self.id = id
		self.connections = dict()
		self.weight = float("inf")
		self.check = False

	def __lt__(self, other):
		return self.weight < other.weight

	def connect(self, other, weight):
		self.connections[other] = weight

	def relax(self):
		self.check = True
		for other, weight in self.connections.items():
			if not other.check:
				if self.weight + weight < other.weight:
					other.weight = self.weight + weight

	def relaxMin(self):
		self.check = True
		mw = float("inf")
		ptr = None

		for p in self.connections:
			if self.connections[p] < mw:
				ptr = p
				mw = self.connections[p]

		ptr.weight = self.weight + mw
		print(ptr)

	def init(self):
		self.weight = 0
			
	def __repr__(self):
		return str(self.id) + ":\t" + str(self.weight)


def fetchByID(x, nodes):
	for i in nodes:
		if i.id == int(x):
			return i



string = open("d24.input", "r").read()

string = '''
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
'''

mazeHash = md5()
mazeHash.update(string.encode())

rewrite = not os.path.isfile("nodes.txt")

if (os.path.isfile("nodes.txt")):
	old_hash = open("nodes.txt", "r").readline().strip()
	if old_hash != mazeHash.hexdigest():
		rewrite = True

if rewrite:
	m = maze(string)

	crawlers = []

	for i in m.nodes:
		crawlers.append(crawler(i, m))
		crawlers[-1].crawl()
		print("Crawler %d finished crawling!"%i)


	with open("nodes.txt", "w") as f:
		f.write(mazeHash.hexdigest())
		f.write("\n")
		for c in crawlers:
			f.write("%d\n%s\n"%(c.id, str(c.targets)[1:-1]))


with open("nodes.txt", "r") as f:
	f.readline()
	data = [i.strip() for i in f.readlines()]

nodes = []
for i in range(0, len(data), 2):
	nodes.append(node(int(data[i])))


for i in range(0, len(data), 2):
	ptr = fetchByID(data[i], nodes)
	connections = data[i + 1].split(",")

	for link in connections:
		target, weight = link.split(":")
		ptr.connect(fetchByID(target, nodes), int(weight))


for n in nodes:
	print(n, n.connections)

fetchByID(0, nodes).init()
fetchByID(0, nodes).relaxMin()
print()

for n in nodes:
	print(n, n.connections)