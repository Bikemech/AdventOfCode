data = [int(i) for i in open("d02", "r").read().split(",")]

data[1] = 12
data[2] = 2

def run(data):
	try:
		for i, j in enumerate(data):
			if i % 4 == 0:
				if j == 1:
					data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]

				elif j == 2:
				    data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]

				elif j == 99:
					print("finish")
					print(i, j)
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
		raise

print(run(data[:])[0])

print(data[0])
