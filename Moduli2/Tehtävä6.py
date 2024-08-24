import random
kolmenumeroisen_koodi = ""
for i in range (3):
    kolmenumeroisen_koodi += str(random.randint(0,9))
nelinumeroisen_koodi = ""
for i in range (4):
    nelinumeroisen_koodi += str(random.randint(1, 9))
print(kolmenumeroisen_koodi)
print(nelinumeroisen_koodi)
