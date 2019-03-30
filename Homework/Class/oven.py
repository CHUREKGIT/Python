class Oven:
    def __init__(self, width, height, litres, type, color):
        self.width = width
        self.height = height
        self.litres = litres
        self.type = type
        self.color = color

    def turn_on(self):
        return "Your Oven is turn on"

    def __str__(self):
        return f"Oven with {self.width}cm, {self.height}cm, {self.litres}l and it is {self.type} and {self.color}"