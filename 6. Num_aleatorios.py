#In this document will see how to work whit "Random Numbers".

import random

"""
Para generar números aleatorios en Python de valor entero, se suele utilizar la función randint(). 
La función randint(a, b) devuelve un número entero comprendido entre a y b (ambos inclusive) de forma aleatoria. 
Ejemplos útiles de esta función: determinar quién comienza una partida (jugador/PC); simular el dado del parchís, etc:
"""
# ¿Quién comienza?

comienza = random.randint(0, 1)
if comienza == 0:
    print('Comienza el jugador')
else:
    print('Comienza el PC')


# Número aleatorio
numero = random.randint(1, 6)

"""
La función randrange(a, b, salto) genera números enteros aleatorios comprendidos entre a y b separados entre sí con un salto. 
Por ejemplo, randrange(5, 27, 4) obtendría un valor aleatorio de entre los siguientes posibles: 5, 9, 13, 17, 21, 25.
"""
for i in range(10):
    print(random.randrange(5, 27, 4))

"""
La función random() devuelve un float comprendido entre [0.0 y 1.0)
"""
for i in range(5):
    print(random.random())

"""
La función uniform(a, b) devuelve un float aleatorio comprendido entre a y b (ambos inclusive).
"""
for i in range(5):
    print(random.uniform(100, 200))

"""
choice()
La función choice(sec) devuelve un elemento aleatorio de una secuencia. 
Es muy útil cuando hay que elegir al azar un elemento de entre un conjunto.
"""
frutas = ['peras', 'manzanas', 'plátanos', 'ciruelas']
for i in range(3):
    print(random.choice(frutas))

"""
La funcion choice tambien se puede utilizar con un diccionario y toma el valor de un item.
Los items deben ser numeros y comenzar en 0.
"""
#si tomamos un diccionario, el mismo debe empezar en 0 que funcione de forma aleatoria
fruits = {0: "pera", 1: "fruta"}
frutas_aleatorias = fruits
print(random.choice(frutas_aleatorias))

"""
La función shuffle(sec) modifica el orden de los elementos de una lista. 
Esta función se asemeja a la acción de mezclar una baraja.
"""
baraja = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
for i in range(3):
    random.shuffle(baraja)
    print(baraja)

"""
La última función que veremos es sample(sec, num). Esta función devuelve num elementos aleatorios de la secuencia sec. 
Siguiendo con el ejemplo de la baraja, sería similar a la acción de repartir num cartas a un jugador.
"""

baraja = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
random.sample(baraja, 5)
