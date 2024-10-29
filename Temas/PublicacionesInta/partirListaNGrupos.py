# Parte de una lista
list1 = ['Sun','Flowers','Peoples','Animales','Day','Night','impar']

print(iter(list1))              #La hacemos iterable
print(*[iter(list1)] * 2)       #De hacerse una tupla, hacemos particiones...
# * de lo que hay todo todo en la tupla (Ya que tiene [] que lo encapsula ) vamos a hacer grupos de tuplas de 2
print(zip(*[iter(list1)] * 2))

partition = list(zip(*[iter(list1)] * 2))
print(partition)



tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = (7,8,9)

untionTuples = zip(tupla1,tupla2,tupla3)
lista_tuplas = list(untionTuples)
print(lista_tuplas)
lista_listas_de_tuplas = [list(x) for x in lista_tuplas]
print(lista_listas_de_tuplas)

'''
ZIP sirve para unir tuplas

Pero todas las uniones van a ser por su indice mas chico
en este ejemplo, haciamos que 1, 4, 7 estuvieran en una misma
ya que todos esos inician en 0

'''