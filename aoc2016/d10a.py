import re

REGEX = re.compile(r'(\d*)x(\d*)')
string = open("d10.input").read()

string = "A(2x2)BCD(2x2)EFG"


def parse(string):
	R = REGEX.match(string)
	return int(R.group(1)), int(R.group(2))


ptr = 0
str_len = 0

p = REGEX.search(string[ptr:])
ptr += p.span()[0]
str_len += p.span()[0] - 1 + parse(string[ptr:])[0] * parse(string[ptr:])[1]
ptr += p.span()[1] - p.span()[0] + 1

print(ptr)
print(str_len)