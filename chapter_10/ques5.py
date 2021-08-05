class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Name of train is {self.name}.")
        print(f"Fare of train is Rs. {self.fare}.")
        print(f"Seats of train is {self.seats}.")

intercity = Train("intercity", 300, 60)
intercity.getStatus()