#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
# per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
# ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
# yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math
def price_per_area(diameter, price):
    diameter_m=diameter/100 #metreiksi
    area=((diameter_m/2)*(diameter_m/2))*math.pi
    per_area=price/area #hinta/neliömetri
    return per_area

pizza1_price=float(input("Paljon ensimmäinen pizza maksaa?\n"))
pizza1_diameter=float(input("Mikä on pizzan halkaisija senttimetreissä?\n"))
pizza1=price_per_area(pizza1_diameter, pizza1_price)

pizza2_price=float(input("Paljon toinen pizza maksaa?\n"))
pizza2_diameter=float(input("Mikä on toisen pizzan halkaisija senttimetreissä?\n"))
pizza2=price_per_area(pizza2_diameter, pizza2_price)

if pizza1>pizza2:
    print(f"Sinun kannattaa ostaa toinen pizza, jonka hinta oli {pizza2_price} ja halkaisija {pizza2_diameter}.")
elif pizza1<pizza2:
    print(f"Sinun kannattaa ostaa ensimmäinen pizza, jonka hinta oli {pizza1_price} ja halkaisija {pizza1_diameter}.")
else:
    print("Pizzojen yksikköhinnat ovat samat, joten valitse houkuttelevampi pizza.")