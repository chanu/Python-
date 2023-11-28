#OOPS Exercise 1: Create a Class with instance attributes
##Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
#CODE:-
class Vehicle:
 def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)
#OUTPUT:-
# 240 18

#OOPS Exercise-2:Create a Vehicle class without any variables and methods
##CODE:-
class Vehicle:
    pass
#OUTPUT:-NULL
#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
#CODE:---
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
#OUTPUT:-Vehicle Name: School Volvo Speed: 180 Mileage: 12.


# OPPS EXERCISE-4:---------------------------------------------------------------------------------------------------------------
#Given:

#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

#Use the following code for your parent Vehicle class.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

#CODE:-
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
#OUTPUT:-The seating capacity of a School Volvo is 50 passengers.

#OPPS EXERCISE-5:-
#Define a property that must have the same value for every class instance (object)
#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

#Use the following code for this exercise.
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
#CODE:-
#Variables created in .__init__() are called instance variables. An instance variable’s value is specific to a particular instance of the class. For example, in the solution, All Vehicle objects have a name and a max_speed, but the name and max_speed variables’ values will vary depending on the Vehicle instance.

#On the other hand, the class variable is shared between all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().

class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
#OUTPUT:-
#White School Volvo Speed: 180 Mileage: 12
#White Audi Q5 Speed: 240 Mileage: 18

#OPPS EXERCISE-6:------------------------------------------------------------------------------------------------------
#Class Inheritance
#Given:

#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
#CODE:-
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
#OUTPUT:-Total Bus fare is: 5500.0

#OPPS EXERCISE-7:-------------------------------------------------------------------------------------------------------
#Check type of an object
#Write a program to determine which class a given Bus object belongs to.

#Given:

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
#CODE:-
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in type()
print(type(School_bus))

#OUTPUT:-  <class '__main__.Bus'>

#OPPS EXERCISE-8:-------------------------------------------------------------------------------------------------------
#Determine if School_bus is also an instance of the Vehicle class

#Given:

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

#CODE:-
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle))
#OUTPUT:-
# True.
























