import math

#Ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan

print("Lasketaanpa ympyrän säde")
print("Pinta-alan yksikkö riippuu siitä mitä yksikköä käytät ilmoittaessasi sädettä")
print("Eli jos syötät vastauksesi metreissä saat tuloksen neliömetreissä\n")
radius=int(input("Syötä tähän ympyrän säde numeronäppäimillä: "))
circle_area=math.pi*radius**2
print("Ympyrän pinta-ala on " + str(circle_area))