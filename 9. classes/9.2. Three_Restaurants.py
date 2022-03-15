class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name.title()} "
              f"and its cuisine is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"The {self.name} is open!")


menu1 = Restaurant('Fooday', 'Junk food')
menu1.describe_restaurant()

menu2 = Restaurant('Pipo', 'Italian food')
menu2.describe_restaurant()

menu3 = Restaurant("Chicken's place", 'Brazilian food')
menu3.describe_restaurant()