"""
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year #creating three instances "make", "model" and "year" and stored as attributes inside a class

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}") #prints information about the car in the order presribed


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car() #2020 Toyota Corolla ("year", "make", "model")
