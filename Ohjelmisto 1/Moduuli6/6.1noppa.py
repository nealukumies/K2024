#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
# silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan
# kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random
def dice():
    value=random.randint(1,6)
    return value

value=0
while value<6: #heittää noppaa kunnes silmäluku 6
    value=dice()
    print(value)