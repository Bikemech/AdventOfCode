# This time we need to find the number after 0 after the 5*10 ^ 7:th number is inserted
# Since 0 always will remain in position 0 we need only to calculate when the last time a
# number is inserted at position 1 or more precisely when the total position is congruent to
# zero in modulo(len(buffer))

from time import time



step = 359
number = 0

index = 0

start = time()

for i in range(1, 5*10**7):
    index += step
    index = index % i
    if index % i == 0:
        number = i

    index += 1

print(time() - start)

print()
print(number)
