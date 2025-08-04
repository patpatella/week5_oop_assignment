# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
    
    def introduce(self):
        return f"I am {self.name} from {self.origin}, wielding {self.power}!"

    def defend(self):
        return f"{self.name} uses {self.power} to protect the city!"

# Subclass using inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def defend(self):
        return f"{self.name} flies at {self.flight_speed} km/h and strikes with {self.power}!"

# usage
hero1 = Superhero("The Flash", "Electric Surge", "Neo-Tokyo")
hero2 = FlyingHero("Superwoman", "Wind Cutter", "Cloud Realm", 750)

print(hero1.introduce())      
print(hero2.defend())      

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        return "Driving on the highway 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the clouds ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing the seas 🚤"

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

