"""
ARRAYS:
Los arrays estan pensados para guardar un unico tipo de dato.
"""

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

my_array_2_bis = my_array_1.reshape((-1,1))
print("Imprimimos el array my_array_2_bis: ", my_array_2_bis)
"""
Con el -1 lo que le indicas es que el tamaño de esa dimensión 
lo calcule en función de las otra dimensiones y la cantidad de los datos. 
Es decir, si tienes un array de una dimensión y 6 datos, 
te lo convierte a un array bidimensional con 1 columna y 6 filas.
Si pusieras -1,2. Te lo convierte a un bidimensional de 2 columnas y 3 filas
"""
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

#creamos un array con 1 y 0 (Matriz identidad)
"""¿Qué es una matriz identidad? Una matriz identidad es una matriz cuadrada con todos 
los elementos de la diagonal principal iguales a uno y los otros elementos iguales a cero.
"""
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
array_2 = np.arange(1,10,1) #entre parentesis va el valor inicial, final y el paso. si no se pone el inicio ni el paso, el numero inicial es 0 y el paso es 1
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

#sumamos los elementos de ambos arrays elemento por elemento
#crear un array con numeros aleatorios del 1 al 100 con tamaño 15
array_1_aleatorio = np.random.randint(1,100, size=15)
print(array_1_aleatorio)

#creamos otro array con numeros aleatorios del 0 al 3 con tamaño 15
array_2_decimal = np.random.uniform(0,3, size=15)
print(array_2_decimal)

array_resultado_suma = []
print(array_1_aleatorio)
print(array_2_decimal)
resultado = 0
for i in range(0, len(array_1_aleatorio)):
    resultado = array_1_aleatorio[i] + array_2_decimal[i]
    array_resultado_suma.append(resultado)
print("El resultado de la suma es: ", array_resultado_suma)

#se puede sumar asi 2 arrays pero con menos decimales
array_resultado_suma_2 = array_1_aleatorio + array_2_decimal
print("El resultado de la suma es: ", array_resultado_suma_2)

#se puede sumar asi 2 arrays pero con menos decimales
array_resultado_suma_3 = np.sum([array_1_aleatorio, array_2_decimal], axis=0)
print("El resultado de la suma es: ", array_resultado_suma_3)

#restamos los elementos de los arrays
array_resultado_resta = []
print(array_1_aleatorio)
print(array_2)
resultado = 0
for i in range(0, len(array_1_aleatorio)):
    resultado = array_1_aleatorio[i] - array_2_decimal[i]
    array_resultado_resta.append(resultado)
print("El resultado de la resta es: ", array_resultado_resta)

#se puede restar asi 2 arrays pero con menos decimales
array_resultado_resta_2 = array_1_aleatorio - array_2_decimal
print("El resultado de la resta es: ", array_resultado_resta_2)

#se puede restar asi 2 arrays pero con menos decimales
array_resultado_resta_3 = np.subtract(array_1_aleatorio, array_2_decimal)
print("El resultado de la resta es: ", array_resultado_resta_3)

"""
En la biblioteca NumPy de Python, tanto numpy.prod como numpy.multiply son funciones que se utilizan
para realizar operaciones de multiplicación en matrices y arreglos. 
Sin embargo, hay algunas diferencias clave entre las dos funciones.

numpy.prod es una función que se utiliza para calcular el producto de todos los elementos 
en un arreglo o matriz. Por ejemplo, si tenemos un arreglo arr = [1, 2, 3, 4], 
entonces numpy.prod(arr) devolverá 24, que es el producto de todos los elementos en arr.

Por otro lado, numpy.multiply se utiliza para multiplicar dos arreglos o matrices elemento
por elemento. Es decir, si tenemos dos arreglos arr1 = [1, 2, 3] y arr2 = [4, 5, 6], 
entonces numpy.multiply(arr1, arr2) devolverá [4, 10, 18], que es el resultado de multiplicar 
cada elemento en arr1 con su correspondiente elemento en arr2.

En resumen, la principal diferencia entre numpy.prod y numpy.multiply es que numpy.prod 
se utiliza para calcular el producto de todos los elementos en un arreglo o matriz, 
mientras que numpy.multiply se utiliza para multiplicar dos arreglos o matrices elemento 
por elemento.
"""
#multiplicamos los elementos de los arrays
array_resultado_prod = []
print(array_1_aleatorio)
print(array_2_decimal)
resultado = 0
for i in range(0, len(array_1_aleatorio)):
    resultado = array_1_aleatorio[i] * array_2_decimal[i]
    array_resultado_prod.append(resultado)
print("El resultado de la multiplicacion es: ", array_resultado_prod)

#se puede multiplicar asi 2 arrays pero con menos decimales
array_resultado_prod_2 = array_1_aleatorio * array_2_decimal
print("El resultado de la multiplicacion es: ", array_resultado_prod_2)

#se puede multiplicar asi 2 arrays pero con menos decimales
array_resultado_prod_3 = np.prod([array_1_aleatorio, array_2_decimal], axis=0)
print("El resultado de la multiplicacion es: ", array_resultado_prod_3)

#se puede multiplicar asi 2 arrays pero con menos decimales
array_resultado_prod_4 = np.multiply(array_1_aleatorio, array_2_decimal)
print("El resultado de la multiplicacion es: ", array_resultado_prod_4)

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

#el valor del medio o mediana
median_array_2 = np.median(array_2) #se puede usar la forma corta sin poner ndarray
print("Calculo de mediana", median_array_2)

#el valor minimo max
max_array_2 = np.ndarray.max(array_2)
max_1_array_2 = np.max(array_2) #se puede usar la forma corta sin poner ndarray
print(max_array_2)
print(max_1_array_2)

desviacion_standard = np.std(array_2)
print("La desviacion estandar es", desviacion_standard)

promedio = np.average(array_2)
print("El array_2 es:", array_2)
print("El promedio del array_2 es:", promedio)

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

#comparamos 2 arrays y vemos que valores estan repetidos
print("---------------")
elemento_comunes_1 = np.intersect1d(array_1, array_2)
print(array_1)
print(array_2)
print(elemento_comunes_1)

#comparamos 2 arrays y vemos cuales son las posiciones de los valores repetidos
print("---------------")
elemento_comunes_1 = np.intersect1d(array_1, array_2, return_indices=True)
print(array_1)
print(array_2)
print(elemento_comunes_1)

#crear un array con numeros aleatorios del 1 al 100 con tamaño 15
array_1 = np.random.randint(1,100, size=15)
print(array_1)

#creamos otro array con numeros aleatorios del 0 al 1 con tamaño 15
array_2 = np.random.uniform(0,1, size=15)
print(array_2)


"""CONCATENAR ARRAYS"""
print("--------------")
len = int(input("Por favor ingrese la longitud del array:\n"))
my_array_1_1 = np.zeros(len)
my_array_1_1.fill(1)
print(my_array_1)

print("--------------")
my_array_1_1 = my_array_1_1.reshape((3,2))
print(my_array_1_1)

print("--------------")
my_array_2_2 = np.eye(3, k = 1)
print(my_array_2_2)

#para concatenar 2 arrays deben tener el mismo tamaño excepto en la dimension correspondiente al axis
print("--------------")
my_array_3_3 = np.concatenate((my_array_1_1,my_array_2_2), axis=1)
print(my_array_3_3)

#otra forma de hacer es con stack. La diferencia entre stack y concatenate es que con stack se hace
#a lo largo de un nuevo eje

print("--------------")
my_array_4_4 = np.vstack((my_array_1_1,my_array_2_2))
print(my_array_4_4)

print("--------------")
my_array_5_5 = np.hstack((my_array_1_1,my_array_2_2))
print(my_array_5_5)

#verificamos cuantas filas tiene el array para luego recorrerlo
ventas = np.array([
    ["2022-01-01", 100, "ropa"],
    ["2022-01-02", 200, "alimentos"],
    ["2022-01-03", 150, "ropa"],
    ["2022-02-01", 120, "alimentos"],
    ["2022-02-02", 180, "electronicos"],
    ["2022-02-03", 200, "alimentos"],
    ["2022-03-01", 90, "ropa"],
    ["2022-03-02", 110, "electronicos"],
    ["2022-03-03", 100, "alimentos"],
])
num_filas = ventas.shape[0]
print(num_filas)

#accedemos a la columnas o filas
fechas = ventas[:,0]
venta_dia = ventas[:,1]
categoria = ventas[:,2]
print(ventas[1:4, 0:2]) #accedemos a las filas de 1 al 4 de las columnas 0 al 2
print(ventas[1:4:2, 0:2:2]) #los ultimos ":" representan el paso que se acceden los slices del array
print(ventas[:, ::-1]) #los primeros ":" respresntan todas las filas, el segundo ":" representa toas las columnas y ":-1" es el paso inverso de las columnas
#quedarme con una columna del array ventas
print(ventas[:, [0,2]]) #se muestan todas las filas pero solamente las columnas 0 y 2
fecha = np.array([venta[0] for venta in ventas])
print(fecha)

#quedarme con una caracter del array fecha
año = np.array([fecha[0:4] for fecha in fechas])
print(año)

# Crear un array con información de las películas (duracion, categoría, año de estreno)
peliculas = np.array([[120, 'Acción', 2010],
                      [90, 'Comedia', 2015],
                      [150, 'Acción', 2012],
                      [110, 'Drama', 2013],
                      [100, 'Comedia', 2018],
                      [130, 'Drama', 2010]])

# Obtener los índices de las películas de cada categoría
accion_indices = np.where(peliculas[:, 1] == 'Acción')[0]
comedia_indices = np.where(peliculas[:, 1] == 'Comedia')[0]
drama_indices = np.where(peliculas[:, 1] == 'Drama')[0]

# Crear arrays separados para cada categoría
peliculas_accion = peliculas[accion_indices]
peliculas_comedia = peliculas[comedia_indices]
peliculas_drama = peliculas[drama_indices]

# Imprimir los arrays separados
print('Películas de Acción:')
print(peliculas_accion)
print('')

print('Películas de Comedia:')
print(peliculas_comedia)
print('')

print('Películas de Drama:')
print(peliculas_drama)
print('')

#borramos la fila inicial que era igual 0
peliculas_accion = np.delete(peliculas_accion, 0, axis = 0)
print(peliculas_accion)

#cambiar el tipo de dato de un array
a = np.array([1,2,3,4])
a = a[:,i].astype(int)
a = a[:,i].astype(str)
a = a[:,i].astype(float)

"""
USO DEL METODO NP.UNIQUE Y NP.COUNT_NONZER
"""

#unique para verificar cuales son los elementos unicos
peliculas = np.array([
    [120, 'Acción', 2010],
    [90, 'Comedia', 2015],
    [150, 'Acción', 2012],
    [110, 'Drama', 2013],
    [100, 'Comedia', 2018],
    [130, 'Comedia', 2010]
    ])

generos, conteos = np.unique(peliculas[:, 1], return_counts = True) #cuenta los generos unicos que estan en la columna 1 y los suma la cantidad de veces que se repiten y los agrega en conteos
print(generos)
print(conteos)

#ordena los indices de los elementos en forma descendente
conteos_desc = np.argsort(conteos)[::-1] #[::-1] sigfinica todas las filas y todas las columnas de forma inversa

#calculamos el genero mas popular
genero_popular = generos[conteos_desc[0]]
print("El genero mas popular es", genero_popular)

#agrupamos las peliculas por decadas
decadas = np.unique(peliculas[:, 2].astype(int) // 10 * 10) #nos quedamos con los años, 
                                                            #lo convertimos a un entero
                                                            #hacemos la division floor (1985 // 10 = 198)
                                                            #multiplicamos * 10 para obtener la decada
print(decadas)
#creamos una lista vacia 
conteos_decadas = []

#la función np.count_nonzero se utiliza para contar el número de elementos diferentes de cero en un array NumPy.
#contamos las peliculas de cada decada
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:, 2].astype(int) >= decada) & (peliculas[:, 2].astype(int) < (decada + 10))) #guardammos en una variable la decada
    conteos_decadas.append(conteo) #agregamos la variable conteo que tiene guardada la decada a la lista conteo_decadas
    print("En la decada", decada, "se crearon", conteo, "peliculas")
    
"HISTOGRAMA"

"""
La función np.histogram() de la librería NumPy permite generar un histograma a partir de un conjunto 
de datos numéricos. El primer argumento de esta función es el conjunto de datos que se va a 
analizar, y el segundo argumento (opcional) es el número de bins (contenedores) en los que se 
dividirá el rango de los datos para construir el histograma.

En el código que mencionas, se está aplicando la función np.histogram() al arreglo array_años. 
Además, se está proporcionando un arreglo bin_array como segundo argumento, lo que indica que se desea definir explícitamente los límites de los bins en los que se dividirá el rango de los datos.
En otras palabras, bin_array es un arreglo que especifica los valores mínimos y máximos de cada bin. 
Por ejemplo, si bin_array tiene la forma [0, 10, 20, 30, 40], esto significa que se desea dividir 
el rango de los datos en 4 bins: uno para los valores entre 0 y 10, otro para los valores 
entre 10 y 20, y así sucesivamente.

La función np.histogram() devuelve dos valores: el primer valor es un arreglo con la frecuencia 
de aparición de los valores en cada bin, y el segundo valor es un arreglo con los límites de los bins.
Por lo tanto, en el código que mencionas, la variable array_histograma contendrá el arreglo 
de frecuencias de aparición de los valores de array_años en cada bin definido por bin_array, 
y la variable bin_array contendrá los límites de los bins especificados.

IMPORTANTE!!

El tamaño del arreglo bin_array determina el número de bins en los que se dividirá el rango de los datos, 
NO el número de elementos que se van a analizar.

Por ejemplo: Si se desea dividir el rango de los valores en 12 bins, uno para cada mes, entonces 
el arreglo bin_meses debe tener una longitud de 13, de modo que haya 12 intervalos 
entre los 13 valores de bin_meses.
"""
#definimos un array con las decadas 
bin_array = np.arange(1980, 2040, 10)

#nos quedamos con los años 
array_años = peliculas[:, 3]

#utilizamos el metodo histogram para contar la cantidad de peliculas por año.
array_histograma, bin_array = np.histogram(array_años, bin_array)

# Imprimimos los resultados
for i in range(len(array_histograma)):
    print("Década {}: {}".format(bin_array[i], array_histograma[i]))


"MASCARAS BOOLEANAS"

mi_array = np.array([0,1,2,3,4,5,6,7,8,9])
otro_array = mi_array > 5
print(otro_array) #imprime un array booloeano con los datos mayores a 5
print(mi_array[mi_array>5]) #imprime un array con los datos de mi_array mayor a 3