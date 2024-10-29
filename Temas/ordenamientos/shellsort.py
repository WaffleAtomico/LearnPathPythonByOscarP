import random, time
import insertionsort
n = 150000
elementos = [random.randint(-n,n) for _ in range(n)]
# elementos = [120, 1, 92, 45, 123, 82, 10, 15, 7, -3, -21, 12, 4, 14, 71]
# elementos = [13, 1, 9, 23, -1, -5, 30, 2, 50, 40, 7]
inicio = time.time()
time.sleep(1)

#Codigo

# print(f"Elementos entregados: {elementos} num: {len(elementos)} " )

salto = int(len(elementos)/2)

# numbers = []

while salto >= 1: 
    # print(f"------------------------> El salto vale: {salto} <--------------------------")
    numbers = []
    sub_num_group = []
    for a in range(0, salto):
        sub_numbers = []
        for x in range(a, len(elementos), salto):
            sub_numbers.append(elementos[x])
        # print("Subnumbers: ",sub_numbers)
        sub_num_group.append(insertionsort.insertion(sub_numbers))
        # for n in :
        
        # print("Subgroup: ",sub_num_group)
    
    for y in range(len(sub_num_group[0])):
        # print(f"y == {y} -- {len(sub_num_group[y])}")
        for x in range(len(sub_num_group)): #Este es para el numero de elementos
            # print(f"x == {x} -- {sub_num_group[x][y]}")
            # print(f"x == {x} \ny == {y}")
            if y <= len(sub_num_group[x])-1:
                # print(f"Numero a agregar {sub_num_group[x][y]}")
                numbers.append(sub_num_group[x][y])
                # print(f"> Numbers: ", numbers)  
            else:
                break
        # print(f"----> Numbers {a}: ", numbers)       

    # print(f"----> Numbers {a}: ", numbers)   
    salto = int(salto/2)
    
elementos = numbers       
        
print(f"Elementos obtenidos: {elementos} num: {len(elementos)} " )
fin = time.time()
print(f"Tiempo de ejecucion: {fin-inicio}")




''' # Generado con IA
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializa el gap

    # Comienza con el gap más grande y reduce el tamaño del gap
    while gap > 0:
        # Realiza una inserción con el gap actual
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Mueve los elementos que están a 'gap' posiciones por delante
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp  # Coloca el elemento temporal en su posición correcta
        
        gap //= 2  # Reduce el tamaño del gap

    return arr

# Ejemplo de uso
numeros = [12, 34, 54, 2, 3]
print("Arreglo original:", numeros)
numeros_ordenados = shell_sort(numeros)
print("Arreglo ordenado:", numeros_ordenados)

'''