#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

import random

def sum_num(numbers):
    sum_numbers=sum(numbers)
    return sum_numbers

amount=int(input("Syötä tähän kuinka monta numeroa haluat syöttää listalle: "))

numbers=[]
for i in range(amount):
    numbers.append(random.randint(1, 10))
print(numbers) #jotta nähdään mikä on lista

print(sum_num(numbers))