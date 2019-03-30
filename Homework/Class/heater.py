class Heater():

    def __init__(self, size, power):
        self.size = size
        self.power = power


    def __str__(self):
        return f"Your heater is {self.size} and has power: {self.power}"
