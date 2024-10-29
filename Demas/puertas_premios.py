vA = int(input("vA: ")) # Valor A 
pA = int(input("pA: ")) # Puerta A el valor para abrirla
vB = int(input("vB: ")) # Valor B
pB = int(input("pB: ")) # Puerta B el valor para abrirla
puntos = int(input("puntos: ")) #Puntos diponibles mios


'''
1 es igual a que puedo comprar esa puerta


A B
1 1 = ambos -> Nuevo caso 1
0 1 = solo B
1 0 = Solo A
0 0 = Nadota
'''
'''
Nuevo caso 1 en donde ambos son 1 1
pA + pB <= puntos? 
Si -> ganaste ambos
No -> Nuevo caso 2
'''
'''
Nuevo caso 2 en donde la suma de ambos no me da el valor de mis puntos, pero me ajusta para mis dos puertas
vA > vB ? Agarro A
vA < vB ? Agarro B
'''
'''
if puntos >= pA+pB: #Si la suma de estos dos es mayor, me gane ambos, ambos valores vaya
    # 1 1
     print("*Ganaste el valor de A sumado con B ",vA+vB)
elif puntos < pA and puntos <pB: # si es menor a ambas puertas nadota
    # 0 0
    print("*Te ganaste nadota ", 0)
elif puntos < pA and puntos >= pB: #Si me ajusta solo para B pero no para A
    # 0 1
    print("* Puerta A < puntos & puerta B > puntos Ganaste el valor de B ",vB)
elif puntos >= pA and puntos < pB: #Si me ajusta solo para A pero no para B
    # 1 0
    print("* pA Ganaste el valor de A ", vA)
else: #Presuponemos que ya pasamos por las combinaciones posibles, lo cual es cierto
    # 0 0
    if vA > vB:
        print("* vA > vB Ganaste el valor de A ", vA)
    else:
        print("* vB > vA Ganaste el valor de B ", vB)
'''  
    
# elif puntos < (pA+pB): 
    


if puntos >= pA+pB: # 1 1 / Si
    print("Ganaste el valor de A sumado con B ",vA+vB)
elif puntos < pA and puntos < pB: # 0 0
    print("Te ganaste nadota ", 0)
elif puntos < (pA+pB): # 1 1 / No
    if vA > vB:  # 1 1 / No /  vA es mayor que vB
        print("Ganaste el valor de A ",vA)
    elif vB < vA: # 1 1 / No /  vB es mayor que vA
        print("Ganaste el valor de B ",vB)
    elif pA == pB: 
        ''' 
        Este no existe, pq ya lo pensaste arriba y abajo
        Si valen lo mismo, significa que A no es mayor que B
        y que b no es mayor a A
        
        Que hace tu codigo?
        En caso de que no cumpla con lo que le pediste, no te devuelve nada (Revisa el nuevo print que puse)
        '''
        if vA > vB:
            print("Ganaste el valor de A ",vA)
        else:
            print("Ganaste el valor de B ",vB)
    else:
        print("Aca no hago nd w") # aca entra en el caso 4
elif puntos >= pA and puntos < pB: # 1 0
    print("Ganaste el valor de A ",vA)
else: # 0 1
    print("Ganaste el valor de B ",vB)
