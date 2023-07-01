# napisati funkciju prosek, koja za svaki element
# prosleđene liste, koja se sastoji isključivo od podlisti, vrada aritmetičku sredinu svih njenih
# vrednosti.
# Primer: prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]) =
#  [3.25, 4.75, 4.0, 5.0]

# Write a function named 'average',
# which for each element of the passed list (which consists exclusively of sublists),
# returns the arithmetic mean of all its values.
# Example: average([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]) should return [3.25, 4.75, 4.0, 5.0]

def average(numberLists:list):
    return [sum(l)/len(l) for l in numberLists]

print(average([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))