# 3-11. Intentional Error: If you haven’t received an index error in one of your
# programs yet, try to make one happen. Change an index in one of your pro-
# grams to produce an index error. Make sure you correct the error before clos-
# ing the program.

dinner = ['Chloe', 'Jose', 'Linda', 'Kate', 'Peter', 'Claus']
# IndexError : list index out of range

try:
    print(dinner[6])
except:
    print('the list index goes from 0 to 5.')
finally:
    print(dinner[5])
