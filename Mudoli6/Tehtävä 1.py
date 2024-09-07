import random
def heita_noppaa():
    return random.randint(1,6)
i = 0
while i != 6:
    i = heita_noppaa()
    print(i)
