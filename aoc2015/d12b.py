import re

num = re.compile(r'(\-?[0-9]+)')

total = 0

stack = 0
ptr = 0
string = open("scrap", "r").read()
while ptr < len(string):
	if string[ptr] == "{":
		stack += 1
	if string[ptr] == "}":
		stack -= 1

	if stack == 0 and num.match(string[ptr:]):
		total += int(num.match(string[ptr:]).group(0))
		ptr += len(num.match(string[ptr:]).group(0)) - 1

	ptr += 1

print(total)
