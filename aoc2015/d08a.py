import re

reghex = re.compile(r'(\\x[0-9a-f]{2})')
regesc = re.compile(r'(\\[\\\"\'])')
	
def strVal(string):
	tot = len(string) - 2
	tot -= len(reghex.findall(string)) * 3
	tot -= len(regesc.findall(string))
	return tot

total = 0
for i in open("d08", "r").readlines():
	val = strVal(i.strip())
	total += len(i.strip()) - val

print(total)