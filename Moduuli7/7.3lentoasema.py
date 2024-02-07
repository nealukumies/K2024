#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma
# kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn
# lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman
# syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan
# lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja
# helposti selaimen avulla.)

print("Haluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman tiedot (2) vai lopettaa (3)?")
choose=input("Syötä 1, 2 tai 3: ")

airports={}

while True:
    if choose=="1":
        print("Valitsit uuden lentoaseman syöttämisen.\n")

        name=input("Syötä tähän lentoaseman nimi: ")
        code=input("Syötä tähän lentoaseman ICAO-koodi: ")
        airports[code]=name

        print("\nHaluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman tiedot (2) vai lopettaa (3)?")
        choose = input("Syötä 1, 2 tai 3: ")

    elif choose=="2":
        print("Valitsit hakea jo syötetyn lentoaseman tiedot.\n")

        askcode=input("Syötä tähän lentoaseman ICAO-koodi: ")

        if askcode in airports:
            print(f"Lentoaseman nimi on {airports[askcode]}.\n")
        else:
            print("Syöttämääsi ICAO-koodia ei löydy järjestelmästä.\n")

        print("Haluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman tiedot (2) vai lopettaa (3)?")
        choose = input("Syötä 1, 2 tai 3: ")

    elif choose=="3":
        print("Päätit lopettaa.")
        break

    else:
        print("Syötitkö varmasti valintasi numeronäppäimillä ja käytit oikeita numeroita?\n\n")
        print("Haluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman tiedot (2) vai lopettaa (3)?")
        choose = input("Syötä 1, 2 tai 3: ")