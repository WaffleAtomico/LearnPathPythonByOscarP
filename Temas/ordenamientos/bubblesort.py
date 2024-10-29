#https://medium.com/karuna-sehgal/an-introduction-to-bubble-sort-d85273acfcd8
import random, time
#Naco y estupido tenia que ser
def bubblesort(elementos):
    for _ in range(len(elementos)):
        for n in range(1, len(elementos) ):
            if elementos[n] < elementos[n-1]:
                aux = elementos[n]
                elementos[n] = elementos[n-1] 
                elementos[n-1] = aux 
    return elementos

def betterBubbleSort(elementos):
    for _ in elementos:
        for n in range(len(elementos)-1):
            if elementos[n] > elementos[n+1]:
                elementos[n], elementos[n+1] = elementos[n+1], elementos[n]
    return elementos


inicio = time.time()
elementos = [120, 1, 92, 45, 123, 82, 10, 15, 7, -3, -21, 12, 4, 14, 71]
n = 150
# elementos = [random.randint(0,1000) for _ in range(n)]
time.sleep(1)
elementos = bubblesort(elementos)
print(elementos)
fin = time.time()
print(f"Tiempo de ejecucion: {fin-inicio}")
