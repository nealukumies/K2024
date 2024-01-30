#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random

amount=int(input("Syötä tähän monta arpakuutiota heität: "))

list=[]

for i in range(amount):
    number=random.randint(1,6)
    list.append(number)

print(f"Heitit {amount} arpakuutiota ja silmälukujen summa on {sum(list)}.")