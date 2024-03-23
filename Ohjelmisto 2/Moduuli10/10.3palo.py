#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee
# palohälytys.

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

    def fire_alarm(self):
        print("FIRE ALARM!!! ALL ELEVATORS DOWN!")
        print("------------")
        n = len(self.elevators)
        i = 0
        for elevator in self.elevators:
            print(f"Elevator number: {n-i}")
            i += 1
            if elevator.floor == self.lowest:
                print("Elevator is already on ground floor.")
            else:
                elevator.transfer_to_floor(self.lowest)
            print("------------")

house1 = House(1, 5, 3)
house2 = House(2, 10, 2)
print("Elevators in house 1:")
house1.ride_elevator(1, 3)
house1.ride_elevator(3, 2)
house1.fire_alarm()
print("Elevators in house 2:")
house2.ride_elevator(1, 3)
house2.ride_elevator(2, 8)
house2.fire_alarm()
