#https://yuminlee2.medium.com/insertion-sort-algorithm-52604aa53ad0
import random, time

def insertion(elementos):
    for amount in range(1, len(elementos)):
        for n in range(amount, 0, -1):
            if elementos[n-1] > elementos[n]:
                aux = elementos[n]
                elementos[n] = elementos[n-1] 
                elementos[n-1] = aux 
            else:
                break
    return elementos

def program():
    inicio = time.time()
    n = 150000
    elementos = [random.randint(0,1000) for _ in range(n)]
    time.sleep(1)
    #Codigo
    elementos = insertion(elementos)
    print(elementos)
    fin = time.time()
    print(f"Tiempo de ejecucion: {fin-inicio}")

# program()