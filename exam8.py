# Napisati funkciju izmeni, koja svaki n-ti element
# liste zamenjuje brojem koji predstavlja sumu svih elemenata originalne liste, od prvog, do
# n-tog elementa.
# Primer: izmeni([1, 2, 4, 7, 9]) = [1, 3, 7, 14, 23]

# Write a function named 'sum_latest',
# which replaces every nth element of the list with a number that represents the sum of all original list elements,
# from the first to the nth element.
# Example: sum_latest([1, 2, 4, 7, 9]) should return [1, 3, 7, 14, 23]

def sum_latest(numbers:list):
    return [sum(numbers[:i]) for i in range(1,len(numbers) + 1)]

print(sum_latest([1, 2, 4, 7, 9]))