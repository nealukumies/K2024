#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
# gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gas(gallon):
    litre=gallon*3.785
    return litre

gallon=float(input("Syötä tähän bensiinin määrä gallonoina: "))

while gallon>0:
    print(f"{gallon} gallonaa on {gas(gallon):.2f} litraa")
    gallon = float(input("Syötä tähän bensiinin määrä gallonoina: "))