#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
# "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#1. Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
#   Tämä tehdään kutsumalla kiihdytä-metodia.
#2. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin
# auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random
class Car:
    def __init__(self, registration, top_speed):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, speed_change):
            self.speed += speed_change
            if self.speed > self.top_speed:
                self.speed = self.top_speed
            elif self.speed < 0:
                self.speed = 0

    def drive(self, time):
        self.distance += self.speed * time

    def print(self):
        print("----------------------")
        print(f"Rekisteritunnus: {self.registration} \nHuippunopeus: {self.top_speed} km/h\nNopeus: {self.speed} km/h\nKuljettu matka: {self.distance} km")


cars=[]
for i in range(1,11):
    speed = random.randint(100, 200)
    new_car = (Car(f"ABC-{i}", speed))
    cars.append(new_car)
    #new_car.print() Jos haluaa tarkastaa luodut autot


check_distance = True
while check_distance:
    for car in cars:
        if car.speed == 0: #Ei jarruta pysähtyneestä (ei varsinaisesti tehtävänannossa)
            car.accelerate(random.randint(1, 15))
        else:
            car.accelerate(random.randint(-10, 100))
        car.drive(1)
        #car.print() Jos haluaa tarkastaa joka stepin
        if car.distance >= 10000:
            check_distance = False
            break #Molemmat loopit poikki

for car in cars:
    car.print()
