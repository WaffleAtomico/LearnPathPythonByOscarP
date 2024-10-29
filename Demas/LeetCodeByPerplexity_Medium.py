'''
Tienes una lista de puntajes de un juego, donde cada puntaje puede ser positivo o negativo.
 Tu tarea es escribir una función que calcule la suma total de los puntajes, 
 pero con las siguientes reglas:

    Si el puntaje es positivo, se suma normalmente.

    Si el puntaje es negativo, se debe ignorar, a menos que sea el segundo puntaje
      negativo consecutivo, en cuyo caso se suma su valor absoluto.

    Si hay más de dos puntajes negativos consecutivos, solo se sumará el segundo.

'''

from functools import reduce

def sumar_puntos(puntajes: list[int]) -> int:
# Tu código aquí
    negCount = 0
    filteredList = list(filter(lambda x: x if x>0 and negCount==2 else abs(x), puntajes))
    print(filteredList)
    total = reduce((lambda x,y: x+y), filteredList)
    print("Resultado total: ", total)
    # a = sum(lambda x, y: x+y, puntajes)

puntajes = [10, -1, -2, 5, -3, -4, 6, -5]
# puntajes = [10, 5, 2, 6]
sumar_puntos(puntajes)
#Salida esperada
#Suma total: 10 + 5 + 2 + 6 = 23




'''

def sumar_puntos(puntajes: List[int]) -> int:
    negCount = 0  # Contador de puntajes negativos consecutivos
    
    filteredList = list(
        filter(
            lambda x: (
                (negCount := 0) if x > 0 else (negCount := negCount + 1),  # Actualiza negCount
                x if x > 0 and negCount == 2 else abs(x) if negCount == 2 else None  # Lógica de filtrado
            )[1],  # Retorna el segundo elemento de la tupla
            puntajes
        )
    )
    
    return sum(filteredList)

'''