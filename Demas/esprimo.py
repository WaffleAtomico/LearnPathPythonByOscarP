n = 8
n = int(input("Escribe un numero, para saber si es primo o no "))
esprimo = False
a = 2
while not esprimo and a <= n-1:
    if (n % a) == 0:
        esprimo = True
        break
    a += 1
if not esprimo:
    print("Es primo")
else:
    print("No es primo")