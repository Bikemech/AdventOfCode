import re

zigzag = re.compile(r'(\w)\w\1')
double_repeat = re.compile(r'(\w\w)\w*\1')

def check(string):
	if double_repeat.search(string):
		if zigzag.search(string):
			return 1
	return 0

count = 0
for i in open("d05", "r").readlines():
	count += check(i)

print(count)
