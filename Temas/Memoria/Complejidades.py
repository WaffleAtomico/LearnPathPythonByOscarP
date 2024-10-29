# O(1): Ya que no cambia con el tamaño de la entrada.
def obtener_primer_elemento(lista):
    return lista[0]


# Complejidad O(log n) - Logarítmica: Ya que La complejidad logarítmica se observa en algoritmos 
# que dividen el problema en partes más pequeñas.
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# la memoria utilizada se reduce a la mitad en cada iteración.


# Complejidad O(n) - Lineal: La complejidad lineal ocurre cuando el uso de memoria
# crece proporcionalmente al tamaño de la entrada

def contar_elementos(lista):
    contador = 0
    for elemento in lista:
        contador += 1
    return contador

#Complejidad O(n^2): Ya que usa bloques anidados
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Aquí, el uso de memoria crece cuadráticamente con respecto al tamaño de lista. 


# Complejidad O(2^n) - Exponencial: Ya que usa todas las combinaciones posibles
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# El uso de memoria se duplica con cada incremento en n. 



#Complejidad O(n!) - Factorial
# se ve en problemas como la generación de todas las permutaciones de un conjunto. 

def permutaciones(lista):
    import itertools
    return list(itertools.permutations(lista))

# El número total de permutaciones crece factorialmente con respecto al número de elementos en lista.