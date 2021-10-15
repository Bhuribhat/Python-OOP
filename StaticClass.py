class Vehicle:
    # Class Variables
    vehicles = list()
    OIL = 10

    def __init__(self, name):
        self.name = name
        self.vehicles.append(self)

    # receives the class as implicit first argument, need at least 1 parameter
    @classmethod
    def num_vehicle(cls):
        # can access class variables
        return len(cls.vehicles)

    # does not receive an implicit first argument, cannot access class variables
    @staticmethod
    def beep(n):
        """beeps n times"""
        for _ in range(n):
            print("Beep !!")

class Math:
    @staticmethod
    def add(x, y):
        return x + y

# instantiate objects
Honda = Vehicle("Honda")
Benz = Vehicle("Benz")

print(Honda.vehicles)
print(Vehicle.vehicles)

# class method -> don't need to create an object of a class to use them
print(Vehicle.num_vehicle())
print(Benz.num_vehicle())

# static method -> don't need self and object class as parameter
Vehicle.beep(5)
print(Math.add(3, 5))