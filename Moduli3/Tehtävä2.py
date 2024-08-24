laivan_hyttiluoka = input("Mikä on laivan hyttiluoka ? ")
if laivan_hyttiluoka == "LUX":
    print(laivan_hyttiluoka + " On parvikkellinen hytti yläkannella.")
elif laivan_hyttiluoka == "B":
    print(laivan_hyttiluoka + " On ikkunallinen hytti autokannen yläpuolella.")
elif laivan_hyttiluoka == "C":
    print(laivan_hyttiluoka + " On ikkunaton hytti autokannen alapuolella.")
else:
    print("virhellinen hyttiluokka.")