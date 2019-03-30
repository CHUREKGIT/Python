from TV import TV
from heater import Heater
from oven import Oven

class Kitchen():
    def __init__(self, size):
        self.size = size
        self.tv = None
        self.heater = None
        self.oven = None


jakub_tv = TV(40, 50, True)
jakub_heater = Heater("small", "1.6kw")
jakub_oven = Oven(150, 200, 56, "electronic", "black")

jakub_kitchen = Kitchen("large")

jakub_kitchen.tv = jakub_tv
jakub_kitchen.heater = jakub_heater

print(jakub_kitchen.tv)
print(jakub_heater)
print(jakub_oven)
