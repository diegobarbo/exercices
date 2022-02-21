# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ['veggie', 'mushroom', 'pepperoni']

for flavour in pizzas:
    print(flavour)
print()
# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
for flavour in pizzas:
    print(f"I used to love {flavour.title()} pizza, but now Margherita pizza it's my favourite.")
print()
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
print("Pizza it's good, but it's fattening, mainly Pepperoni pizza.")
print("I like Veggie pizza, but I'm not a veggie person.")
print("I really like pizza!")
