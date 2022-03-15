# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} "
              f"and its cuisine is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"The {self.name} is open!")

restaurant = Restaurant('Colosso', 'italian')
print(restaurant.name)
print(restaurant.cuisine_type)
print()
restaurant.describe_restaurant()
print()
restaurant.open_restaurant()

