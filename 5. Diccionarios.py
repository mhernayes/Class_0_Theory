#In this document will see how to work whit "Dictionarys".

#definir un diccionario

stuff = {"food": 15, "energy": 100, "enemies": 3}

#imprimir un valor del dicionario
print(stuff.get("food"))

#acceder a todos los keys y values del diccionario con la funcion "items"
print(stuff.items())

#acceder a los keys del diccionario
print(stuff.keys())

#remover el ultimo key y value del diccionario
stuff.popitem()
print(stuff)

#para ver el value de una key
print(stuff.setdefault("food"))

#agregar al diccionar una key y value
print(stuff.setdefault("carne, 200"))
print(stuff)

#actualizar un diccionario
new_items = {"rocks": 4, "arrows": 23 }
stuff.update(new_items)
stuff.update(food = 20)
print(stuff)

#agregar items al diccionario
stuff['papel']=42
print(stuff)