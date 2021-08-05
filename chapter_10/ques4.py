class Calculator:
    def __init__(self, n):
        self.num = n
    def square(self):
        print(f"Square is {self.num **2}")
    def squareRoot(self):
        print(f"Square root is {self.num **0.5}")
    def cube(self):
        print(f"Cube is {self.num **3}")
    @staticmethod
    def greet():
        print("This is a nice calculator!")
a = Calculator(25)
a.greet()
a.square()
a.squareRoot()
a.cube()