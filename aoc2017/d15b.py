# Generator A starts with 516
# Generator B starts with 190

def generator(start, multiplier, divider):
    s = start
    m = multiplier

    while True:
        s *= m
        s = s % 2147483647
        if s % divider == 0:
            yield s

def compare(a, b):
    arem = a % 2**16
    brem = b % 2**16

    if arem == brem:
        return 1

    return 0

a = generator(516, 16807, 4)
b = generator(190, 48271, 8)

count = 0
for _ in range(5 * 10**6):
    count += compare(next(a), next(b))


print(count)