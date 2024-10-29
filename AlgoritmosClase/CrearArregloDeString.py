entradas = int(input("Cantidad de terrenos: "))
# entradas = 1
while entradas > 0:
    n = int(input("n: ")) # x 
    m = int(input("m: ")) # y 
    if n < 2:
        n = 2
    if m < 2:
        m = 2
        
    matrix = []
    
    for _ in range(m): # Pasamos fila por fila
        fila = input("Escribe todos tus caracteres de la fila : ")
        # print(' '.join(fila))
        fila = ' '.join(fila)
        # print(fila.split())
        fila  = fila.split() # Crea una lista, con cada numero que separamos
        
        for x in range( len(fila) ):
            fila[x] = int(fila[x])
            
        # print(fila)
        matrix.append(fila)  
        
    for x in matrix:
        print(x)

    
    # matrix = [  [0,0,0,0,0,0,0,0],
    #             [0,0,1,1,1,0,1,0],
    #             [0,1,0,0,1,0,1,1],
    #             [0,1,0,0,1,0,0,0],
    #             [0,1,0,1,0,0,1,0],
    #             [1,0,0,1,0,1,0,1],
    #             [0,1,1,1,0,1,0,1],
    #             [0,0,0,0,0,0,1,1],
    #             ]
    
    # for x in matrix:
    #     print(x)
    
    ''' 
    # DONDE PONGO MI GRIFO?
    
    min_x = 0
    min_y = 0
    max_x = len(matrix[0]) 
    max_y = len(matrix) 
    #Donde ponemos el grifo
    inicio_x = -1 
    inicio_y = -1
    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            if i == 0 or i == max_y-1: #Como comenzamos desde 0, necesitamos restar 1 ya que usamos indices
                if matrix[i][j] == 0:
                    inicio_x = j
                    inicio_y = i
                    break
                # print(matrix[i][j], end=' ')
            else:
                if j == min_x or j == max_x-1:
                    if matrix[i][j] == 0:
                        inicio_x = j
                        inicio_y = i
                        break
                    # print(matrix[i][j], end=' ')
        # print()  
    print(f"Posicion en donde vamos a poner nuestro grifo: ({inicio_y},  {inicio_x})")  
    
    '''
    
    
    # if matrix[inicio_y][inicio_x] == 0 # SIEMPRE SERA TRUE
    
    #Revisar estas cardinalidades en cada NODO
    # if inicio_y - 1 >= 0: 
    #     #haz X cosa
    # if inicio_x - 1 >= 0:
        
    # if inicio_x + 1 < max_x:
    
    # if inicio_y + 1 < max_y:
    
    
    # Revisar si hay a la derecha
    # Revisar si hay a la izquierda
    # Revisar si hay abajo
    # Revisar si hay arriba
    
    
    entradas -= 1