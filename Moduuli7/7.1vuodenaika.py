#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
# tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi
# kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on
# ensimmäinen talvikuukausi.

seasons=("talvi", "kevät", "kesä", "syksy")

month=int(input("Syötä kuukauden numero (1-12): "))

if month>12 or month<0:
    print("Et tainnut syöttää kuukautta 1-12!")
elif month==12 or month<3:
    print(f"Nyt on {seasons[0]}.")
elif month==3 or month<6:
    print(f"Nyt on {seasons[1]}.")
elif month==6 or month<9:
    print(f"Nyt on {seasons[2]}.")
else:
    print(f"Nyt on {seasons[3]}.")


