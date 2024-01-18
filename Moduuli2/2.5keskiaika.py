#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
# leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi
# ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

print("Keskiajalla massa ilmoitettiin leivisköinä, nauloina ja luoteina")
print("Ilmoita massa keskiaikoisten mittojen mukaan niin ilmoitan massan nykymittojen mukaan")
leiviskat=float(input("Anna leiviskät: "))
naulat=float(input("Anna naulat: "))
luodit=float(input("Anna luodit: "))

leiviskat_g=leiviskat*8512
naulat_g=naulat*425.6
luodit_g=luodit*13.3
massa=leiviskat_g+naulat_g+luodit_g
massa_kg=int(massa/1000)
massa_g=round(massa-(massa_kg*1000), 2)

print("Massa nykymittojen mukaan:")
print(str(massa_kg) + " kilogrammaa ja " + str(massa_g) + " grammaa.")