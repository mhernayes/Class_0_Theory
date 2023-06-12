"""
SETS:

En Python, un set es una colección desordenada y mutable de elementos únicos. 
- Los elementos no llevan un indice asociado.
- No se pueden reasignar valores a los elementos de un set
- Se pueden borrar ni añadir elementos
- Los elementos son unicos y no hay duplicados
La estructura de un set se define mediante llaves ({}) que contienen elementos separados por comas. 
Por ejemplo:
"""
my_set = {1, 2, 3, 4}

#También es posible crear un set vacío usando la función set():
empty_set = set()

#convertir una lista a una set
lista = [1,2,3,4]
my_set = set(lista)
print(my_set)

"""
Los sets tienen algunas operaciones y métodos útiles, tales como:

add(elemento): agrega un elemento al set
remove(elemento): elimina un elemento del set y lanza un error si el elemento no se encuentra en el set
discard(elemento): elimina un elemento del set si está presente en él, y no hace nada en caso contrario
union(set): devuelve un nuevo set que contiene todos los elementos de ambos sets
intersection(set): devuelve un nuevo set que contiene solo los elementos comunes a ambos sets. Se puede utilizar el simbolo "&"
difference(set): devuelve un nuevo set que contiene solo los elementos que están en el primer set pero no en el segundo set
issubset(set): devuelve True si el set es un subconjunto del set dado, y False en caso contrario
symetric_difference(set): se eliminan los que se repiten entre los 2 sets
"""
#Por ejemplo, para agregar un elemento al set my_set, se puede usar el método add:
my_set.add(5)

#Luego, se puede usar el método remove para eliminar el elemento 2 del set:
my_set.remove(2)

#Para crear un nuevo set que contenga todos los elementos de my_set y other_set, se puede usar el método union:
other_set = {3, 4, 5, 6}

#El resultado será un nuevo set que contiene los elementos {1, 3, 4, 5, 6}.
new_set = my_set.union(other_set)

frutas = {"manzana", "pera", "banana"}
print("manzana" in frutas) #True
print("tomate" in frutas) #False
