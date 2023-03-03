class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def type_of_bus(self, bus):
        print("Type:  ", type(bus))

School_bus = Bus("School Volvo", 12, 50)
School_bus.type_of_bus(School_bus)