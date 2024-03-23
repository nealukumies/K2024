#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton
# ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi
# sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
# polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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

class Electric(Car):
    def __init__(self, registration, top_speed, battery_capacity):
        super().__init__(registration, top_speed)
        self.battery_capacity = battery_capacity

    def print_table(self):
        print("----------------------")
        print("Sähköauto")
        print(f"Rekisteritunnus: {self.registration} \nHuippunopeus: {self.top_speed} km/h\nAkkukapasiteetti: {self.battery_capacity} kWh\nNopeus: {self.speed} km/h\nKuljettu matka: {self.distance} km")


class Petrol(Car):
    def __init__(self, registration, top_speed, tank):
        super().__init__(registration, top_speed)
        self.tank = tank

    def print_table(self):
        print("----------------------")
        print("Polttomoottoriauto")
        print(f"Rekisteritunnus: {self.registration} \nHuippunopeus: {self.top_speed} km/h\nTankkikoko: {self.tank} l\nNopeus: {self.speed} km/h\nKuljettu matka: {self.distance} km")


electric1 = Electric("ABC-15", 180, 52.5)
petrol1 = Petrol("ACD-123", 165, 32.3)
electric1.speed = 100
petrol1.speed = 90
electric1.drive(3)
petrol1.drive(3)
electric1.print_table()
petrol1.print_table()