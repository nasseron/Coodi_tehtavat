kuhan_pitus = int(input("Kuinka monta sentimetria kuha on pitka? "))
alamittainen = 37
alimminsallitty_pyyntimittaus = alamittainen -kuhan_pitus
if kuhan_pitus < alamittainen:
    print("Laske kuha takaisin järveen")
    print("On jäljellä ",alimminsallitty_pyyntimittaus,"cm senttiä alimmasta sallitusta pyyntimitasta puuttuu.")