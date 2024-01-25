#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä
# antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. Tuuma=2,54cm

inches=float(input("Syötä tuumat: "))
while inches>0:
    cms=inches*2.54
    print(f"Syötit {inches} tuumaa, joka on {cms} senttimetriä.")
    inches=float(input("Syötä tuumat: "))