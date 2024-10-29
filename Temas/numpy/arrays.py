#Esta libreria estara centrada en el manejo de numeros y cosas matematicas
def mostrar(arr):
    print(arr)
    print(type(arr))
    print("Dimensiones del arreglo: ",arr.ndim)

import numpy as np

#Investigar sobre scapy pyPI
# Investigar sobre decordaroes y metaprogramacion



arr = np.array(12)
mostrar(arr)

arr = np.array([1,2,3,4,5]) #Puede usarse a partir de tuplas y listas
mostrar(arr)


arr = np.array([[1, 2, 3], [4, 5, 6]])
mostrar(arr)

arr = np.array([ [ [1, 2, 3], [4, 5, 6] ],  [[1, 2, 3], [4, 5, 6]] ])
mostrar(arr)


arr = np.array([1, 2, 3, 4], ndmin=5)
mostrar(arr)

                 # |
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1]) 

#                                  |
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) # 6


print('Last element from 2nd dim: ', arr[1, -1]) 




