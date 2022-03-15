# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.


class User:

    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.nationality = nationality.title()

    def describe_user(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Age:", self.age)
        print("Nationality:", self.nationality)

    def greet_user(self):
        print(f"Hello, my dear {self.first_name}.")


paul = User('paul', 'silva', 20, 'italy')
paul.describe_user()
paul.greet_user()
