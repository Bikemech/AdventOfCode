def run(data):
	try:
		for i, j in enumerate(data):
			if i % 4 == 0:
				if j == 1:
					data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]

				elif j == 2:
				    data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]

				elif j == 99:
					return data

				else:
					print("Run time Error")
					print(i, j)
					return [2]
		print("EOF")
		return data
	except:
		print("\t\t", i, j, "\n\n")
		print(data)


data = [int(i) for i in open("d02", "r").read().split(",")]


target = 19690720
a, b = 0, 0

for i in range(100):
	for j in range(100):
		data[1] = i
		data[2] = j
		t = run(data[:])[0]
		if t == target:
			print(i, j)
			print(t)




