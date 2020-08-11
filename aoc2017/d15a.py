# Generator A starts with 516
# Generator B starts with 190

def generator(start, multiplier):
    s = start
    m = multiplier

    while True:
        s *= m
        s = s % 2147483647
        yield s

def compare(a, b):
    arem = a % 2**16
    brem = b % 2**16

    if arem == brem:
        return 1

    return 0

a = generator(516, 16807)
b = generator(190, 48271)

count = 0
for _ in range(4 * 10**7):
    count += compare(next(a), next(b))

print(count)