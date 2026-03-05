from animal import Animal
from leg import Leg

class Cat(Animal):
    left_leg = Leg()
    right_leg = Leg()
    name = ""

    def __init__(self, cat_name = None):
        if cat_name is None:
            self.name = "No name"
        else:
            self.name = cat_name
    
    def show(self):
        print("This cat's name is ")
        print(self.name)
        super().show()
    pass

Willow = Cat("Willow")
Willow.eyes = 1
Willow.show()