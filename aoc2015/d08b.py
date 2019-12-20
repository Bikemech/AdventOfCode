import re

regspc = re.compile(r'[\'\"\\]')
	
def strVal(string):
	tot = len(string) + 2
	tot += len(regspc.findall(string))
	return tot

total = 0
for i in open("d08", "r").readlines():
	val = strVal(i.strip()) - len(i.strip())
	total += val
	

print(total)