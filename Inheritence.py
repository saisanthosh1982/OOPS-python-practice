# Inheritence

# Inheretence is a fundemental concept of creating new classes based on existing classes.
# The class which is inherited is called the superclass, and the class that inherits from it is called the subclass.

class Vehicle:
    def __init__(self,brand,model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stopping...")


class Car(Vehicle):
    def __init__(self,brand,model, year, doors, wheels):
        super().__init__(brand, model, year)
        self.doors = doors
        self.wheels = wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, wheels, doors):
        super().__init__(brand, model, year)
        self.wheels = wheels
        self.doors = doors


car = Car('Nissan','Elantra',2012,4,4)
bike = Bike('Hond','300',2020,0,2)
print(car.__dict__)
print(bike.__dict__)
car.start()