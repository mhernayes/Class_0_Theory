"""
Cuando usar listas
Por otro lado, las listas pueden ser fácilmente modificadas, ya que son mutables o dinamicas.

Se puede añadir elementos, eliminarlos, cambiarlos de posición o intercambiar unos por otros.

Las listas son útiles si lo que quieres es que tus datos sean flexibles, que puedan ser modificados cuando sea necesario.

Las listas soportan una variedad de métodos incorporados de Python que llevan a cabo ciertas operaciones sobre ellas, operaciones no soportadas por la tuplas.

Todo ello implica que la longitud, el tamaño de una lista pueda variar durante el ciclo de vida del programa.
"""

#In this document will see how to work whit "Lists".

#definir listas de variables
fruits = ["orange", "apple","grape", "apple", "apple", "apple"]
numbers = [8, 14, "1985", 24.5, "2004"]

#imprimir una lista desde 0 hasta 30 (30 no incluido) de 2 en 2 
numeros = list(range(0, 30, 2))
print(numeros)

#imprimir un elemento de una lista
print(fruits[0])

#imprimir el ultimo elemento de la lista
print(fruits[-1]) 

#agregar al final una variable a la lista
fruits.append("applejuice")
print(fruits)

#agregar un elemento en una posicion determinada
fruits.insert(1, "banana")
print(fruits)

#borrar el ultimo elemento de una lista
fruits.pop()
print(fruits)

#eliminar un elemento de una lista
fruits.pop(1)

#guardar el elemento borrado en una variable
frutas = fruits.pop()

#agregar una lista a otra lista (unir). tambien se pueden unir sumando elementos lista1 + lista2
fruits.extend(numbers)
print(fruits)

#elimar una variable determinada (elimina la primera aparicion del elemento)
fruits.remove("orange")
print(fruits)

#eliminar un campo
fruits.pop(3)
frutas_eliminadas = fruits.pop(3)
print(fruits)

#elimiar el ultimo campo
fruits.pop(-1)
print(fruits)

#ordenar los numeros de una lista
number = [1939, 5, 3, 4, 6, 7, 9, 2, 1]
number.sort()
print(number)

#ordenar de manera temporal
numeros = [101, 10, 2, 1, 4, 5, 6]
print(sorted(numeros))

#ordenar las palabras de una lista
letters = ["a", "c", "b", "e", "d"]
letters.sort()
print(letters)

#chequear variables de una lista
print("orange" in fruits)
print("grape" in fruits)

#chequear y contar variables de una lista
print(fruits.count("apple"))

#obtener la posicion de una variable dentro de una lista
print(fruits.index("grape"))

number = "hola"
number_2 = " como estas?"
number_3 = number + number_2 + " puto"
print(number_3)

print(number + number_2)

#keyword "del" que se puede aplicar a cualquier objeto
del fruits[1]

#invertir la lista
lista11 = ["hola", "chau"]
print(lista11.reverse())
print(lista11.sort(reverse=True))

#ver que cantidad de elemntos tiene una lista
print(len(fruits))

#ver si un elemento esta en una lista
if frutas in fruits:
    print("esta es la fruta")
else:
    print("esta fruta no esta")

#Si una lista esta vacia arroja false, si esta llena arroja true

#recorrer una lista (metodo 1)
fruits = ["orange", "apple","grape", "apple", "apple", "apple"]
print(len(fruits))
for i in range(0, len(fruits)):
    print(fruits[i])

print("\n")

#recorrer una lista (metodo 2)
#los dos puntos representan el valor puede ser inicial o final 
#cuando recorremos de esta forma para imprimir o hacer otra cosa colocamos el "frutas"
for frutas in fruits[0:3]:
    print(frutas)

#funciones con numeros
digitos = [1, 4, 5, 7, 9, 8]
print(min(digitos))
print(max(digitos))
print(sum(digitos))

#porcion de la lista
algunos_digitos = digitos[2:4]
print(algunos_digitos)

#desde el primer elemento hasta el 4
algunos_digitos = digitos[:4] 
print(algunos_digitos)

#desde el elemento 4 hasta el ultimo
algunos_digitos = digitos[4:]
print(algunos_digitos)

#desde el elemento -3 hasta el ultimo
algunos_digitos = digitos[-3:]
print(algunos_digitos)

#copiar una lista y agregar elementos a esa nueva lista
print("\n")
comida = ["milanesa", "papas", "ensalada", "pizza", "helado"]
mi_comida = comida[:]
mi_comida.append("sanguche")
print(comida)
print(mi_comida)

#listas anidadas y como acceder a sus valores
print("\n")
datos_alumnos = [["David", 27], ["Jose", 22], ["Martin", 36]]
print(datos_alumnos[0])
print(type(datos_alumnos))
print(datos_alumnos[0][1])
print(type(datos_alumnos[0][0]))
print(datos_alumnos[0:2])
print(datos_alumnos[-1:])

print("\n")
lista = []
terminado = False

#separar una cadena de caracteres en una lista
cadena_1 = "David Fernandez 12311267A 43527 2 2.1 4.6 3.4"
alumnos = cadena_1.split()
print(alumnos)

while terminado == False:
    numero = (input("ingrese un numero: "))
    if numero.isnumeric() == True:
        lista.append(int(numero))
    else:
        print("no es numero, por favor ingrese un numero")
    if len(lista) == 5:
        terminado = True

print(lista)
print(sorted(lista))
print(max(lista))
print(min(lista))

#convertir una lista en un string
lista10 = [1,2,3,4,5]
string = ''.join(lista10)
print(lista10)

"""COMPRESION DE LISTAS
El método de compresión de listas en Python es una técnica que permite crear una nueva lista a partir de una o varias 
secuencias de elementos existentes, utilizando una sintaxis concisa y legible.
La sintaxis básica de la compresión de listas es la siguiente:

nueva_lista = [expresion for elemento in secuencia]

En esta sintaxis, "expresión" es una expresión que se evalúa para cada elemento en la secuencia, y los resultados se agregan a la "nueva_lista". 
Por ejemplo, si tenemos una lista de números y queremos crear una nueva lista con el doble de cada número, podemos hacer lo siguiente:
"""
numeros = [1, 2, 3, 4, 5]
dobles = [num * 2 for num in numeros]
print(dobles)  # Output: [2, 4, 6, 8, 10]

""" 
También es posible agregar una o varias cláusulas if para filtrar los elementos de la secuencia. 
Por ejemplo, si queremos crear una nueva lista solo con los números pares de la lista original, podemos hacer lo siguiente:
"""
numeros = [1, 2, 3, 4, 5]
pares = [num for num in numeros if num % 2 == 0]
print(pares)  # Output: [2, 4]

"""
La compresión de listas es una forma conveniente y eficiente de crear nuevas listas en Python, especialmente cuando se trabaja con datos de grandes volúmenes. 
Sin embargo, es importante tener en cuenta que su uso excesivo puede hacer que el código sea menos legible y difícil de mantener.
"""

productos = [{"producto_1": 
            {"nombre": "leche",
            "precio": 100,
            }},
        {"producto_2":
            {"nombre": "manteca",
            "precio": 50,
            }}
        ]

lista = [info_productos for producto in productos for info_productos in producto.vlaues() if list(producto.keys())[0] == "producto_1"]
print(lista)

"""
lista = [...]: Esta línea crea una nueva lista llamada lista y la inicializa con los elementos que se generarán en la lista comprehension.

info_productos for producto in productos: Esto establece el primer nivel de iteración en la lista comprension. 
Se recorre cada elemento en la lista productos, y se asigna a la variable producto.

for info_productos in producto.values(): Esta es la segunda cláusula for dentro de la lista comprension. 
Itera sobre los valores de cada diccionario contenido en producto y los asigna a la variable info_productos. 
En otras palabras, se recorren los valores de cada diccionario dentro de la lista productos.

if list(producto.keys())[0] == "producto_1": Esta es una cláusula if que filtra los elementos en función de una condición. 
En este caso, verifica si la primera clave en el diccionario producto es igual a "producto_1". La función list(producto.keys())[0] 
obtiene la lista de claves del diccionario producto y luego selecciona el primer elemento de esa lista.

info_productos: Este es el elemento que se agrega a la lista lista. En cada iteración, se añade el valor actual 
de info_productos a la lista.

En resumen, la lista comprehension recorre la lista productos, luego recorre los valores de cada diccionario dentro 
de productos, y solo agrega a la lista lista los valores que provienen del diccionario cuya clave es "producto_1".
"""