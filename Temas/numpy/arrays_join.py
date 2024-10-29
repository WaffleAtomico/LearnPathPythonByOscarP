import numpy as np

'''Unir 2 arreglos 1D'''
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr) #LOS PONE EN UNO SOLOOO & hace una copia

print("\n-\n")

'''Join two 2-D arrays along rows (axis=1):'''
            #A    |  |  B |  |
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr) 

print("\n-\n")

'''Joining Arrays Using Stack Functions'''
'''Stacking is same as concatenation, the only difference is that stacking is done along a new axis.'''


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr3 = np.array([7, 8, 9])

arr2x1 = np.stack((arr1, arr2), axis=1)
arr1x2x3 = np.stack((arr1, arr2, arr3), axis=1)
print(arr2x1)
print(arr1x2x3)

print("\n-\n")

'''Stacking Along Rows'''
'''NumPy provides a helper function: hstack() to stack along rows.'''
# 1 2 3
# 4 5 6
arr = np.hstack((arr1, arr2))
# Igual a concatenate
print(arr) 
print("\n-\n")


'''Stacking Along Columns'''
# 1 2 3
# 4 5 6
arr = np.vstack((arr1, arr2))

print(arr, end="\n\n-\n\n") 

'''Stacking Along Height (depth)'''
# 1 2 3
# 4 5 6
arr = np.dstack((arr1, arr2))
print(arr, end="\n\n-\n\n") 


'''-------------SPLIT--------------'''
print(f"{'-'*20} SPLIT {'-'*20}")

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
# Si te pasas de valores, entonces genera arreglos de X tipo, supongo que los que tenga el array original
print(newarr, end="\n\n-\n\n")

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)
# Nos da 3 arreglos de 2D
print(newarr, end="\n\n-\n\n")

#Solo parte dentro de la misma dimencion de los elementos


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 2, axis=1)
print(newarr, end="\n\n-\n\n")

#hsplit & hSTACK tienen los mismos principios
#Lo mismo que VSTACK   y    DSTACK, pero con split 
