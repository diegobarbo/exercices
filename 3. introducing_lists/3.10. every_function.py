# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

languages = ['english', 'portuguese', 'french']

# Finding the Length of a List
print(len(languages))
print()

# Printing a List in Reverse Order (reverte a ordem original da lista e a modifica permanentemente)
languages.reverse()
print(languages)
print()

# Sorting a List Temporarily with the sorted() Function
# (organiza a lista em ordem alfabética sem modifica-la permanentemente)
# (aceita o argumento "reverse=True" se precisar inverter a ordem alfabética)
print(sorted(languages))
print()
print(sorted(languages, reverse=True))
print()

# Sorting a List Permanently with the sort() Method
# (organiza em ordem alfabética e modifica permanentemente)
# (aceita o argumento "reverse=True" se precisar inverter a ordem alfabética)
languages.sort()
print(languages)
print()

# Removing an Item by Value
languages.remove('french')
print(languages)
print()

# Popping Items from any Position in a List
languages.pop(0)
print(languages)

# Removing an Item Using the del Statement
del languages[0]
print(languages)

# Inserting Elements into a List
languages.insert(0, 'japanese')
print(languages)
print()

# Appending Elements to the End of a List
languages.append('spanish')
print(languages)
