#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. Tuuma=2,54cm

tuumat = float(input("Syötä tuumat: "))
while tuumat>0:
    sentit=tuumat*2.54
    print(f"Syötit {tuumat} tuumaa, joka on {sentit} senttimetriä.")
    tuumat=float(input("Syötä tuumat: "))