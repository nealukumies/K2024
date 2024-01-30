#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki
# parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

import random
def even(values):
    new_list=[]
    for n in values:
        if n%2==0:
            new_list.append(n)
    return new_list

amount=int(input("Syötä tähän kuinka monta numeroa haluat syöttää listalle: "))

numbers=[]
for i in range(amount):
    numbers.append(random.randint(1, 100))
    #Range vain esimerkkinä alkuperäisen listan luontia varten


print(f"Alkuperäinen lista on {numbers}.")
print(f"Karsittu lista on {even(numbers)}.")
