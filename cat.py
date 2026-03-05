from animal import Animal
from leg import Leg

cat = Animal()
dog = Animal()

cat.eyes = 1
dog.eyes = 4

how_many_eyes = dog.eyes

cat.show()
dog.show()
print(how_many_eyes)

cat.show()

left_leg = Leg()

left_leg.smelly = False
print(left_leg.is_smelly())