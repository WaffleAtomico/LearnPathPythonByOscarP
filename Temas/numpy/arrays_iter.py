

'''Normalmente podemos iterar los arreglos como normalmente lo hariamos'''

import numpy as np


'''Iterating Arrays Using nditer()'''

'''
The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
It solves some basic issues which we face in iteration, lets go through it with examples. 
'''
#Array 3D
arr = np.array([ [[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x, end=", ") 

print("\n-\n")


'''Iterating Array With Different Data Types'''

'''
We can use op_dtypes argument and pass it the expected datatype to change
the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array)
so it needs some other space to perform this action, that extra space is called buffer, 
and in order to enable it in nditer() we pass flags=['buffered'].
'''
'''
Necesita espacio adicional para almacenar los datos convertidos. 
Este espacio adicional es conocido como buffer.
'''
arr = np.array([1, 2, 3])
# le indicas a nditer que debe habilitar el uso de un buffer
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']): #Tipo de Variable
  print(x) 
  
print("\n-\n")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# Itera por el arreglo escalar saltando un elemento
print(arr[:, ::2])
# Recorre todas las columnas, y en las filas hace saltos de 2
for x in np.nditer(arr[:, ::2]):
  print(x, end=", ") 
print("\n-\n")

'''Enumerated Iteration Using ndenumerate()'''


arr = np.array([1, 2, 3])
print(np.ndenumerate(arr))
for idx, x in np.ndenumerate(arr):
  print(idx, x) 
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
  print(type(idx), type(x)) # Se puede parcear a int
print("\n-\n")



