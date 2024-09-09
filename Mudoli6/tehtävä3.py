def gallons_to_liters(gallons):
    liters = gallons * 3.785
    return liters

gallons_mount = float(input('Gallons mount: '))
while gallons_mount > 0:
    A = gallons_to_liters(gallons_mount)
    print(A)
    gallons_mount = float(input('Gallons mount: '))
    if gallons_mount < 0:
         print("Presse enter to stop!")
