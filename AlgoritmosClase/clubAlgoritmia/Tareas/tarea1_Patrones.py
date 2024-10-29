def juego1(n):
    '''
    ***
    ***
    ***
    '''
    print("Juego 1")
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()
    
def juego2(n):
    '''
    111
    222
    333
    '''
    print("Juego 2")
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i, end="")
        print()
    
def juego3(n):
    '''
    123
    123
    123
    '''
    print("Juego 3")
    for _ in range(n):
        for j in range(1, n+1):
            print(j, end="")
        print()
        
def juego4(n):
    '''
    *
    **
    ***
    '''
    print("Juego 4")
    for i in range(1,n+1):
        for j in range(i):
            print("*", end="")
        print()
    
def juego5(n):
    '''
    1
    12
    123
    '''
    print("Juego 5")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
    
def juego6(n):
    '''
    123
    12
    1
    '''
    print("Juego 6")
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end="")
        print()
        
def juego7(n):
    '''
    321
    21
    1
    '''
    print("Juego 7")
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()
    
def juego8(n):
    '''
      *
     **
    ***
    '''
    print("Juego 8")
    for i in range(n, 0, -1):
        for j in range(0, n):
            if j < i-1:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    
def juego9(n):
    '''
      1
     21
    321
    '''
    print("Juego 9")
    for i in range(n, 0, -1):
            for j in range(1, n+1, 1):
                if j < i: 
                    print(" ", end="")
                else:
                    print((n-j+1), end="")
            print()
    
def juego10(n):
    '''
    ***
    * *
    ***
    '''
    print("Juego 10")
    for i in range(n):
        for j in range(n):
            if i == n-1 or i == 0 or j == n-1 or j == 0:
                print("*", end="")
            else:
                print(' ', end='')
        print()
        
n = int(input("Selena, pon tu numero del tamaño de las figuras papu: "))
# n = 10


juego_op = int(input("Selecciona un juego papu Selena, del 1 al 10: "))

match juego_op:
    case 1:
        juego1(n)
    case 2:
        juego2(n)
    case 3:
        juego3(n)
    case 4:
        juego4(n)
    case 5:
        juego5(n)
    case 6:
        juego6(n)
    case 7:
        juego7(n)
    case 8:
        juego8(n)
    case 9:
        juego9(n)
    case 10:
        juego10(n)
    case _:
        print("Opción no válida. Por favor selecciona un número del 1 al 10.")

