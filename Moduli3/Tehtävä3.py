sukupoli = input("Mikä on sukupuoli? ")
hemoglobiini = int(input("Mikä on sinun hemoglobiiniarvo? "))

if sukupoli == "nainen" and hemoglobiini < 117:
    print("hemoglobiiniarvo on alhainen.")
elif sukupoli == "naine" and hemoglobiini == 117 - 175:
    print("hemohglobiiniarvo on normaali.")
elif sukupoli == "naine" and hemoglobiini > 175:
    print("hemohglobiiniarvo on korke.")
elif sukupoli == "nainen" and hemoglobiini < 134:
    print("hemoglobiiniarvo on alhainen.")
elif sukupoli == "naine" and hemoglobiini == 134 - 195:
    print("hemohglobiiniarvo on normaali.")
elif sukupoli == "naine" and hemoglobiini > 195:
    print("hemohglobiiniarvo on korke.")
