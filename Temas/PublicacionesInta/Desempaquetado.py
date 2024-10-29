# Se puede desempaquetar elementos de una lista de esta manera normalmente


# Lista
numeros = [1, 2, 3]

# Desempaquetado
a, b, c = numeros

print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3
print('-'*40)

# Pero ahora, podemos ver esta nueva manera

# Lista con más elementos
numeros = [1, 2, 3, 4, 5]

# Desempaquetado con el operador *


a, *resto, b = numeros

print(a)      # Salida: 1
print(resto)  # Salida: [2, 3, 4]
print(b)      # Salida: 5
# Asi podemos agarrar el primer y ultimo elemento, pero almacenando lo del medio
print('-'*40)


def suma(x, y):
    return x + y

numeros = (5, 10,) #Si hay mas valores de los que se espera, no va a permitir insertarlos, va a dar error

# Desempaquetando la tupla al llamar a la función
resultado = suma(*numeros)

print(resultado)  # Salida: 15

print('-'*40)


list1 = [1, 2, 3]
iterador = iter(list1)

# Desempaquetando el iterador en una lista
lista_iteradores = [iterador] * 3

for x in range(0, len(lista_iteradores)+2):
    # print(lista_iteradores[x]) #Esto solo va a dar direcciones de memoria y el tipo
    print("Pasando iterador: ",next(lista_iteradores[0],4)) 
    
    
# print(lista_iteradores)
# Imprimiendo los elementos del primer iterador
# print(next(lista_iteradores[0]))  # Salida: 1
# print(next(lista_iteradores[0]))  # Salida: 2

# print("[0]: ",next(lista_iteradores[0]))

# Todos apuntan al mismo iterador
# print("[1]: ",next(lista_iteradores[1]))  # Salida: 3


'''
next()

Ayuda para mover el indice incial de un arreglo y podemos evitar que haya un overflow asignandole un valor
next([objeto_iterable], [valorlimite])

'''
