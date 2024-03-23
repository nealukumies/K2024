# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina
# annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä
# talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita
# taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita
# pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


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
    def transfer_to_floor(self, floor_number):
        if floor_number > self.floor:
            amount = floor_number - self.floor
            for i in range(amount):
                self.floor_up()
        elif floor_number < self.floor:
            amount = self.floor - floor_number
            for i in range(amount):
                self.floor_down()
        else:
            print(f"Elevator is on floor {floor_number}")
        print("You can step out of elevator.")


class House:
    def __init__(self, lowest, highest, amount_of_elevators):
        Elevator.__init__(self, lowest, highest)
        self.amount_of_elevators = amount_of_elevators
        self.elevators = []
        for i in range(amount_of_elevators):
            self.elevators.append(Elevator(lowest, highest))

    def ride_elevator(self, elevator_number, floor_number):
        print(f"Elevator number: {elevator_number}")
        self.elevators[(elevator_number)-1].transfer_to_floor(floor_number)
        print("------------")

house1 = House(1, 10, 3)
house1.ride_elevator(1, 8)
house1.ride_elevator(2, 10)
house1.ride_elevator(1, 2)
