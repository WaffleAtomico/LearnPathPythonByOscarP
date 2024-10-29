import random, time

#Usa recursividad
def merge(left, right):
        resp = []
        i = j = 0 # mejora recomendada
        l_left = len(left) #Mejora de eficiencia de accesos
        l_right = len(right)
        # while len(left) != 0 and len(right) != 0: #Se pregunta antes la longitud en vez de en cada if
        while i < l_left and j < l_right:
            # print("L: ",left[0])
            # print("r: ",right[0])
            if left[i] <= right[j]:
                resp.append(left[i])
                i += 1 #Usar un .pop() consume mas memoria, es mejor usar un contador para la velocidad
            else:
                resp.append(right[j])
                j += 1
            # print("Resp> ",resp)
        resp.extend(left[i:])
        resp.extend(right[j:])    
        # print("Resp: ",resp)
        return resp

def mergesort(elementos):
    if len(elementos) <=1: 
        # if len(elementos) == 2:
        #     if elementos[0] > elementos[1]:
        #         elementos[0], elementos[1] = elementos[1], elementos[0]
        return elementos
    mitad = len(elementos)//2
    micha1 = mergesort(elementos[:mitad])
    micha2 = mergesort(elementos[mitad:])
    return merge(micha1, micha2)  


n = 15000
elementos = [random.randint(-n,n) for _ in range(n)]
# elementos = [120, 1, 92, 45, 123, 82, 10, 15, 7, -3, -21, 12, 4, 14, 71]
# elementos = [13, 1, 9, 23, -1, -5, 30, 2, 50, 40, 7]
# elementos = [38,27,43,3,9,82,10]

#Codigo

print(f"Cantidad: {len(elementos)} \n Elementos entregados:  " )
# {elementos}
inicio = time.time()
particion = int(len(elementos)/2)

elementos = mergesort(elementos)       
    
fin = time.time()    
print(f"Cantidad: num: {len(elementos)} \n Elementos obtenidos: {elementos} " )
print(f"Tiempo de ejecucion: {fin-inicio}")