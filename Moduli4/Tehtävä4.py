number = 1
while True:
    number = int(input("Guesse a number: "))
    if number >=1  and number <=10:
        print("Your guess is correct.")
        break
    elif number > 10:
        print("Your guess is too big.")
    else:
        print("Your guess is too small.")

