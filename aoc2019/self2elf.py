from sys import argv
import re
from os import system # windows only....

def alter_string(line, from_, to_):
	target = re.compile(r'[\W]*(%s)[\W]*'%from_)
	phrase = target.search(line)
	if phrase:
		return line.replace(phrase.group(1), to_)

if len(argv) < 5:
	print("no default settings!!")
	print("<input filename> <output filename> <target word> <new word>")
	exit(1)

f = open(argv[1], "r")
lines = f.readlines()
f.close()

system("mkdir new")

new_file = open(".\\new\\%s"%argv[2], "w")

for v1 in lines:
	v2 = alter_string(v1, argv[3], argv[4])
	if v2:
		new_file.write(v2)
	else:
		new_file.write(v1)
