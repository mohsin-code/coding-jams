#Polymorphism
class Sea_creatures():      #Parent Class/Super Class
    def types(self, types):
        print("TYPE:    ", types)
    def Colony(self):
        print("Exists in colonies!")
    def Uncolonized(self):
        print("Stays alone!")

class Plants():
    def types(self, type):
        print("TYPE:    ", type)

class Animals():
    def Colony(self):
        print("Graze together!")


obj_Sea = Sea_creatures()
obj_Plants = Plants()
obj_Animals = Animals()

obj_Sea.types("botanical")
obj_Plants.types("massive")

obj_Sea.Colony()
obj_Animals.Colony()



#Polymorphism & Inheritence
class Botanica(Sea_creatures):
    def Colony(self):
        return super().Colony()
    def types(self, Color_code):
        if Color_code == 0:
            print("Colorless")
        elif Color_code == 1:
            print("Black")
        else:
            print("Colorful")


obj_Botanica = Botanica()

color = str(input("Enter the color code of the plant:  "))

obj_Sea.types("Botanical")
obj_Botanica.types(color)

