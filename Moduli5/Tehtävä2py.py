from random import random

numbers = []

syote = input("Anna luku (tai tyhja merkijono pyshtömään): ")
while syote != '' :
    numbers.append(int(syote))
    syote = input("Anna luku (tai tyhja merkijono pyshtömään): ")

numbers.sort(reverse=True)
print(numbers[0:5])
for i in range (0,5):
    print(f'Numero: {numbers[i]}')


