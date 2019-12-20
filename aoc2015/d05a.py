import re

vowel = re.compile(r'[aeiou]')
repeat = re.compile(r'(.)\1{1}')
naughty = re.compile(r'(ab|cd|pq|xy)')

def check(string):
	if naughty.search(string):
		return 0

	if len(vowel.findall(string)) > 2 and repeat.search(string):
		return 1
	return 0

count = 0
for i in open("d05", "r").readlines():
	count += check(i)

print(count)
