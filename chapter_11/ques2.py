class Animals:
    animalType = "mammal"

class Pets(Animals):
    color: "white"

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow")

d = Dog()
d.bark()
print(d.animalType)