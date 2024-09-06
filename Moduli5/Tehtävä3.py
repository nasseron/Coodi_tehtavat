
luku = int(input("Anna luku( ilmoitta jos on alkuluku)"))
is_prime = True
if luku <= 1:
    is_prime = False
else:
    for i in range(2, int(luku**0.5)+1):
        if luku % i == 0:
            is_prime = False
            break
    if is_prime:
        print(luku, "On alkuluku")
    else:
        print(luku, "Ei olealkuluku")




