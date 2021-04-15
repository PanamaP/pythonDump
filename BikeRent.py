# Elfar Snær Arnarson
# 27 Febrúar 2020
# Skilaverkefni 4


class BikeRent:

    def __init__(self, inventory=15):
        self.inventory = inventory

    def displayinv(self):
        with open("bike_inventory.txt", "r") as f:
            fjoldi = f.read().replace('\n', '')
            self.inventory = int(fjoldi)
        print(f"Currently there are {self.inventory} bikes available to rent.")
        return self.inventory


class Customer:

    def __init__(self):
        pass

    def bike_request(self):
        bikes = int(input("How many bikes would you like to rent? : "))
        self.bikes = bikes
        with open("bike_inventory.txt", "r") as f:
            fjoldi = f.read().replace('\n', '')
            fjoldi = int(fjoldi) - int(bikes)
            inventory = str(fjoldi)
        with open("bike_inventory.txt", "w") as f:
            f.write(inventory)
        print(self.bikes)

    def bike_return(self):
        days = int(input('How many days did you rent? : '))
        bike_return = int(input('How many bikes? : '))
        with open("bike_inventory.txt", "r") as f:
            fjoldi = f.read().replace('\n', '')
            fjoldi = int(fjoldi) + int(bike_return)
            inventory = str(fjoldi)
        bill = days * bike_return * 20
        print(f"Thanks for the return, the bill is ${bill}")
        with open("bike_inventory.txt", "w") as f:
            f.write(inventory)