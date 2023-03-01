class Vehicle:
    _name = "Toyota"
    
    def __init__(self):
        self.__type = "Car"
    
    def get(self):
        return self.__type
        
    def set(self, type):
        self.__type = type
        

veh = Vehicle()
print("Type: ", veh.get())

veh.set("Truck")
print("Type: ", veh.get())

print("Mangled Type: ", veh._Vehicle__type)
print("Protected Name: ", veh._name)
