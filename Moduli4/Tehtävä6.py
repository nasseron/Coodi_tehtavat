import random
N = 100000
n = toisto = x = y = 0
while toisto <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    toisto += 1
    if x ** 2 + y ** 2 <= 1:
        n += 1
print("Piin arvo on noin ", 4 * n /N)
