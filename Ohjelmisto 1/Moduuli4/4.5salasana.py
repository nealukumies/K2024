#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

id="python"
password="rules"
i=0

while i<5:
    id_input = input("Syötä tunnus: ")
    password_input = input("Syötä salasana: ")
    if id_input==id and password_input==password:
        print("Tervetuloa!")
        break
    i=i+1

if i==5:
    print("Pääsy evätty")