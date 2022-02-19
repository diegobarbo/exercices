# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

name = ' Diego Barbosa Silva '
print(name)

print()

name2 = 'John\t Quincy \nAdams'
print(name2)

print()

print(name.lstrip())
print(name.rstrip())
print(name.strip())