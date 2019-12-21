import re

num = re.compile(r'(\-?[0-9]+)')

print(sum([int(i) for i in num.findall(open("d12", "r").read())]))