import re

home = re.compile(r'COM\)([0-9A-Z]{1,3})')
data = open("scrap", "r").readlines()
data = open("d06", "r").readlines()

class node:
	def __init__(self, id):
		self.id = id
		self.spy = re.compile(r'%s\)([0-9A-Z]{1,3})'%self.id)
		self.branch = []
		self.parent = None
		self.d = -1
		self.path = None


	def __repr__(self):
		return self.id

	def find_all(self, data):
		self.find_child(data)
		for kid in self.branch:
			kid.find_all(data)

	def find_child(self, data):
		used_indicies = []	# This list stores indicies that
							# match.

		for i, name in enumerate(data):
			if self.spy.match(name):
				new = node(self.spy.match(name).group(1))
				new.parent = self
				new.d = self.d + 1
				self.branch.append(new)
				used_indicies.append(i)

		for i in used_indicies[::-1]:	# Deleting these stripped
			del data[i]			# about 40% of the time it
								# takes to construct a big tree.

	def count(self):
		c = 1
		for i in self.branch:
			c += i.count()

		return c

	def sum_depth(self):
		s = self.d
		for i in self.branch:
			s += i.sum_depth()
		return s

	def search_node(self, id):
		if self.id == id:
			return self
		else:
			for i in self.branch:
				node = i.search_node(id)
				if node:
					return node

	def trace_path(self, id1, id2):
		A = self.search_node(id1)
		B = self.search_node(id2)

		if A is None or B is None:
			return None

		A = A.parent
		B = B.parent

		steps = 0
		while True:
			if A == B:
				return steps
			steps += 1
			if A.d >= B.d:
				A = A.parent
			elif B.d > A.d:
				B = B.parent


	
# first step: Find root "COM"

root = node("COM")
root.find_all(data)

print(root.trace_path("YOU", "SAN"))