''' tuplas '''
print('''Las tuplas al contrario que las listas que usan corchetes, utilizan parentesis para su sintaxis''')
mitupla = ('bruno',8,12,1987)
# imprimir por indice
print ('- Imprimimos la tupla:',mitupla)
print ('- Imprimimos posicion de la tupla:',mitupla[0])
# convertir una tupla en lista
milista = list(mitupla)
print ('- Imprimimos la tupla convertida en lista con lista():',milista)
# convertir lista en una tupla
lista = ['curro', 'tocho', 'freya']
tupla = tuple(lista)
print('- Imprimimos la lista:', lista)
print ('- Imprimimos la lista convertida en tupla con tuple():', lista)
# Comprovar si algo esta en la tupla si esta true si no esta false
print('- Comprovamos si juan esta en la tupla:')
print ('juan' in mitupla)
# saber cuantos elementos hay en la tupla
print('- Comprovamos cuantas veces aparece bruno en la tupla con count():')
print (mitupla.count('bruno'))
# saber la longitud de la tupla
print('- Comprovamos la longitud de la tupla con len():')
print (len(mitupla))

# Tuplas unitarias siempre acaban con una coma si no no son unitarias
tupla_unitaria = ('hola mundo',)
print('- Imprimimos la tupla unitaria que acaba con una coma(tupla de un unico elemento): ', tupla_unitaria)

# Desempaquetar una tupla (asignar a variables los valores de la tupla)
nombre, dia,mes,agno = mitupla
print('- Desempaquetamos la tupla: (nombre, dia,mes,agno = mitupla):')
print (f'· Mi nombre es {nombre} naci el dia {dia} el mes {mes} del año {agno}')

# buscar objetos con el metodo index
print('- Buscamos objetos con el metodo index: (mitupla.index(8))')
print(mitupla)
print (mitupla.index(8))

# buscar por indice
print('- Buscamos por indice que sera 8 y posicion desde donde empezar la busqueda 0:(mitupla.index(8,0)) ')
print(mitupla)
print (mitupla.index(8,0)) # primero valor a buscar y segundo el indice desde cual empezar a buscar

# iterar en las tuplas con for
print('- Iteramos con un for la tupla:')
for i in mitupla:
    print (i)

# anidar tuplas
print('''- Anidamos una tupla y sacamos el indice [1][0]: ('bruno', (8,12), 1987)''')
tupla_1 = ('bruno', (8,12), 1987)
print (tupla_1[1][0])

# Operaciones con tuplas
print('- Operamos con las tuplas sumandolas: (mitupla + tupla_1) - (tupla_1*2)')
print('- Suma:',mitupla+tupla_1)
print('- Multiplicación:',tupla_1*2)

# Eliminamos una tupla
del mitupla
print('Eliminamos la tupla:',mitupla)