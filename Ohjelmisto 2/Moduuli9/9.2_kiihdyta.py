#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
# että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton
# nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa
# ei tarvitse vielä päivittää.



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

    def print(self):
        print("----------------------")
        print(
            f"Rekisteritunnus: {self.registration} \nHuippunopeus: {self.top_speed} km/h\nNopeus: {self.speed} km/h\nKuljettu matka: {self.distance} km")


new_car = Car("ABC-123", 142)
new_car.print()

new_car.accelerate(30)
new_car.print()
new_car.accelerate(70)
new_car.print()
new_car.accelerate(50)
new_car.print()
new_car.accelerate(-200)
new_car.print()
