#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
    #kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
    #nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

print("Tämä ohjelma tulostaa kaksi erilaista numerolukon koodia:")
code_1=random.randint(0, 9), random.randint(0, 9), random.randint(0,9)
code_2=random.randint(1, 6), random.randint(1, 6), random.randint(1,6), random.randint(1,6)
print("Tässä sinulle kolminumeroinen koodi: " + code_1 + ", ole hyvä!")
print("Tässä sinulle nelinumeroinen koodi: " + code_2 + ", ole hyvä!")