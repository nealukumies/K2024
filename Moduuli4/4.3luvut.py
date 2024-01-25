#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


first_number=True
biggest=0
smallest=0

while True:
    number = input("Syötä luku: ")
    if number=="":
        break
    try:
        num=float(number)
        if first_number is True:
            smallest=num
            biggest=num
            first_number=False
        else:
            if num<smallest:
                smallest=num
            elif num>biggest:
                biggest=num
    except ValueError:
        print("Syötä luku tai jätä tyhjäksi.")

print(f"Saaduista luvuin pienin on {smallest} ja suurin luku {biggest}.")