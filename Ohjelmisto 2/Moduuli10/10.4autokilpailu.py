# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen
# lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan
# ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
# 1.tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät
# toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# 2.tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# 3.kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
# kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle
# annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun
# etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan
# kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin
# avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

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


class Competition:
    def __init__(self, name, length, amount_of_cars):
        self.name = name
        self.length = length
        self.cars = []
        for i in range(1, amount_of_cars+1):
            speed = random.randint(100, 200)
            new_car = (Car(f"ABC-{i}", speed))
            self.cars.append(new_car)

    def print_table(self):
        for car in self.cars:
            print("------------------------")
            print(f"Rekisteritunnus: {car.registration} \nHuippunopeus: {car.top_speed} km/h\nNopeus: {car.speed} km/h\nKuljettu matka: {car.distance} km")

    def time_flies(self):
        for car in self.cars:
            if car.speed == 0:  # Ei jarruta pysähtyneestä (ei varsinaisesti tehtävänannossa)
                car.accelerate(random.randint(1, 15))
            else:
                car.accelerate(random.randint(-10, 100))
            car.drive(1)

    def end_of_competition(self):
        for car in self.cars:
            if car.distance >= self.length:
                return True, car


competition = Competition("Romuralli", 8000, 10)

rounds = 0
while True:
    rounds += 1
    competition.time_flies()
    if competition.end_of_competition():
        print(80*"-")
        print(f"Kilpailu päättynyt!")
        competition.print_table()
        break
    elif rounds % 10 == 0:
        print(80*"-")
        print("10 tunnin jälkeen tilanne on seuraava:")
        competition.print_table()

