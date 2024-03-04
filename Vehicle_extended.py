class Vehicle():
    count = 0

    def __init__(self, make, model, vehicle_count):
        self.make = make
        self.model = model
        self.vehicle_count = vehicle_count

    def increment_vehicle_count(self):
        Vehicle.count += self.vehicle_count

    def get_vehicle_count(self):
        return self.vehicle_count

    def __repr__(self):
        return f"Vehicle's make is {self.make} and the model is {self.model}. Total number of vehicles is {self.count}."

class Car(Vehicle):
    def __init__(self, make, model, vehicle_count, number_of_wheels = 4):
        super().__init__(make, model, vehicle_count)
        self.number_of_wheels = number_of_wheels

    def __repr__(self):
        return f"Car's make is {self.make} and the model is {self.model}. It has {self.number_of_wheels} wheels.Total number of vehicles is {self.count}."

vehicle = Vehicle("Mercedes-Benz","S-class", 4)    
vehicle.increment_vehicle_count()

car = Car("Toyota", "Camry", 5)
car.increment_vehicle_count()

vehicle = Vehicle("Mercedes-Benz","S-class", 3)
vehicle.increment_vehicle_count()
print(vehicle.get_vehicle_count())

print(repr(car))
print(repr(vehicle))