class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"Vehicle's make is {self.make} and the model is {self.model}."

class Car(Vehicle):
    def __init__(self, make, model, number_of_wheels = 4):
        super().__init__(make, model)
        self.number_of_wheels = number_of_wheels

class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

class ElectricCar(ElectricVehicle,Car):
    def __init__(self):
        super().__init__(battery_capacity, make, model, number_of_wheels = 4)

#super-ov miayn ElectricVehicle-i property-nern e jarangum, te Car-ic el karogh e jarangel? 
