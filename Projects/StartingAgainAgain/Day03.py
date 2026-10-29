#OOP in Python
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.year} {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.year} {self.make} {self.model} has stopped.")

CarOne = Car("Toyota", "Camry", 2022, "blue")
print(CarOne.make)
print(CarOne.model)
print(CarOne.year)
print(CarOne.color)