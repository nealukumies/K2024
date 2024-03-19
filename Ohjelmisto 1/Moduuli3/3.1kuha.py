# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Onko alamittainen? Paljon jää sallitusta pyyntimitasta.
# Kuha on alamittainen 37 cm.

kuha=float(input("Syötä kalastamasi kuhan pituus senttimetreissä: "))
if kuha<37:
    alamitta=37-kuha
    print(f"Kuha on alamittainen. Salllitusta pyyntimitasta uupuu {alamitta} senttimetriä.")
elif kuha==37:
    print("Kuha on juuri ja juuri sallitun pyyntimitan kokoinen.")
elif kuha>37:
    print("Onneksi olkoon! Kuhan pituus ylittää sallitun pyyntimitan.")