import re

rgnum = re.compile(r'\s(\d+):')
REGEX = [re.compile(r'children:\s(\d+)'),
	re.compile(r'cats:\s(\d+)'),
	re.compile(r'samoyeds:\s(\d+)'),
	re.compile(r'pomeranians:\s(\d+)'),
	re.compile(r'akitas:\s(\d+)'),
	re.compile(r'vizslas:\s(\d+)'),
	re.compile(r'goldfish:\s(\d+)'),
	re.compile(r'trees:\s(\d+)'),
	re.compile(r'cars:\s(\d+)'),
	re.compile(r'perfumes:\s(\d+)')]

class Sue:
	def __init__(self, string):
		self.id = int(rgnum.search(string).group(1))
		self.attributes = [-1 for i in range(10)]

		for i, rg in enumerate(REGEX):
			if rg.search(string):
				self.attributes[i] = (int(rg.search(string).group(1)))				

	def __repr__(self):
		return str(self.id)

	def compare(self, other):
		for i, attr in enumerate(self.attributes):
			if attr > -1:
				if attr != other.attributes[i]:
					return False

		return True

OUR_SUE = Sue("Sue 1001: children: 3 cats: 7 samoyeds: 2 pomeranians: 3 akitas: 0 vizslas: 0 goldfish: 5 trees: 3 cars: 2 perfumes: 1")

Sues = [Sue(i) for i in open("d16.puz", "r").readlines()]

for i, j in enumerate([3, 7, 2, 3, 0, 0, 5, 3, 2, 1]):
	temp = []
	for aunt in Sues:
		if aunt.attributes[i] == -1 or aunt.attributes == j:
			temp.append(aunt)

	if len(temp) == 0:
		print(Sues)


	Sues = temp