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

#podemos asignar valores al array
my_array_10[my_array_10 == 0] = 2
my_array_10[my_array_10 < 2] = 4
print(my_array_10)
my_array_10[2] = 3 #se asigna el valor a la fila 2
print(my_array_10)

#se asigna el valor la fila 0 hasta la 2
my_array_10[:2] = 5 
print(my_array_10)

#se asigna el valor a la fila 1 hasta la ultima
my_array_10[1:] = 7 
print(my_array_10)

#reemplazamos desde la fila 1 hasta el final y la columna 2 hasta el final por un 2
my_array_11 = np.eye(3, k = 1)
my_array_11[1:, 2:] = 2
print(my_array_11)

#ordenamos el array
sorted_array = np.sort(my_array_11)
print(sorted_array)

#ordenamos el array por ejes "Y"
sorted_array = np.sort(my_array_11, axis = 0) #el eje 0 es el vertical
print(sorted_array)

#ordenamos el array por ejes "X"
sorted_array = np.sort(my_array_11, axis = -1) #el eje 0 es el horizontal
print(sorted_array)

#copiar arrays con view afecta el original
array_view = sorted_array.view()
array_view[:] = 5 #reemplazamos todos los elementos por 5
print(array_view)
print(sorted_array)

#copiar arrays con copy NO afecta el original
array_view = sorted_array.copy()
array_view[:] = 6 #reemplazamos todos los elementos por 5
print(array_view)
print(sorted_array)