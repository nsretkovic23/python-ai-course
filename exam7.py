# Korišcenjem programskog jezika Python, napisati funkciju saberi, koja listu tuple vrednosti
# transformiše u listu brojeva, koji se dobijaju primenom operacije sabiranja.
# Primer: operacija([(1, 4, 6), (2, 4), (4, 1)]) = [11, 6, 5]

# Using the Python programming language, write a function named 'tuples_sum',
# which transforms a list of tuples into a list of numbers,
# obtained by applying the addition operation.
# Example: sum([(1, 4, 6), (2, 4), (4, 1)]) should return [11, 6, 5]

def tuples_sum(tuples:list):
    return [sum(t) for t in tuples]

print(tuples_sum([(1, 4, 6), (2, 4), (4, 1)]))