import re
NAME = re.compile(r'.*\s(\w{1,2})$')
EXPR = re.compile(r'(NOT|AND|OR|RSHIFT|LSHIFT)')

data = {NAME.match(i).group(1):i for i in open("d07", "r").readlines()}
data = {NAME.match(i).group(1):i for i in open("scrap", "r").readlines()}

# find wire 'a' and connect recursively backwards...


class node:
	def __init__(self, line):
		print(line)
		self.ID = NAME.match(line).group(1)
		self.a = None
		self.b = None
		self.val = None

		if EXPR.search(line):
			self.expr = EXPR.search(line).group(1)
		else:
			self.expr = None

		self.assemble(line)

	def view(self):
		if self.a:
			print(self.ID, self.a.ID)
			self.a.view()
		else:
			print(self.ID, self.a)

		if self.b:
			print(self.ID, self.b.ID)
			self.b.view()
		else:
			print(self.ID, self.b)


	def assemble(self, line):


		if self.expr is None:
			if line.split()[1].isdigit:
				a = line.split()[0]
			else:
				a = data[line.split()[0]].split()[0]

			self.a = makeWire(a)


		elif self.expr == "NOT":
			if line.split()[1].isdigit():
				a = line.split()[1]
			else:
				a = NAME.match(data[line.split()[1]]).group(1)
			self.a = makeWire(a)

		elif self.expr in ("AND", "OR", "RSHIFT", "LSHIFT"):
			if line.split()[0].isdigit():
				a = line.split()[0]
			else:
				a = NAME.match(data[line.split()[0]]).group(1)

			if line.split()[2].isdigit():
				b = line.split()[2]
			else:
				b = NAME.match(data[line.split()[2]]).group(1)

			self.a = makeWire(a)
			self.b = makeWire(b)

	def rshift(self, a, b):
		self.val = (a >> b) % (1 << 16)
		return self.val

	def lshift(self, a, b):
		self.val = (a << b) % (1 << 16)
		return self.val

	def lnot(self, a):
		self.val = ~a % (1 << 16)
		return self.val

	def land(self, a, b):
		self.val = (a & b) % (1 << 16)
		return self.val

	def lor(self, a, b):
		self.val = (a | b) % (1 << 16)
		return self.val

	def eval(self):
		print(self.ID)
		if self.expr is None:
			self.val = self.a.eval()
			return self.val

		if self.expr == "NOT":
			self.val = self.lnot(self.a.eval())
			return self.val

		if self.expr == "AND":
			self.val = self.land(self.a.eval(), self.b.eval())
			return self.val

		if self.expr == "OR":
			self.val = self.lor(self.a.eval(), self.b.eval())
			return self.val

		if self.expr == "LSHIFT":
			self.val = self.lshift(self.a.eval(), self.b.eval())
			return self.val

		if self.expr == "RSHIFT":
			self.val = self.rshift(self.a.eval(), self.b.eval())
			return self.val



class constant:
	def __init__(self, val):
		self.val = val
		self.ID = str(val)
		self.a = None
		self.b = None

	def eval(self):
		return self.val

	def view(self):
		return

def makeWire(name):
	if name.isdigit():
		return constant(int(name))
	return node(data[name])


root = makeWire('a')

print("tree")

print(root.eval())