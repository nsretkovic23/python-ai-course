# Koriscenjem programskog jezika Python, napisati funkciju parni, koja listu brojeva transformise u rečnik parnih i neparnih brojeva.
# Primer: parni([1, 7, 2, 4, 5]) = {'Parni': [2, 4], 'Neparni': [1, 7, 5]}

# Using the Python programming language, write a function called 'even', which transforms a list of numbers into a dictionary of even and odd numbers.
# Example: even([1, 7, 2, 4, 5]) = {'Even': [2, 4], 'Odd': [1, 7, 5]}

def even(numbers:list) -> dict:
    # Solved in two ways, first way: using list comprehensions (for even numbers)
    # Second way: using filter (for odd numbers)
    return dict({'Even':[x for x in numbers if x%2 == 0], 'Odd':list(filter(lambda x: x%2 != 0, numbers))})

print(even([1, 7, 2, 4, 5]))

