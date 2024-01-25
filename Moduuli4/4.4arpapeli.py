#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

number=random.randint(1, 10)

guess=int(input("Arvaa numero välilä 1-10: "))

while guess != number:
    if guess>number:
        print("Liian suuri arvaus.")
        guess=int(input("Yritä uudestaan: "))
    if guess<number:
        print("Liian pieni arvaus.")
        guess = int(input("Yritä uudestaan: "))

print(f"Oikein! Numero on {number}.")
