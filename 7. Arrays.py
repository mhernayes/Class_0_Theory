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
array_view[:] = 6 #reemplazamos todos los elementos por 5 (operador de asignacion)
print(array_view)
print(sorted_array)

#llenar una array 
#metodo por operador de asignacion
array_1 = np.zeros((3,3))
array_1[:] = 2 #reemplazamos todos los elementos por 5 (operador de asignacion)
array_1_1 = array_1 + 5
array_1_2 = array_1 * 3
print(array_1_1)
print(array_1_2)
#metodo con fill
array_1.fill(8) #usamos fill para llenar el array
print(array_1)


#Diferencia de como acceder a las operaciones matematicas.
"""
Ambos métodos son utilizados para calcular la suma de los elementos en un arreglo NumPy array_2. 
La principal diferencia entre ellos es la forma en que se accede al método sum().

En el primer método, np.ndarray.sum(array_2), la función sum() se llama a través de la clase ndarray del módulo NumPy. 
Este método funciona de la misma manera que el método array_2.sum(), ya que ambos devuelven la suma de los elementos del arreglo array_2. 
Sin embargo, la diferencia radica en la forma en que se accede al método sum(). 
Al llamarlo a través de la clase ndarray, se puede usar una sintaxis más explícita para indicar en qué arreglo se debe realizar la suma.

En el segundo método, array_2.sum(), la función sum() se llama directamente en el arreglo array_2. 
Este método es más breve y suele ser el más comúnmente utilizado.

En resumen, la principal diferencia es la forma en que se accede al método sum(), ya sea a través de la clase ndarray o directamente en el arreglo. 
Ambos métodos son igualmente válidos y producirán el mismo resultado para el cálculo de la suma de los elementos del arreglo.

"""

#Operaciones Matematicas y mas con ARRAYS

#creamos un array 
array_2 = np.arange(1,10,1)
print(array_2)
array_2 = array_2.reshape((3,3))
print("El array 2 es:\n", array_2)

#usamos el metodo de numpy para sumar
suma_1_array_2 = np.ndarray.sum(array_2)
suma_1_1_array_2 = np.sum(array_2) #se puede usar la forma corta sin poner ndarray
print(suma_1_array_2)
print(suma_1_1_array_2)

#sumamos sin np
suma_2_array_2 = array_2.sum()
print(suma_2_array_2)

#sumamos el eje 0 - columnas
suma_3_array_2 = array_2.sum(0)
print(suma_3_array_2)

#sumamos el eje 1 - filas
suma_4_array_2 = array_2.sum(1)
print(suma_4_array_2)

#usamos el metodo de numpy para multiplicar
prod_1_array_2 = np.ndarray.prod(array_2)
prod_1_1_array_2 = np.prod(array_2)#se puede usar la forma corta sin poner ndarray
print(prod_1_array_2)
print(prod_1_1_array_2)

#multiplicamos sin np
prod_2_array_2 = array_2.prod()
print(prod_2_array_2)

#multiplicamos el eje 0 - columnas
prod_3_array_2 = array_2.prod(0)
print(prod_3_array_2)

#multiplicamos el eje 1 - filas
prod_4_array_2 = array_2.prod(1)
print(prod_4_array_2)

#el valor medio mean
mean_array_2 = np.ndarray.mean(array_2)
mean_1_array_2 = np.mean(array_2) #se puede usar la forma corta sin poner ndarray
print(mean_array_2)
print(mean_1_array_2)

#el valor minimo min
min_array_2 = np.ndarray.min(array_2)
min_1_array_2 = np.min(array_2) #se puede usar la forma corta sin poner ndarray
print(min_array_2)
print(min_1_array_2)

#el valor minimo max
max_array_2 = np.ndarray.max(array_2)
max_1_array_2 = np.max(array_2) #se puede usar la forma corta sin poner ndarray
print(max_array_2)
print(max_1_array_2)

#la posicion donde se encuentra el valor minimo
argmin_array_2 = np.ndarray.argmin(array_2)
argmin_1_array_2 = np.argmin(array_2) #se puede usar la forma corta sin poner ndarray
print(argmin_array_2)
print(argmin_1_array_2)

#la posicion donde se encuentra el valor maximo
argmax_array_2 = np.ndarray.argmax(array_2)
argmax_1_array_2 = np.argmax(array_2) #se puede usar la forma corta sin poner ndarray
print(argmax_array_2)
print(argmax_1_array_2)

#otra forma de crear el array darle forma al mismo tiempo
array_3 = np.arange(1,10).reshape(3,3)
print(array_3)

#como pasar todo a un array de 1 columna 
array_4 = array_3.reshape(array_3.size)
print(array_4)
print(array_3.size) #para ver el tamaño del array en cantidad de elementos

array_5 = array_3.flatten()
print(array_5)

array_5 = array_3.ravel()
print(array_5)

#intercambiar filas por columnas
array_6_1 = np.swapaxes(array_3, 1,0)
print(array_6_1)

array_6_2 = array_3.transpose(1,0)
print(array_6_2)

#operciones con matrices
my_array_7 = np.zeros((2,3), dtype = np.int64)
my_array_7[:] = 4
my_array_7 = 2 * my_array_7 + 4
print(my_array_7)

#multiplicaicon matricial
mult_array_2 = np.matmul(my_array_7, array_6_1)
print(array_1)
print(array_2)
mult_array_2 = np.matmul(array_1, array_2) #se puede usar la forma corta sin poner ndarray
print(mult_array_2)
