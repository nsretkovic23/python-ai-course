# Napisati funkciju presek, koja prihvata dve liste
# (bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih
# elemenata koji se nalaze u obe liste.
# Primer: presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]) = ["1"]

# Write a function named 'intersection',
# which accepts two lists (of any type of data)
# and returns a list composed of all the elements that are found in both lists.
# Example: presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]) should return ["1"]

def intersection(list1:list, list2:list):
    return [x for x in list1 if x in list2]

print(intersection([5, 4, "1", "8", 3, 7], [1, 9, "1"]))