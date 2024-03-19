#Kirjoita ohjelma, joka kysyy sukupuolen ja Hb
#Ohjelma ilmoittaa, onko alhainen, normaali vai korkea
#Viitearvot: Naisen 117-175 g/l, Miehen 134-195 g/l

print("Tämä ohjelma kertoo onko hemoglobiinisi alhainen, normaali vai korkea.\n")
print("Syötä ensin sukupuolesi N: Nainen tai M: Mies.")
sukupuoli=input("N/M: ")

if sukupuoli=="N" or sukupuoli=="n":
    hb = int(input("Syötä tähän hemoglobiini-arvosi yksikössä g/l: "))
    if hb<117:
        print("Hemoglobiini-arvosi on alhainen.")
    elif hb>117 and hb<175:
        print("Hemoglobiini-arvosi on normaali.")
    else:
        print("Hemoglobiini-arvosi on korkea.")
elif sukupuoli=="M"  or sukupuoli=="m":
    hb = int(input("Syötä tähän hemoglobiini-arvosi yksikössä g/l: "))
    if hb<134:
        print("Hemoglobiini-arvosi on alhainen.")
    elif hb>134 and hb<195:
        print("Hemoglobiini-arvosi on normaali.")
    else:
        print("Hemoglobiini-arvosi on korkea.")
else:
    print("Et tainnut syöttää sukupuolta oikeassa muodossa.")