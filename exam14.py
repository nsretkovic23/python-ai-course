# Napisati funkciju unija, koja prihvata dve liste
# (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih
# elemenata obe liste bez ponavljanja.
# Primer: unija([5, 4, "1", "8", 7], [1, 9, "1"]) = [5, 4, "1", "8", 7, 9, 1]

# Write a function named 'union',
# which accepts two lists (of any type of data)
# and returns a list composed of all the elements from both lists, with no repetitions.
# Example: union([5, 4, "1", "8", 7], [1, 9, "1"]) should return [5, 4, "1", "8", 7, 9, 1]

def union(list1:list, list2:list):
    return list(set(list1+list2))

print(union([5, 4, "1", "8", 7], [1, 9, "1"]))