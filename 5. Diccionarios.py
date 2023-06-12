#In this document will see how to work with "Dictionarys".

#definir un diccionario
stuff = {"food": 15, "energy": 100, "enemies": 3}

#imprimir un valor del dicionario. Se podria hace print (stuff["food"]), pero si "food" no se encuentra en el diccionario daria un error
print(stuff.get("food"))
print(stuff["food"])

#cambiar el valor de una clave de un diccionario
print(stuff)
stuff["food"] = 20
print(stuff)

#acceder a todos los keys y values del diccionario con la funcion "items"
print(stuff.items())

#acceder a los keys del diccionario
print(stuff.keys())

#acceder a los values del diccionario
print(stuff.values())

#remover o eliminar un item
#stuff.pop("clave")

##remover o eliminar un item
#del stuff["clave"]

#remover o eliminar todos los items
#stuff.clear()

#remover el ultimo key y value del diccionario
stuff.popitem()
print(stuff)

#para ver el value de una key
print(stuff.setdefault("food"))

#agregar al diccionar una key y value
print(stuff.setdefault("carne, 200"))
print(stuff)
stuff["pera"] = 15
print("El diccionario actualizado es", stuff)

#actualizar un diccionario
new_items = {"rocks": 4, "arrows": 23 }
stuff.update(new_items) #se agrega la informacion del diccionario new_items al diccionario stuff
stuff.update(food = 20) #se actualiza el valor de la clave food
print(stuff)

#agregar items al diccionario
stuff['papel'] = 42
print(stuff)

#convertir una lista de tuplas en diccionarios
#si hay 2 tuplas con la misma clave, solo se conservara la ultima tupla
lista = [("fruta", "pera"), ("casa", "departamento"), ("auto", "toyota")]
lista_dict = dict(lista)
print(lista_dict)

#utilizar la funcion zip para unir 2 listas y transformarlas en clave valor (ambas listas deben tener la misma longitud)
alumnos = ["martin", "mauro", "ricardo"]
notas = [8, 9, 10]
my_dict = dict(zip(alumnos, notas))
print(my_dict)
print(type(my_dict))

#convertir un set de tuplas en diccionarios
#si hay 2 tuplas con la misma clave, solo se conservara la ultima tupla
my_set = {("fruta", "pera"), ("casa", "departamento"), ("auto", "toyota"), ("auto", "toyota")}
my_set_dict = dict(my_set)
print(my_set_dict)

for key, value in my_set_dict.items():
    print("La clave es:", key)
    print("El valor es:", value)

#para acceder las claves se puede hacer de la siguiente forma - EXPLICITO
for keys in my_set_dict.keys():
    print("La clave es:", keys)

#para acceder las claves se puede hacer de la siguiente forma - IMPLICITO
for keys in my_set_dict:
    print("La clave es:", keys)

#imprimirlos ordenados
#para acceder las claves se puede hacer de la siguiente forma - EXPLICITO
for keys in sorted(my_set_dict.keys()):
    print("La clave es:", keys)

#imprimir los valores unicos
#para acceder las claves se puede hacer de la siguiente forma - EXPLICITO
for value in set(my_set_dict.values()):
    print("Los valores son:", value)

#anidamientos de diccionarios
stuff_1 = [{"food": 15, "energy": 100, "enemies": 3}, {"food": 15, "energy": 100, "enemies": 3}]
print(stuff_1[0]["food"])

#utilizar compresion de listas en diccionarios
programadores = {
    "Juan": ["Python", "C++"],
    "Sara": ["C++", "Rust"],
    "Eduardo": ["Solidity", "Fortran"],
    "Felipe": ["Python", "Fortran", "R"]
}

for nombre, lenguaje in programadores.items(): #recorremos todos los key y values del diccionarios programadores con el metodo items()
    print(lenguaje[0])
    
lenguajes = [lenguaje for programador in programadores.values() for lenguaje in programador] #utilizamos la compresion de listas
print(lenguajes)

programadores_2 = {
    "Juan": {
        "Python": 9, 
        "C++": 8,      
        },
    "Sara": {
        "C++": 7, 
        "Rust": 10,
        },
    "Eduardo": {
        "Solidity": 4, 
        "Fortran": 9,
        },
    "Felipe": {
        "Python": 8, 
        "Fortran": 5, 
    }
}

#notas = for nombre, lenguaje in programadores.values() for lenguaje in programador


