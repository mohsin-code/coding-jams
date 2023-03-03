class Vehicle:
    def __init__(self, speed, mile):
        self.max_speed = speed
        self.mileage = mile

Ford = Vehicle(100, 25000)
print(Ford.max_speed, Ford.mileage)