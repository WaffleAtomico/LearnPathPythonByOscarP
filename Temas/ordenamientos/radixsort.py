import random
import time
class Radix:
    def __init__(self, elementos):
        self.elementos = elementos
        
    def radixsortP(self, max):
        print()
        
    def radixsortN(self, max):
        print()
        
    def radixsortABC(self, max):
        print()
    



if __name__ == "__main__":

    n = 15
    elementos = [random.randint(-n,n) for _ in range(n)]
    elementos = [120, 1, 92, 45, 123, 82, 10, 15, 7, -3, -21, 12, 4, 14, 71]

    print(f"Cantidad: {len(elementos)} \n Elementos entregados:  " )

    # {elementos}
    inicio = time.time()

    radixsort = Radix(elementos) 
    elementos = radixsort.radixsortP(elementos, 4)  
    
        
    fin = time.time()    
    print(f"Cantidad: num: {len(elementos)} \n Elementos obtenidos: {elementos} " )
    print(f"Tiempo de ejecucion: {fin-inicio}")
