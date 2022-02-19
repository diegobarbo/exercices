# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list

dinner = ['Jose', 'Linda', 'Peter']

print(f"Good news, {dinner}! I've found a bigger table for us to dinner. I will invite more guests.")

dinner.insert(0, 'Chloe')
dinner.insert(2, 'Kate')
dinner.append('Claus')
print(f"The list of guests now will be: {dinner}.")
print()
print(f"Dear {dinner[0]}, dinner should be at 8 o'clock PM.")
print(f"Dear {dinner[1]}, dinner should be at 8 o'clock PM.")
print(f"Dear {dinner[2]}, dinner should be at 8 o'clock PM.")
print(f"Dear {dinner[3]}, dinner should be at 8 o'clock PM.")
print(f"Dear {dinner[4]}, dinner should be at 8 o'clock PM.")
print(f"Dear {dinner[5]}, dinner should be at 8 o'clock PM.")