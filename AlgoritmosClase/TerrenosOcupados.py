#MEJORA: Puedes conocer todos los de los lados, y luego pasas la lista de posibles fuentes
# Si conoces todos los de arriba, lo que vas a buscar va a ser abajo
# Si conoces todos los de abajo, buscaras arriba
# Si conoces todos los de la derecha, ira a la izquierda
# Si conoces todos los de la izquierda
# Entonces recorremos una lista de numeros, todos los que busques y sean validos
# Solo aplicamos el flujo por cada borde que encontramos y nos ahorramos valores


def imprimirLista(lista):
    for x in lista:
        print(x)
    print()
    
def BuscarPivote(matrix, y, x, inicio_y = 0, inicio_x = 0):
    while matrix[inicio_y][inicio_x] != 0:
        # print(f'y:{inicio_y} x:{inicio_x} -> ({y}, {x}) {matrix[inicio_y][inicio_x]} {matrix[inicio_y][inicio_x] != 0}' )
        if inicio_y == 0 or inicio_y == y-1:
            if inicio_x + 1 <= x-1: #pasamos columna si no llego al tope en la siguiente
                inicio_x += 1
            elif inicio_y + 1 <= y-1: #pasamos fila
                inicio_y += 1 
        else: #Si no estamos en los bordes superiores
            # si son los bordes laterales, solo 2 (lo que nos importa)
            if matrix[inicio_y][0] == 0:
                inicio_x = 0
                break
            if matrix[inicio_y][x-1] == 0:
                inicio_x = x-1
                break 
            inicio_y += 1  
                 
        if inicio_y == y-1 and inicio_x == x-1:
            return [-1,-1]
    return [inicio_y, inicio_x]
    
def TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, pos_y, pos_x, recorrido):
    # imprimirLista(matrix)
    # print(f"Cuadrante actual: ({pos_y}, {pos_x})")
    # print(recorrido)
    # cont = 0
    temporal_y = pos_y
    temporal_x = pos_x
    
    if temporal_x-1 >= 0 and recorrido.get((temporal_y, temporal_x-1) , 0) == 0: #Se resta ya que si puede ir a la izquierda
        if matrix[temporal_y][temporal_x-1] == 0:
            # print(f"Nodo puede ir hacia la izquierda -> ({temporal_y},{temporal_x-1}) ")
            recorrido[temporal_y, temporal_x-1] = 1
            TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y, temporal_x-1, recorrido)
            # cont += TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y, temporal_x-1, recorrido) + 1  

    if temporal_x <  lim_x-1 and recorrido.get((temporal_y, temporal_x+1) , 0) == 0: #Se suma a X pq si puede ir a la derecha
        if matrix[temporal_y][temporal_x+1] == 0:
            # print(f"Nodo puede ir a la derecha -> ({temporal_y},{temporal_x+1}) ")
            recorrido[temporal_y, temporal_x+1] = 1
            #Y se vuelve a llamar la funcion agregando los nuevos registros al set
            TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y, temporal_x+1, recorrido)
            # cont += TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y, temporal_x+1, recorrido) + 1
   
    if temporal_y < lim_y-1  and recorrido.get((temporal_y+1, temporal_x) , 0) == 0:
        if matrix[temporal_y+1][temporal_x] == 0:
            # print(f"Nodo puede ir abajo -> ({temporal_y+1},{temporal_x}) ")
            recorrido[temporal_y+1, temporal_x] = 1
            TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y+1, temporal_x, recorrido)
            # cont += TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y+1, temporal_x, recorrido) + 1 
         
    if temporal_y-1 >= 0 and recorrido.get((temporal_y-1, temporal_x) , 0) == 0:
        if matrix[temporal_y-1][temporal_x] == 0:
            # print(f"Pivote tiene para ir a arriba -> ({temporal_y-1},{temporal_x}) ")
            recorrido[temporal_y-1, temporal_x] = 1
            TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y-1, temporal_x, recorrido)
            # cont += TrazarCaminoPorNodoLibre(matrix, lim_y, lim_x, temporal_y-1, temporal_x, recorrido) + 1 
    # return cont
    
def BuscarPivotesEscondidos(matrix, y, x, conocidos):
    #Nos centramos en BORDES, lo de adentro lo traza el flujo
    for longitud_y in range(y):
        if longitud_y == 0 or longitud_y == y-1:
            for longitud_x in range(x):
                # print(buscar:= BuscarPivote(matrix, y, x, longitud_y, longitud_x) )
                # print(conocidos.get(tuple(buscar), -1) )
                buscar = BuscarPivote(matrix, y, x, longitud_y, longitud_x) 
                if buscar != [-1, -1] and conocidos.get(tuple(buscar), -1) == -1:
                    # print(buscar)
                    # print("Este no lo conozco eh ")
                    conocidos[tuple(buscar)] = 1
                    TrazarCaminoPorNodoLibre(matrix, y, x, buscar[0], buscar[1], conocidos)
        else:
            validos = [0, x-1]
            for longitud_x in validos:
                buscar = BuscarPivote(matrix, y, x, longitud_y, longitud_x)
                if buscar != [-1, -1] and conocidos.get(tuple(buscar), -1) == -1:
                        conocidos[tuple(buscar)] = 1
                        TrazarCaminoPorNodoLibre(matrix, y, x, buscar[0], buscar[1], conocidos)
                        
            '''
            for longitud_x in range(x):
                if longitud_x == x or longitud_x == x-1:
                  buscar = BuscarPivote(matrix, y, x, longitud_y, longitud_x) 
                if buscar != [-1, -1] and conocidos.get(tuple(buscar), -1) == -1:
                    # print(buscar)
                    # print("Este no lo conozco eh ")
                    conocidos[tuple(buscar)] = 1
                    TrazarCaminoPorNodoLibre(matrix, y, x, buscar[0], buscar[1], conocidos)  
            '''
            
        # print()
    # return resp

entradas = int(input("Cantidad de terrenos: "))
# entradas = 1
matrixVertical = []
while entradas > 0: 
    x = int(input("Longitud de X (Filas): "))
    y = int(input("Longitud de Y (Columnas): "))
    # x = 0
    # y = 0
    if x < 2:
        x = 2
    if y < 2:
        y = 2
    # '''
    for i in range(y):
        fila = input(f"Inserta las celdas ocupadas por edificios de la fila {i+1}, en cadena de texto: ")
        # fila = '0'
        if len(fila) < x:
            fila = fila + '0'*(x-len(fila))
        fila = ' '.join(fila[:x])
        matrixVertical.append(list( map( lambda x: int(x), fila.split() ) ))
    # '''    
    '''
    matrixVertical = [  [0,0,0,0,0,0,0,0],
                        [0,0,1,1,1,0,1,0],
                        [0,1,0,0,1,0,1,1],
                        [0,1,0,0,1,0,0,0],
                        [0,1,0,1,0,0,1,0],
                        [1,0,0,1,0,1,0,1],
                        [0,1,1,1,0,1,0,1],
                        [0,0,0,0,0,0,1,1],
                        ]
    '''
    # matrixVertical=[   [0,0,0,0,], #4
    #                    [1,0,1,0,], #2 
    #                    [0,0,0,1,], #3
    #                    [1,0,0,1,], #2 -> 11
    #                    [0,1,1,1,]
    #                 ] 
    # matrixVertical = [[0,0,0,0,0,0,0,0,], [0,0,1,0,1,1,0,0,], [0,1,0,1,0,0,1,0,], [0,1,0,0,1,0,0,1,], [0,1,1,1,0,1,0,1,], [0,0,0,0,0,0,1,1,],]
    # matrixVertical =[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],]
    # Patrones que no procesa AUN
    
    # matrixVertical = [
    #     [0, 1, 0, 1, 0, 1], # 3
    #     [1, 0, 1, 0, 1, 0], # 1
    #     [0, 1, 0, 1, 0, 1], # 3
    # ] # son 7 en total
    
    # al final debe de haber un check, para todas las filas, si hay un pivote en cada linea, sin contar una
    # que comience desde la 0, luego la 1, luego la 2 y asi
    #Tecnicamente, deberia revisar todos los de los lados (0,0) (0,1)...
    # luego que evalue desde el inicio (1,0) (2, 0)
    # Debe de encontrar pivotes que no se hayan evaluado antes
    # 
    # Y Si encuentra que hay un pivote que no tenia en su cantidad completa, lo va a usar
    # Y ahi se usa la funcion de ir nodo por nodo, partiendo de ese desconocido
    
    # matrixVertical = [
    #     [0, 0, 0, 0, 0, 0,],
    #     [1, 0, 1, 1, 1, 1,],
    #     [1, 0, 1, 1, 0, 0,],
    #     [0, 0, 0, 0, 1, 1,],
    # ] # Son 14 en total
    
    '''
    0 1 0 1 0 1 
    1 0 1 0 1 0
    0 1 0 1 0 1
    
    0 0 0 0 0 0
    1 0 1 1 1 1
    1 0 1 1 0 0
    0 0 0 0 1 1
    '''
    imprimirLista(matrixVertical)
    y = len(matrixVertical)
    x = len(matrixVertical[0])
    # #necesitamos un PIVOTE, para saber de donde comenzamos, sabemos que comenzamos por los lados de la derecha
    inicio_y, inicio_x = BuscarPivote(matrixVertical, y, x)  
    if inicio_y < 0 and inicio_x < 0:
        print("Cuadros libres: ", 0)
        break
    # print(f'Pivote> y:{inicio_y} x:{inicio_x}   -  valor: ', matrixVertical[inicio_y][inicio_x])
    conocidos = {(inicio_y, inicio_x): 1 }
    # print(conocidos)
    TrazarCaminoPorNodoLibre(matrixVertical, y, x, inicio_y, inicio_x, conocidos)
    # print("Valores escondidos ")
    BuscarPivotesEscondidos(matrixVertical, y, x, conocidos)
    # print(resp)
    print("Cuadros libres: ", len(conocidos))
    # print(max(conocidos)) #Devuelve la key maxima
    # print(max(conocidos)[0]) # Esto es y maxima alcanzada
    entradas -=1
    
         
    
    
    
    
    
''' No maquinable, horrendamente ineficiente
total = 8*8
    ocupados1 = 0
    ocupados0 = 0
    # capa = 0
    cebolla = x/2 #Por lo menos la mitad de iteraciones del maximo
    cebolla = 4
    for capa in range(cebolla):
        for x in range(len(matrix)):
            # print('x> ',x)
            for y in range(len(matrix[x])):
                # Filas
                if x == capa or x == len(matrix)-(capa+1) or y == capa or y == len(matrix[x])-(capa+1):
                    print(f'{matrix[x][y]}' , end=' ')
                    ocupados1 += 1 if matrix[x][y] == 1 else 0
                    ocupados0 += 1 if matrix[x][y] == 0 else 0
                else:
                    print(' ', end=' ')
            print()
        print("Ocupados: ", ocupados1)
        print("desocupados: ", ocupados0)
        print(f"Capa {capa} ocupados ", ocupados0+ocupados1)
          
    # print("Ocupados: ", ocupados1)
    # print("desocupados: ", ocupados0)
    # print("Capa 0 ocupados ", ocupados0+ocupados1)
    # print("Cumple? ", 8*4) #L * 4
    
'''
    
''' Demasiados acomodos, y para casos como [0,1,0,0,1,0,1,0], demasiado dificil saber, y seria tener estados "pendientes"

print("Vertical ")        
    imprimirLista(matrixVertical) 
    matrixHorizontal = []
    y = 0
    for x in range(len(matrixVertical[0])):
        aux = []
        for y in range(len(matrixVertical)):
            aux.append(matrixVertical[y][x])
        matrixHorizontal.append(aux)
    
    print("Horizontal ")        
    imprimirLista(matrixHorizontal)
    
    print("--  --")
    #aqui ya tenemos ambas listas
    for i in matrixVertical:
        print(i)
        if i.count(1) > 1: 
            izq = False
            der = False
            for j in range(len(i)//2):
                if izq and der:
                    i[j] = 1
                if i[j] == 1:
                    izq = True
                else:
                    izq = False
                if i[-j] == 1:
                    der = True
                else:
                    der = False
                print(i[j], end=' ')
                
            print()
    print("Vertical ")        
    imprimirLista(matrixVertical)
            
    
    # 0 0
    # 1 1
    # 0 1
    # 0 1
    # 1 1
    # 0 0
    # 1 1
    
        
    
    # print("Horizontal ")        
    # imprimirLista(matrixHorizontal)
    
    final= []
    for j in range(len(matrixHorizontal[0])-1):
        aux = []
        for i in range(len(matrixHorizontal)-1): #por cada nivel, hace una comparacion
            # print(matrixHorizontal[j][i] and matrixVertical[i][j])  
            aux.append(matrixHorizontal[j][i] and matrixVertical[i][j])
        final.append(aux)
    
    print("FINAL ")        
    imprimirLista(final)
    
'''   

'''RESPUESTA 1, aproach

#El pivote si o si debe de ser un 0, y debe de trazar una linea por donde encuentre un 0
    # temporal_y = incio_y
    # temporal_x = incio_x
    
    # pivote_der = True
    # pivote_izq = True
    # pivote_ariba = True
    # pivote_abajo = True
    
    # if temporal_x < x-1 and pivote_der: 
    #     print("Pivote puede ir a la derecha")
    #     #Y se vuelve a llamar la funcion agregando los nuevos registros al set
    # else:
    #     pivote_abajo = False
        
    # if temporal_x-1 > 0 and pivote_izq:
    #     print("Pivote puede ir hacia la izquierda")  
    # else:
    #     pivote_izq = False 
        
    # if temporal_y < y-1 and pivote_abajo:
    #     print("Pivote puede ir abajo")
    # else:
    #     pivote_der = False
         
    # if temporal_y - 1 > 0 and pivote_ariba:
    #     print("Pivote tiene para ir a arriba")
    # else:
    #     pivote_ariba = False
        
    #Es con recursividad, para poder ir a todos los caminos posibles, pero sin tocar los ya conocidos
    #Se agregan en un SET los ya conocidos, para evitar repetidos
    #En un set, ya que no necesitamos clave valor, solo no repetidos, al final solo los contamos
    #Con recursividad, no guardamos el camino por el que nos quedamos pendientes, pq ya solo entra en todas las opciones
    
        
    
           
    # libres = 0
    # ocupados son las filas que pasaste, teniendo en cuenta que no se pasaron todas hipoteticamente
    # totales = x*y
    
'''