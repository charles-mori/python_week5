# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass with inheritance and encapsulation
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.__flight_speed = flight_speed  # Encapsulation

    def fly(self):
        print(f"{self.name} flies through {self.city} at {self.__flight_speed} km/h!")

    # Getter for encapsulated variable
    def get_flight_speed(self):
        return self.__flight_speed

#testing out the class

hero1 = Superhero("ShadowStrike", "Invisibility", "Metroville")
hero1.introduce()
hero1.use_power()

hero2 = FlyingHero("SkyBlaze", "Fire Manipulation", "SkyCity", 500)
hero2.introduce()
hero2.use_power()
hero2.fly()
print(f"Flight Speed: {hero2.get_flight_speed()} km/h")