# Korišcenjem programskog jezika Python, napisati funkciju brojel, koja broji koliko
# elemenata ima svaka podlista liste koja joj je prosleđena. Ukoliko elemenat liste nije
# podlista funkcija vrada -1.
# Primer: brojel([1, 2], [3, 4, 5], 'el', ['1', 1]) = [2, 3, -1, 2]

# Using the Python programming language, write a function named 'sublist_len',
# which counts the number of elements in each sublist of the provided list.
# If an element of the list is not a list, the function should return -1.
# Example: sublist_len([[1, 2], [3, 4, 5], 'el', ['1', 1]]) should return [2, 3, -1, 2]

# Solved with AI's tip to use isinstance, primary idea was to use type(element).__name__ == 'list'
def sublist_len(objects:list):
    return [len(x) if isinstance(x, list) else -1 for x in objects]

def sublist_len2(objects:list):
    return [len(x) if type(x).__name__ == 'list' else -1 for x in objects]

def sublist_len3(objects:list):
    return list(map(lambda x: len(x) if isinstance(x, list) else -1, objects))

print(sublist_len([[1, 2], [3, 4, 5], 'el', ['1', 1]]))
print(sublist_len2([[1, 2], [3, 4, 5], 'el', ['1', 1]]))
print(sublist_len3([[1, 2], [3, 4, 5], 'el', ['1', 1]]))
