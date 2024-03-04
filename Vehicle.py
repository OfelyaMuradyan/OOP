class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"Vehicle's make is {self.make} and the model is {self.model}."

class Car(Vehicle):
    def __init__(self, make, model, number_of_wheels = 4):
        super().__init__(make, model)
        self.number_of_wheels = number_of_wheels

    def __repr__(self):
        return f"Car's make is {self.make} and the model is {self.model}. It has {self.number_of_wheels} wheels."
    
car = Car("Toyota", "Camry")
vehicle = Vehicle("Mercedes-Benz","S-class")
print(repr(car))
print(repr(vehicle))
