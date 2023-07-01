# Korišcenjem programskog jezika Python, napisati funkciju razlika, koja prihvata dve liste
# (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih
# elemenata iz prve liste, koji se ne nalaze u drugoj listi.
# Primer: razlika([1, 4, 6, "2", "6"], [4, 5, "2"]) = [1, 6, "6"]

# Using the Python programming language, write a function named 'difference',
# which accepts two lists (of any type of data),
# and returns a list composed of all elements from the first list that are not present in the second list.
# Example: difference([1, 4, 6, "2", "6"], [4, 5, "2"]) should return [1, 6, "6"]

def difference(list1:list, list2:list):
    return [x for x in list1 if x not in list2]

print(difference([1, 4, 6, "2", "6"], [4, 5, "2"]))