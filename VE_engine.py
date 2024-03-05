class Vehicle:
    count = 0

    def __init__(self, make, model, vehicle_count):
        self.make = make
        self.model = model
        self.vehicle_count = vehicle_count

    def increment_vehicle_count(self):
        Vehicle.count += self.vehicle_count  #???????

    def get_vehicle_count(self):
        return self.vehicle_count
    
    def start_engine(self):
        print("Engine started")

    def __repr__(self):
        return f"Vehicle's make is {self.make} and the model is {self.model}. Total number of vehicles is {self.count}."

class Car(Vehicle):
    #def start_engine(self):
    #    print("Car engine started")
    
    def __init__(self, make, model, vehicle_count, number_of_wheels = 4):            #karanq mi masy pokhancenq????
        super().__init__(make, model, vehicle_count)
        self.number_of_wheels = number_of_wheels

    def start_engine(self):
        print("Car engine started")

    def __repr__(self):
        return f"Car's make is {self.make} and the model is {self.model}. It has {self.number_of_wheels} wheels.Total number of vehicles is {self.count}."   #??????

vehicle = Vehicle("Mercedes-Benz","S-class", 4)    
vehicle.start_engine()

car = Car("Toyota", "Camry", 5)
car.start_engine()

vehicle.start_engine()

print(repr(car))
print(repr(vehicle))
