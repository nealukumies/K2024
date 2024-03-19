#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
# ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton
# nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
# jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen
# jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, registration, top_speed):
        self.registration = registration
        self.top_speed = top_speed
        self.speed = 0
        self.distance = 0

    def print(self):
        print("----------------------")
        print(f"Rekisteritunnus: {self.registration} \nHuippunopeus: {self.top_speed} km/h\nNopeus: {self.speed} km/h\nKuljettu matka: {self.distance} km")


new_car = Car("ABC-123", 142)
new_car.print()