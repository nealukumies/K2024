import random
#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
    #kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
    #nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

print("Tämä ohjelma tulostaa kaksi erilaista numerolukon koodia\n")
a=random.randint(0, 9)
b=random.randint(0, 9)
c=random.randint(0, 9)
code_1=str(a)+str(b)+str(c)
d=random.randint(1,6)
e=random.randint(1,6)
f=random.randint(1,6)
g=random.randint(1,6)
code_2=str(d)+str(e)+str(f)+str(g)
print("Tässä sinulle kolminumeroinen koodi: " + code_1 + ", ole hyvä!")
print("Tässä sinulle nelinumeroinen koodi: " + code_2 + ", ole hyvä!")