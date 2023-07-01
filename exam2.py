# Korišdenjem programskog jezika Python, napisati funkciju lista_tipova, koja iz liste koja može
# da sadrži elemente različitog tipa izdvaja vrednosti po tipu i smešta ih u rečnik.
#  Napomena: Naziv tipa može da se preuzme korišćenjem atributa __name__ nad samim tipom podataka.
# Primer: numlista(["Prvi", "Drugi", 2, 4, [3, 5]]) =
#  {'str': ["Prvi", "Drugi"], 'int': [2, 4], 'list': [[3, 5]]}

# Using the Python programming language, write a function named type_list that extracts values
# from a list (which can contain elements of different types) by type and places them in a dictionary.
# Note: The name of the type can be retrieved by using the __name__ attribute on the data type itself
# Example: numlista(["Prvi", "Drugi", 2, 4, [3, 5]]) =
#  {'str': ["Prvi", "Drugi"], 'int': [2, 4], 'list': [[3, 5]]}

def type_list(objects:list):
    types = set({type(x).__name__ for x in objects})
    return {t:list(filter(lambda x: type(x).__name__ == t, objects)) for t in types}

print(type_list(["Prvi", "Drugi", 2, 4, [3, 5]]))