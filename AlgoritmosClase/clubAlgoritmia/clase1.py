'''
Cada for va a tardar mas

'''

# Comentamos ya que es un chingo de datos

'''
for i in range(24):
    for j in range(60):
        for k in range(60):
            print(f"{i} : {j} : {k}")
'''

            
            
# Tabla de verdad, hasta el 8
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            print(f"{i} {j} {k}")
            
            
            
# Tablero de ajedrez

for i in range(8):
    for j in range(8):
        if (j+i) % 2 == 0:
            print("X", end="")
        else:
            print("0", end="")
    print()
    


# Problema


'''
Selenea esta aprendiendo
Imprimir valores
'''

def juego3(n):
    '''
    123
    123
    123
    '''
    for _ in range(n):
        for j in range(1, n+1):
            print(j, end="")
        print()
    
def juego4(n):
    '''
    ***
    **
    *
    '''
    # MEJOR MANERA HECHA POR OSCAR PENILLA SKAKIEVICH WIIII
    for i in range(1,n+1):
        print("*"*i)
    # for i in range(1,n+1):
    #     for j in range(i):
    #         print("*", end="")
    #     print()
    
    
def juego6(n):
    '''
    123
    12
    1
    '''
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()


n = 3
juego3(n)
juego4(n)
juego6(n)



numero = 123124
print("Cantidad de caracteres: ", len(str(numero)))

contador = 0
while numero != 0:
    numero = numero//10
    contador += 1
    
print("Cantidad de caracteres: ", contador)
    




def twosum(numbers, target):
    result = []
    for i in range(0, len(numbers)):
        if numbers[i]+numbers[-i] == target:
                result.append(i+1)
                result.append(i+1)
                return result
        # for j in range(i+1, len(numbers)):
            
    
numbers = [1, 2, 7, 11, 15]


print(twosum(numbers, target=9))

def piramide(n):
    if n % 2 == 0:
        m = n-1
        for i in range(1,n+1):
            print(" "*m, end="")
            print("*"*i*2) # *2 para espejearlo
            m -= 1
    else:
        m = n-1
        for i in range(1,n+1):
            print(i, end='')
            print("-",m)
            print(" "*m, end="")
            print("*" * i, end='')
            print("*" * (i-m))
            m -= 1

n = 3
piramide(n)
