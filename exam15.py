# Napisati funkciju izdvoji, koja iz zadate liste čiji su
# elementi liste, izdvaja n-ti element i formira rezultujudu listu, pri čemu je n=0 za prvu
# podlistu i uvedava se sukcesivno za 1. Ukoliko ne postoji n-ti element u listi vrada se 0.
# Primer: izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]) = [5, 9, 0, 12]

# Write a function named 'nth_element',
# which given a list whose elements are lists, extracts the nth element
# and forms a resulting list, where n=0 for the first sublist and increases successively by 1.
# If the nth element does not exist in the list, return 0.
# Example: nth_element([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]) should return [5, 9, 0, 12]

def nth_element(lists:list):
    return [lists[i][i] if i < len(lists[i]) else 0 for i in range(0,len(lists))]

print(nth_element([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))