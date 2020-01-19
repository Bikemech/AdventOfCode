import json

def sum_numbers(obj):
    if type(obj) == type(dict()):
        if "red" in obj.values():
            print(obj.values())
            return 0
        return sum(map(sum_numbers, obj.values()))

    if type(obj) == type(list()):
        return sum(map(sum_numbers, obj))

    if type(obj) == type(0):
        return obj

    return 0

data = json.loads(open('d12.puz', 'r').read())
print(sum_numbers(data))

for i in data:
    print(i)
    print(sum_numbers(i))