# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
# • Use a for loop to print each food the restaurant offers.
for food in foods:
    print(food)
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# foods[0] = 'bread'
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.
print()
foods = ('soup', 'bbq chicken', 'carrot cake', 'cannoli', 'ice cream')
for food in foods:
    print(food)

