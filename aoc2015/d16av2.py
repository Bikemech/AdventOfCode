import re

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


Sues = open("d16.puz", "r").readlines()
attr = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

for j, rg in enumerate(REGEX):
	for i, aunt in enumerate(Sues):
		if rg.search(aunt):
			if int(rg.search(aunt).group(1)) != attr[j]:
				Sues[i] = ""

for i in Sues:
	if i:
		print(i)