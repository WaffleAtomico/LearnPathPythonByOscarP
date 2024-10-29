import numpy as np

'''1D a 2D'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3) # 4 columnas de 3 elementos c/u

print(newarr) 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# Solo puedes usar multiplos de preferencia, si o si debe de ser justo
newarr = arr.reshape(2, 6) 

print(newarr)
 
'''1D a 3D'''
print("\n-\n")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2) #2 arreglos de 3 filas y 3 columnas

print(newarr) 
'''Es una copia o es una vista? Es una vista'''
print("\n-\n")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

print("\n-\n")
'''No se la dimension'''
'''
Escribir -1 ayuda a saber la dimension
Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
                    #2,2,-1
newarr = arr.reshape(1, 1, -1)

print(newarr) 
print(newarr.shape)
print("\n-\n")

'''Flettering'''
'''Flattening array means converting a multidimensional array into a 1D array.'''

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr) 
print(type(newarr))
print(type(newarr.tolist()))
print("\n-\n")

'''Ejercicio'''

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(6)
print(newarr)