import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

#Imprime todos los lugares en donde hay coincidencias
x = np.where(arr == 4)
print(x, end="\n\n-\n\n")
#Si no existe un valor retorna el arreglo normal
x = np.where(arr == 41)
print(x, end="\n\n-\n\n")
#Si los numeros son par
x = np.where(arr%2 == 0)
print(x, end="\n\n-\n\n")
#Impares
x = np.where(arr%2 == 1)
print(x, end="\n\n-\n\n")

'''BUSQUEDA BINARIAAAAAAA'''
# Se presupone que esta ordenados los numeros
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7) 

print(x) 
print("Val: ",arr[x], end="\n\n-\n\n")

#Para devolver el valor pero
'''
The method starts the search from the right and returns the first index where the number 7
is no longer less than the next value.
'''
x = np.searchsorted(arr, 7, side='right') 
print(x) 
print("Val: ",arr[x], end="\n\n-\n\n") #El 2 ya no es mayor que el 7 que estamos buscando

#Buscar en donde deberian ser insertados nuevos numeros

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x, end="\n\n-\n\n") 
# en el 1, ya que es menor al 3, en el 2 ya que es menor al 5 y en el 3 ya que es menor al 7


'''-------------SORT--------------'''
print(f"{'-'*20} SORT {'-'*20}")

arr = np.array([3, 2, 0, 1])

print(np.sort(arr), end="\n\n-\n\n")

# Note: This method returns a copy of the array, leaving the original array unchanged.

'''Ordena alfabeticamente'''
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr), end="\n\n-\n\n") 


'''Arreglo booleano tmb'''
arr = np.array([True, False, True])

print(np.sort(arr), end="\n\n-\n\n") 

'''2D array'''

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr), end="\n\n-\n\n") 
#Ordena cada uno por separado

# Si quiziera ordenar todos, tendria que 
# hacerlo de 1
# ordenarlo
# Y hacerlo uno de 2x3 en este caso


'''-------------Filter--------------'''
print(f"{'-'*20} Filter {'-'*20}")
# In NumPy, you filter an array using a boolean index list.

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr, end="\n\n-\n\n")

# Se puede crear una lista de filto, recorriendo los valores y agregando a una lista
# Si se cumplen las caracteristicas, se asigna la posicion en true, si no, en false

'''Creating Filter Directly From Array'''
arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42 #Esto en python normal, no se puede, es propiedad de los arreglos np

newarr = arr[filter_arr]

print(filter_arr)
print(newarr, end="\n\n-\n\n")

