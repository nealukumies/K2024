#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

lista=[]
luku=input("Syötä kokonaisluku: ")

while True:
    if luku=="":
        break
    else:
        lista.append(int(luku))
        luku=input("Syötä kokonaisluku: ")

jarjestetty=sorted(lista, reverse=True)  #Järjestää listan suurimmasta pienimpään

print(jarjestetty[0:5])
