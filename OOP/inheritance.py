# Exercise 1
class Vehicle:
    color = "White"

    def __init__(self, name, speed, mile, capacity):
        self.name = name
        self.max_speed = speed
        self.mileage = mile
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

    def fare(self):
        return 1.1 * super().fare() 

# Exercise 2
class Car(Vehicle):
    pass
        
# Exercise 3
Volvo = Bus("Volvo", 120, 25000, 50)
print(Volvo.color + " " + Volvo.name + " " + str(Volvo.max_speed) + " km/h " + str(Volvo.mileage) + " miles")

# Exercise 4
print(Volvo.seating_capacity())

# Exercise 5
Audi = Car("Audi", 240, 18000, 20)
print(Audi.color + " " + Audi.name + " " + str(Audi.max_speed) + " km/h " + str(Audi.mileage) + " miles")

# Exercise 6
print("Total Bus Fare: " + str(Volvo.fare()))

# Exercise 7
print("Volvo belongs to: " + str(type(Volvo)))

# Exercise 8
print("Volvo is also an instance of Vehilce: " + str(isinstance(Volvo, Vehicle)))