# napisati funkciju razlika, koja kreira novu listu čiji
# su elementi razlika susednih elementa liste.
# Primer: razlika([8, 5, 3, 1, 1]) = [3, 2, 2, 0]

# Write a function named 'difference',
# which creates a new list where each element represents the difference
# between neighboring elements from the original list.
# Example: difference([8, 5, 3, 1, 1]) should return [3, 2, 2, 0]

from functools import reduce

# Practicing reduce:
def difference(numbers:list):
    return [reduce(lambda x,y: x-y, numbers[i:i+2]) for i in range(0,len(numbers)-1)]

# Simple:
def difference2(numbers:list):
    return [numbers[i]-numbers[i+1] for i in range(0, len(numbers) - 1)]

print(difference([8, 5, 3, 1, 1]))