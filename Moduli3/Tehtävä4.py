vuosiluku = int(input("Mikä on vuosiluku?: "))
if vuosiluku % 4 == 0:
    print("Vuosiluku on karkausvuosiluku.")
elif vuosiluku % 100 == 0 and vuosiluku % 400 == 0:
    print("Vuosiluku on karkausvuosiluku")
else:
    print("vuosiluku ei ole karkausvuosiluk.")