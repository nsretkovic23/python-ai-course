# Korišcenjem programskog jezika Python, napisati funkciju zbir, koja kreira novu listu čiji su
# elementi zbirovi susednih elementa liste.
# Primer: zbir([1, 2, 3, 4, 5]) = [3, 5, 7, 9]

# Using the Python programming language, write a function named 'neighbour_sum',
# which creates a new list where each element is the sum of neighboring elements from the original list.
# Example: sum([1, 2, 3, 4, 5]) should return [3, 5, 7, 9]

def neighbour_sum(numbers:list):
    return [numbers[i] + numbers[i+1] for i in range(len(numbers) - 1)]

print(neighbour_sum([1, 2, 3, 4, 5]))