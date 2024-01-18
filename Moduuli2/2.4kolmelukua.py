#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon
print("Leikitäänpä sitten vähän numeroilla :)")
print("Seuraavaksi pyydän kolmea kokonaislukua")
number_a=int(input("Kirjoita ensimmäinen luku tähän: "))
number_b=int(input("Kirjoita toinen luku tähän: "))
number_c=int(input("Kirjoita kolmas luku tähän: "))
sum=number_a+number_b+number_c
product=number_a*number_b*number_c
mean=sum/3
print("Lukujesi summa on " +str(sum) + ", tulo on " + str(product) + " ja keskiarvo on " + str(mean))