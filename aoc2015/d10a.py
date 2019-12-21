import re

def look_say(x):
	ptr = x[0]
	new = ""
	c = 1

	for i in x[1:]:
		if i == ptr:
			c += 1
		else:
			new += "%d%s"%(c, ptr)
			c = 1

		ptr = i

	new += "%d%s"%(c, ptr)

	return new

data = "1113122113"

for i in range(40):
	data = look_say(data)

print(len(data))

for i in range(10):
	data = look_say(data)

print(len(data))