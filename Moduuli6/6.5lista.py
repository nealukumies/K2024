#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki
# parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

import random

amount=int(input("Syötä tähän kuinka monta numeroa haluat syöttää listalle: "))
numbers=[]
def list(numbers):
    for i in range(amount):
        numbers.append(random.randint(1,10))
    return numbers
def even(values):
    new_list=[]
    for n in values:
        if n%2==0:
            new_list.append(n)
    return new_list

original_list=list(numbers)
even_list=even(original_list)
print(f"Alkuperäinen lista on {original_list}.")
print(f"Karsittu lista on {even_list}.")
