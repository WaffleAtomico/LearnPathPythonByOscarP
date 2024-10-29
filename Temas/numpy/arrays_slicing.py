import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print("1 al 5: ",arr[1:5])
print("Desde el 4ta: ",arr[4:])
print("4ta para atras: ", arr[:4])
print("Con indices negativos ", arr[-3:-1])
print("Step de 2 en 2: ",arr[1:5:2]) 
print("Saltos de 2 en 2, desde 0 ",arr[::2])
print("Saltos de -2 en -2, desde 0 ",arr[::-2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#Si bien se ve como un arreglo, seccionamos y podemos usar rangos por cada coma que hay
#Atras de la coma, filas, luego de la coma, las COLUMNAS
print("Doble arreglo: ",arr[1, 1:4])
print("Doble arreglo 2 [0:2, 2]",arr[0:2, 2]) 
print("Doble rango arreglo ",arr[0:2, 1:4])  

'''
DATA TYPES IN NUMPY


Below is a list of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer    (No negativos)
    f - float
    c - complex float       (Numeros imaginarios como 3+4i)
    m - timedelta           (Un objeto que representa una duración o diferencia entre dos 
                             fechas/tiempos. Se utiliza para realizar operaciones de tiempo, 
                             como sumar o restar intervalos a objetos de fecha/hora)
    M - datetime            
    O - object              (Es un tipo genérico que puede contener cualquier tipo de dato.
                             En programación orientada a objetos, todos los tipos de datos 
                             son considerados objetos.)
    S - string
    U - unicode string      (Similar a una cadena normal, pero diseñada para manejar caracteres
                             de múltiples lenguajes y símbolos. )
    V - fixed chunk of memory for other type ( void )
                            (Se refiere a un bloque fijo de memoria que puede ser utilizado para 
                             almacenar datos de cualquier tipo. Este concepto es común en lenguajes
                             como C/C++, donde se requiere un manejo más directo de la memoria.
                             Estas variables son fundamentales en la programación y permiten manejar
                             diferentes tipos de datos según las necesidades específicas del desarrollo.)
'''


arr = np.array([1, 2, 3, 4], dtype='S')
print("Tipo de dato ",arr)
arr = np.array([1, 2, 3, 4], dtype='i4') #4 bytes integer:
print("Imaginario i4 ",arr)


arr = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 10, 11, 12]])

'''
La Coma ,
En la sintaxis de slicing de NumPy, la coma , 
se utiliza para separar los índices de las diferentes dimensiones del arreglo. En este caso:

    Antes de la coma: Se refiere a las filas del arreglo.
    Después de la coma: Se refiere a las columnas del arreglo.

'''
# [:]   #1ero
# [::2] #2do
# Final: [:, ::2]
print(arr[:, ::2])