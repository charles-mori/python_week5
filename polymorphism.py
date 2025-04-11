class Vehicle:
    def move(self):
        print("This vehicle moves... somehow.")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

#testing 

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
