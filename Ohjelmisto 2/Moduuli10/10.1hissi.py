#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja
# ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen,
# kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat
# hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa
# hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja
# käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self.floor = lowest

    def floor_up(self):
        self.floor += 1
        print(f"Elevator is now on floor {self.floor}")

    def floor_down(self):
        self.floor -= 1
        print(f"Elevator is now on floor {self.floor}")
    def transfer_to_floor(self, number):
        if number > self.floor:
            amount = number - self.floor
            for i in range(amount):
                self.floor_up()
        elif number < self.floor:
            amount = self.floor - number
            for i in range(amount):
                self.floor_down()
        else:
            print(f"Elevator is on floor {number}")
        print("You can step out of elevator.")


elevator1 = Elevator(1, 10)
elevator1.transfer_to_floor(10)
print(30*"-")
elevator1.transfer_to_floor(1)