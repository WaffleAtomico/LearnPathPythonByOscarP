def dividir_lista(lista, tamaño):
    return [lista[i:(i + tamaño)] for i in range(0, len(lista), tamaño)]


#E N T R A D A S 
#Recibo la  longitud de arreglos
#Recibo los numeros separados por comas
#Numero en donde inicia
#Numero en donde termina

long = int(input("Ingresa la logintud de los subarreglos: "))
# long = 4

matrix = input("Ingresa tus valores a evaluar: ")
# matrix = ( (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1), (0, 0, 1, 0) )
matrix = matrix.split(',')
matrix = dividir_lista(matrix, long)

ini = int(input("Inicias en... "))
fin =  int(input("Terminas en... "))
# ini = 4
# fin = 1

print(matrix)

recorrido = []
recorrido.append(ini-1)
cont = 0
while recorrido[-1] != fin-1:
    print(f"Recorrido completo: {recorrido}, actual: {recorrido[-1]}")
    #Para mejorar eficiencia, habria que contar cuantos caminos hay por iteracion, los nodos ya visitados, va a ser la clave
    #El valor es la cantidad de 1's que tiene a su disposicion
    #Si ya ha pasado por un nodo, se le va a restar, 
    # vaya que si es la columna 1 y tiene 3 1's, tomas el primero, quemas 1
    # Te quedan 2  1's, pero ya sabes que has pasado por el nodo 1,0
    for x in range(0, long):
        print(f"Lista actual {matrix[recorrido[-1]]}: siguiente fila {x} ",matrix[recorrido[-1]][x])
        if matrix[recorrido[-1]][x] == 1:
            if x not in recorrido:
                recorrido.append(x)
                # cont +=1
                break
            # cont +=1

print(list(map(lambda x : x+1, recorrido)))