#Ohjelma, joka kysyy suorakulmion kannan ja korkeuden
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
#Suorakulmion piiri tarkoittaa sen neljän sivun yhteyspituutta

print("Lasketaanpa seuraavaksi suorakulmion piiri ja pinta-ala")
print("Tässäkin lopullinen yksikkö riippuu siitä, missä yksikössä olet syöttänyt tiedot")
print("Muista käyttää samaa yksikköä sekä korkeuden, että kannan ilmoittamisessa\n")
height=int(input("Syötä tähän suorakulmiosi korkeus numeronäppäimillä: "))
width=int(input("Syötä tähän suorakulmiosi kanta numeronäppäimillä: "))
rectangle_area=height*width
rectangle_perimeter=2*height+2*width
print("Suorakulmion piiri on " + str(rectangle_perimeter) + " ja pinta-ala " + str(rectangle_area))