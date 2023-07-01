# Napisati funkciju izmeni, koja elemente na
# parnim pozicijama uvedava za jedan i od njih kreira podlistu pp, dok elemente na
# neparnim pozicijama umanjuje za 1 i od njih kreira podlistu np. Funkcija vrada rečnik koji
# sadrži liste pp i np.
# Primer: izmeni([8, 6, 3, 1, 1]) = {'pp': [9, 4, 2], 'np': [5, 0]}

# Write a function named 'modify',
# which increments the elements at even positions by one and from them creates a sublist 'pp',
# while it decrements the elements at odd positions by one and from them creates a sublist 'np'.
# The function returns a dictionary which contains the 'pp' and 'np' lists.
# Example: modify([8, 6, 3, 1, 1]) should return {'pp': [9, 4, 2], 'np': [5, 0]}

def modify(numbers:list):
    pp = [numbers[i]+1 for i in range(0, len(numbers)) if i%2 == 0]
    np = [numbers[i]-1 for i in range(0, len(numbers)) if i%2 != 0]
    return {'pp':pp, 'np':np}

print(modify([8, 6, 3, 1, 1]))

