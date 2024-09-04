import random
luku = int(input("Kuinka monta kertaa haluat heittää yhden kiven? "))

summa = 0
for i in range (luku):
    kivi = random.randint(1,6)
    print('kivi', kivi)
    summa = summa + kivi

print(f"Arpakuutioden silmälukujen summa on: {summa}")