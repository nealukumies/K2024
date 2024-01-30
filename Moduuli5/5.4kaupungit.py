#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
# niiden läpikäymiseen.

cities=[]

for i in range(0,5):
    kaupunki=input("Syötä tähän kaupungin nimi: ")
    cities.append(kaupunki)

for city in cities:
    print(city)