"""
Uso de funciones
En Python, una función es un bloque de código reutilizable que realiza una tarea específica. 
Puedes definir tus propias funciones para agrupar una serie de instrucciones relacionadas y 
luego llamarlas desde cualquier parte de tu programa.

Para definir una función en Python, se utiliza la palabra clave def, seguida del nombre de 
la función y paréntesis que pueden contener argumentos si es necesario. 
Aquí tienes un ejemplo básico de una función que imprime "¡Hola, mundo!":
"""
def saludar():
    print("¡Hola, mundo!")

# Llamando a la función
saludar()


import math
# Utilizando una función del módulo math
resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0


"""Retorno de una variable
En este caso, la función suma() recibe dos argumentos (a y b), los suma y devuelve 
el resultado utilizando la palabra clave return. Al llamar a la función y almacenar 
su resultado en la variable resultado_suma, luego podemos imprimir ese valor.
"""
def suma(a, b):
    resultado = a + b
    return resultado

# Llamando a la función y almacenando el resultado en una variable
resultado_suma = suma(3, 4)
print(resultado_suma)  # Imprime 7


"""
En este caso, la función saludar() tiene un argumento llamado nombre. 
Cuando llamamos a la función y le pasamos la variable nombre_usuario como argumento, 
el valor de esa variable se utiliza dentro de la función para imprimir el saludo adecuado.
"""
def saludar(nombre):
    print("¡Hola, " + nombre + "!")

# Llamando a la función y pasando una variable como argumento
nombre_usuario = "Juan"
saludar(nombre_usuario)  # Imprime "¡Hola, Juan!"


"""
Recursividad
En este caso, la función factorial() se llama a sí misma dentro del caso recursivo 
return n * factorial(n-1), multiplicando el número n por el factorial del número anterior n-1. 
El caso base if n == 0 detiene la recursión cuando n llega a cero, retornando 1.
"""
def factorial(n):
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n-1)

# Llamando a la función recursiva
resultado = factorial(5)
print(resultado)  # Imprime 120


"""
Parametros opcionales
Parámetros opcionales: Puedes definir parámetros opcionales en una función asignándoles 
un valor predeterminado. Estos parámetros pueden ser omitidos al llamar a la función, 
y en su lugar se utilizará el valor predeterminado.
"""
def saludar(nombre, saludo="¡Hola!"):
    print(saludo + " " + nombre)

# Llamando a la función sin especificar el saludo
saludar("Juan")  # Imprime "¡Hola! Juan"

# Llamando a la función especificando un saludo personalizado
saludar("María", "¡Buen día!")  # Imprime "¡Buen día! María"


"""
Alcance de variables
Alcance de variables: Las variables definidas dentro de una función tienen un alcance 
local, lo que significa que solo son accesibles dentro de esa función. 
Por otro lado, las variables definidas fuera de una función tienen un alcance global 
y pueden ser accedidas desde cualquier parte del programa.
"""

"""
Funciones anidadas
En Python, puedes definir funciones dentro de otras funciones. 
Estas funciones se llaman funciones anidadas o funciones internas. 
Las funciones anidadas pueden acceder a las variables locales de la función externa.
En este caso, la función interior() se define dentro de la función exterior(). 
La función exterior() imprime "Función externa" y luego llama a interior(), 
que a su vez imprime "Función interna".
"""
def exterior():
    def interior():
        print("Función interna")

    print("Función externa")
    interior()

exterior()


"""
Argumentos de longitud variable: 
Puedes definir funciones que acepten un número variable de argumentos utilizando 
los parámetros "*args" y "**kwargs". 
El parámetro "*args" permite pasar un número arbitrario de argumentos posicionales (tuplas)
El parámetro "**kwargs" permite pasar un número arbitrario de argumentos clave-valor (diccionarios).
"""
def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)  # Imprime 15

def imprimir_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamando a la función con diferentes argumentos clave-valor
imprimir_informacion(nombre="Juan", edad=25, ciudad="México")


"""
Funciones lambda
En Python, puedes utilizar las funciones lambda para crear funciones anónimas de una 
sola expresión. Estas funciones son útiles cuando necesitas una función rápida y sencilla.
"""
cuadrado = lambda x: x**2
resultado = cuadrado(5)
print(resultado)  # Imprime 25

"""
En este ejemplo, tenemos una lista de diccionarios que representan personas con sus respectivos 
nombres y edades. Utilizamos una función lambda llamada comparar_edad para definir un 
criterio de filtro. La función lambda toma cada elemento de la lista y verifica si la edad 
de la persona es mayor o igual a 18.
Luego, utilizamos la función filter() junto con la función lambda para filtrar las personas 
mayores de edad. El resultado se convierte en una lista y se almacena en la variable 
personas_mayores. Finalmente, imprimimos personas_mayores, que contendrá solo las personas 
cuya edad es mayor o igual a 18.
Recuerda que las funciones lambda son útiles cuando necesitas definir funciones simples y 
específicas en el momento, sin tener que crear una función separada con la sintaxis def. 
Puedes utilizar funciones lambda en diversas situaciones, como operaciones de filtrado, 
mapeo y reducción de datos. 
"""
comparar_edad = lambda persona: persona["edad"] >= 18
personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 16},
    {"nombre": "Pedro", "edad": 20},
    {"nombre": "Laura", "edad": 14}
]
personas_mayores = list(filter(comparar_edad, personas))
print(personas_mayores)


"""
Decoradores
Los decoradores son funciones que envuelven otras funciones para extender o modificar 
su comportamiento. Proporcionan una forma elegante de modificar funciones existentes 
sin modificar su código original. Los decoradores se definen utilizando la sintaxis 
del símbolo "@" antes de la función a decorar. 
En este caso, el decorador decorador() envuelve la función funcion_decorada() y agrega 
algunas instrucciones antes y después de llamar a la función.
"""
def decorador(func):
    def wrapper():
        print("Antes de llamar a la función")
        func()
        print("Después de llamar a la función")
    return wrapper

@decorador
def funcion_decorada():
    print("Función decorada")

funcion_decorada()


"""
Documentación de funciones
Es buena práctica incluir documentación en tus funciones para describir su propósito, 
los parámetros que aceptan y el valor de retorno. Puedes agregar una cadena de 
documentación (docstring) dentro de la función utilizando comillas triples.
En este caso, la cadena de documentación describe el propósito de la función y el parámetro nombre. 
Luego, se accede a la cadena de documentación utilizando el atributo __doc__ de la función.
"""
def saludar(nombre):
    """
    Esta función imprime un saludo personalizado.
    :param nombre: El nombre de la persona a saludar.
    """
    print("¡Hola, " + nombre + "!")

ayuda = saludar.__doc__
print(ayuda)

"""
La función filter() en Python es una función incorporada que permite filtrar elementos 
de una secuencia (como una lista, tupla o conjunto) según una función de filtro dada. 
Toma dos argumentos: la función de filtro y la secuencia que se desea filtrar.

En este ejemplo, se define una función es_par() que toma un número como argumento y 
devuelve True si el número es par y False si es impar. Luego, la función filter() se 
utiliza para filtrar los elementos de la lista numeros y mantener solo los números pares. 
Al convertir el objeto filter a una lista usando list(), obtenemos [2, 4, 6, 8, 10], que 
son los números pares de la lista original.
"""
def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(es_par, numeros))
print(numeros_pares)  # Imprime: [2, 4, 6, 8, 10]

""" 
Parámetros posicionales: 
Son parámetros que se pasan a una función en el orden en 
que se declaran. Estos parámetros se asignan a los argumentos en función de su posición. 
Es decir, el primer argumento se asigna al primer parámetro posicional, el segundo argumento 
se asigna al segundo parámetro posicional, y así sucesivamente. Los parámetros posicionales 
son obligatorios, lo que significa que deben proporcionarse al llamar a la función.

En este caso, se pasan los valores 2 y 3 como argumentos, que se asignan a los parámetros 
posicionales a y b. La función suma los valores y devuelve el resultado.

"""
def suma(a, b):
    return a + b

resultado = suma(2, 3)

""" 
Parámetros opcionales (con valores predeterminados): 
Son parámetros que tienen un valor asignado por defecto. 
Estos parámetros no requieren que se les proporcione un argumento al llamar a la función. 
Si no se proporciona un argumento, se utilizará el valor predeterminado.

En este caso, "Alice" se asigna al parámetro nombre, mientras que no se proporciona 
un argumento para edad. Como edad tiene un valor predeterminado de 30, se utilizará ese 
valor al llamar a la función.

También es posible proporcionar un argumento para un parámetro opcional si se desea 
cambiar su valor predeterminado:
En este caso, "Bob" se asigna al parámetro nombre y 25 se asigna al parámetro edad, 
reemplazando el valor predeterminado.

"""

def saludar(nombre, edad=30):
    print(f"Hola, soy {nombre} y tengo {edad} años.")

saludar("Alice")

saludar("Bob", 25)

"""
Parámetros de palabra clave: Son parámetros que se pasan a una función utilizando su 
nombre (palabra clave) en lugar de su posición. Estos parámetros son opcionales y permiten 
especificar los valores de los parámetros de manera explícita, sin depender del orden.

En este caso, se pasan los valores Alice y 25 como argumentos utilizando los nombres de 
los parámetros correspondientes. Los parámetros de palabra clave ofrecen mayor claridad y 
flexibilidad al llamar a la función, ya que no se necesita recordar el orden de los argumentos.

"""

def saludar(nombre, edad):
    print(f"Hola, soy {nombre} y tengo {edad} años.")

saludar(nombre="Alice", edad=25)




