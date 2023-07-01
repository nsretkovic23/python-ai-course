# Korišcenjem programskog jezika Python, napisati funkciju uredi, koja svaki od prvih N
# elemenata uvedava za definisanu vrednost a preostale umanjuje za definisanu vrednost.
# Funkciji se prosledjuje lista koja sadrži samo numericke vrednosti i vrednost koja treba da
# se uvecava, odnosno umanjuje.
# Primer: uredi([1, 2, 3, 4, 5], 3, 1) = [2, 3, 4, 3, 4]

# Using the Python programming language, write a function named 'increment_decrement',
# which increments each of the first N elements by a defined value,
# and decreases the remaining elements by that same value.
# The function is passed a list that contains only numeric values, value of N and an increment/decrement value.
# Example: increment_decrement([1, 2, 3, 4, 5], 3, 1) should return [2, 3, 4, 3, 4]"

def increment_decrement(numbers, n, value):
    # :n - n here is exclusive, while in n: n is inclusive as starting position
    return list(x + value for x in numbers[:n]) + list(x - value for x in numbers[n:])

print(increment_decrement([1, 2, 3, 4, 5], 3, 1))