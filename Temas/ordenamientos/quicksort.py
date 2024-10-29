import time
from numpy import random
from collections import Counter

'''
Se rompio, ya no jala
'''

def separar(pivote, values):
    return_values = [] 
    # print(f"pivote actual: {pivote}, longitud del arreglo entregado: {values}, Son {len(values)} valores")
    if(len(values) == 1):
        return_values.append(values)
        return return_values[0]
    else:
        mayores = []
        menores = []
        for n in values: #Obtenemos los numeros solamente
            if pivote > n:
                menores.append(n)
            elif pivote < n:
                mayores.append(n)
                
        if len(menores) > 0:
            min_pivote = menores[len(menores)//2]
            return_values.append(separar(min_pivote, menores))

        return_values.append(pivote)
        
        if len(mayores) > 0:
            max_pivote = mayores[len(mayores)//2]
            return_values.append(separar(max_pivote, mayores))
        return return_values #Significa que tengo elementos aun o mas de 1, ya que si tenia 1 no podria entrar


def quicksort1(pivote, values):
    if len(values) == 1:
        return values
    menores = []
    mayores = []
    iguales = []
    for x in values:
        if x < pivote:
            menores.append(x)
        elif x > pivote:
            mayores.append(x)
        else:
            iguales.append(x)
    values.clear()
    if len(menores) > 0:
        values.extend(quicksort1(menores[len(menores)//2] , menores))
    values.extend(iguales)
    if len(mayores) > 0:
        values.extend(quicksort1(mayores[len(mayores)//2], mayores))
    return values
        
n = 15000
# elementos = [random.randint(-n,n) for _ in range(n)]
elementos = list(random.randint(n, size=(n)))
# elementos = [120, 1, 92, 45, 123, 82, 10, 15,1,1, 7, -3, -21, 12, 4, 14, 71]

#Codigo
pivote = elementos[len(elementos)//2]
print(f"Elementos entregados:  num: {len(elementos)} " )
# print(f"Elementos repetidos {Counter(elementos)}")
# elementos = separar(pivote, elementos)
inicio = time.time()
elementos = quicksort1(elementos[len(elementos)//2], elementos)
fin = time.time()
print(f"Elementos obtenidos: {elementos} num: {len(elementos)} " )
# {elementos}
print(f"Tiempo de ejecucion: {fin-inicio}")





''' Problema, no devuelve la misma cantidad entregada


def separar(pivote, values):
    return_values = [] 
    # print(f"pivote actual: {pivote}, longitud del arreglo entregado: {values}, Son {len(values)} valores")
    if(len(values) == 1):
        return_values += values
        return return_values
    else:
        mayores = []
        menores = []
        for n in values: #Obtenemos los numeros solamente
            if pivote > n:
                menores.append(n)
            elif pivote < n:
                mayores.append(n)
                
        if len(menores) > 0:
            min_pivote = menores[int(len(menores)/2)]
            return_values += separar(min_pivote, menores)

        return_values += [pivote]
        
        if len(mayores) > 0:
            max_pivote = mayores[int(len(mayores)/2)]
            return_values += separar(max_pivote, mayores)
        return return_values #Significa que tengo elementos aun o mas de 1, ya que si tenia 1 no podria entrar


'''