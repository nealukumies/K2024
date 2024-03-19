#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luku=int(input("Syötä kokonaisluku: "))

if luku==1:
    print("Luku 1 ei ole alkuluku")

elif luku>1:
    for i in range(2, int(luku/2)+1):
        if (luku%i)==0:
            print("Luku ei ole alkuluku")
            break #riittää kun ehto täyttyy kerran, ei tarvitse tsekata koko rangea
        else:
            print(f"Luku on alkuluku")
            break #printtaa vain kerran