# napisati funkciju izbroj, koja određuje broj
# elemenata liste, gde svaki element može da bude podlista ili broj.
# Primer: izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]) = 13

# Write a function named 'count' that determines the number of elements in the list,
# where each element can be a sublist or a number.
# Example: count([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]) should return 13

from functools import reduce

def count(objects:list):
    return reduce(lambda x,y: x + (count(y) if isinstance(y,list) else 1), objects, 0)

print(count([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))