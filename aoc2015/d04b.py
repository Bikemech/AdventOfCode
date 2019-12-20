from hashlib import md5
import re

key = open("d04", "r").read()
test = re.compile(r'(0){6}')
index = 254575 # from part 1

while True:
	hash_ = md5()
	line = "%s%d"%(key, index)
	hash_.update(line.encode())
	if test.match(str(hash_.hexdigest())):
		break
	index += 1

print(index)