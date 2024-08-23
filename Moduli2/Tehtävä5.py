leiviskat = int(input("Anna leiviskät :"))
naulat = int(input("Anna naulat :"))
luodit = float(input("Anna leuodit :"))
leiviskat_gramma = leiviskat * 20 * 32 * 13.3
naulat_gramma = naulat * 32 * 13.3
luodit_gramma = luodit*13.3

vastaus = leiviskat_gramma + naulat_gramma + luodit_gramma
print(vastaus/1000)
#leiviskat_kg = leiviskat_gramma * 1000
#naulat_kg = naulat_gramma * 1000
#luodit_kg = luodit_gramma * 1000