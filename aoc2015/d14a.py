import re
num = re.compile(r'(\d+)')

class deer:
	def __init__(self, line):
		self.t = 0
		self.vel = int(num.findall(line)[0])
		self.per = int(num.findall(line)[1])
		self.rest = int(num.findall(line)[2])
		self.dist = 0

	def tick(self):
		self.t += 1
		if self.t % (self.per + self.rest) <=  self.per:
			self.dist += self.vel

items = [deer(line) for line in open("scrap", "r").readlines()]

for i in range(1001):
	for j in items:
		j.tick()

for i in items:
	print(i.dist)