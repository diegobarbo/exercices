# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

dinner = ['Chloe', 'Jose', 'Linda', 'Kate', 'Peter', 'Claus']

print("I'm embarrassed! My new dinner table won't arrive in time for our meeting.\nI have to cancel on four of you.")
print()

unlucky_1 = dinner.pop()
print(f"Sorry, {unlucky_1}. No chair for you.")

unlucky_2 = dinner.pop()
print(f"Sorry, {unlucky_2}. No chair for you.")

unlucky_3 = dinner.pop()
print(f"Sorry, {unlucky_3}. No chair for you.")

unlucky_4 = dinner.pop()
print(f"Sorry, {unlucky_4}. No chair for you.")

print()
print(dinner)

print(f"{dinner[0]}, you are still invited!")
print(f"{dinner[1]}, you are my best friend and still invited.")
print()

print(f"{dinner[0]} arrived for dinner!")
del dinner[0]
print(dinner)
print(f"{dinner[0]} arrived for dinner too!")
del dinner[0]
print(dinner)
