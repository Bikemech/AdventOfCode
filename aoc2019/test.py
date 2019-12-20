import re

home = re.compile(r'COM\)([0-9A-Z]{1,3})')
data = open("scrap", "r").readlines()
data = open("d06", "r").readlines()

class node:
	def __init__(ELF, id):
		ELF.id = id
		ELF.spy = re.compile(r'%s\)([0-9A-Z]{1,3})'%ELF.id)
		ELF.branch = []
		ELF.parent = None
		ELF.d = -1
		ELF.path = None


	def __repr__(ELF):
		return ELF.id

	def find_all(ELF, data):
		ELF.find_child(data)
		for kid in ELF.branch:
			kid.find_all(data)

	def find_child(ELF, data):
		used_indicies = []	# This list stores indicies that
							# match.

		for i, name in enumerate(data):
			if ELF.spy.match(name):
				new = node(ELF.spy.match(name).group(1))
				new.parent = ELF
				new.d = ELF.d + 1
				ELF.branch.append(new)
				used_indicies.append(i)

		for i in used_indicies[::-1]:	# Deleting these stripped
			del data[i]			# about 40% of the time it
								# takes to construct a big tree.

	def count(ELF):
		c = 1
		for i in ELF.branch:
			c += i.count()

		return c

	def sum_depth(ELF):
		s = ELF.d
		for i in ELF.branch:
			s += i.sum_depth()
		return s

	def search_node(ELF, id):
		if ELF.id == id:
			return ELF
		else:
			for i in ELF.branch:
				node = i.search_node(id)
				if node:
					return node

	def trace_path(ELF, id1, id2):
		A = ELF.search_node(id1)
		B = ELF.search_node(id2)

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