#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä
# syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
# joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi
# ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
# allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

names=set()

name = input("Syötä nimi: ")

while True:
    if name=="":
        break
    elif name in names:
        print("Aiemmin syötetty nimi.")
        name=input("Syötä nimi: ")
    elif name not in names:
        names.add(name)
        print("Uusi nimi.")
        name = input("Syötä nimi: ")
        
print(names)