# Blake Martin
# This program is intended to


# create vehicle class
class Vehicle:
    def __init__(self, type):
        self.type = type

# creating child class for Vehicle


class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)  # super class called to inherit all properties from parent
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# getting input from user
v_type = input("Vehicle type: ")
v_year = input("Year of vehicle: ")
v_make = input("Make of vehicle: ")
v_model = input("Model of vehicle: ")
v_doors = input("Number of doors (2 or 4): ")
v_roof = input("Type of roof (solid or sun): ")

# calling constructors from child class
A = Automobile(v_type, v_year, v_make, v_model, v_doors, v_roof)

# printing answers given by user
print("Vehicle type: "+A.type)
print("Year: " + A.year)
print("Make: " + A.make)
print("Model: " + A.model)
print("Doors: " + A.doors)
print("Roof type: " + A.roof)
