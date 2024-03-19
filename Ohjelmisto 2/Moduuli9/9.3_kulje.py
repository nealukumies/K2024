#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
# tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.



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
        self.distance += time * self.speed

    def print(self):
        print("----------------------")
        print(f"Rekisteritunnus: {self.registration} \nHuippunopeus: {self.top_speed} km/h\nNopeus: {self.speed} km/h\nKuljettu matka: {self.distance} km")


new_car = Car("ABC-123", 142)
new_car.distance = 2000
new_car.speed = 60
new_car.print()
print("----------------------")
print("Auton tiedot 1,5h jälkeen: ")
new_car.drive(1.5)
new_car.print()