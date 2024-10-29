#https://runestone.academy/ns/books/published/pythoned/SortSearch/ElOrdenamientoPorSeleccion.html
#Ordenando buscando el mayor, se puede ir por el menor igualmente, pero asignando a la posicion inicial
#Moraleja: No te compliques con la ultima posicion, mejor con la mas chica
import random, time

def selection(elementos):
    for amount in range(len(elementos)):
        max = 0
        for n in range(len(elementos) - amount):
            if elementos[n] > elementos[max]:
                max = n
        aux = elementos[(len(elementos)-1) -amount] #Maximo normal va hacia el cache
        elementos[(len(elementos)-1) -amount] = elementos[max] #El verdadero maximo es elementos[posicion del numero maxima]
        elementos[max] = aux   #Posicion del maximo va hacia tiene el valor del auxiliar
    return elementos

inicio = time.time()
n = 100
elementos = [random.randint(-500,500) for _ in range(n)]
time.sleep(1)
#Codigo

elementos = selection(elementos)

print(elementos)
fin = time.time()
print(f"Tiempo de ejecucion: {fin-inicio}")