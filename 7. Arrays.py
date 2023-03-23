#Los arrays estan pensados para guardar un unico tipo de dato.

import numpy as np

# por lo que puedo ver una matriz como esta:
my_array_1 = np.array([[1,2,3],[4,5,6]])
# es lo mismo que escribirla asi:
""" 
[1,2,3]
[4,5,6]
"""
#imprimos el array
print(my_array_1)
# si usamos el metodo shape para ver la cantidad de elementos que contiene cada columna y cada fila
print(my_array_1.shape)

my_array_2 = my_array_1.reshape((3,2))
print(my_array_2)


#usar arange para crear un array
my_array_3 = np.arange(8) #el array va desde 0 hasta 7
print(my_array_3)

my_array_4 = np.arange(2,8) #el array va desde 2 hasta 7
print(my_array_4)

my_array_5 = np.arange(2,8,2) #el array va desde 2 hasta 7 pero incrementa 2
print(my_array_5)

my_array_5 = np.arange(-2,8,2.5) #el array va desde -2 hasta 7 pero incrementa 2,5
print(my_array_5)

#creamos un array todo de 
my_array_6 = np.zeros((2,3))
print(my_array_6)

#creamos un array todo de 1
my_array_7 = np.ones((2,3))
print(my_array_7)

#creamos un array vacio 
my_array_8 = np.empty((2,3))
print(my_array_8)

#creamos un array vacio 
my_array_9 = np.empty((4,3))
print(my_array_9)

#creamos un array con 1 y 0
my_array_10 = np.eye(3, k = 1)
print(my_array_10)

