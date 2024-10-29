def formulagen(a,b,c):
    #Hacemos esto porque presuponemos que no tiene un valor
    x1 = "Indeterminado"
    x2 = "Indeterminado"

    discriminante = (b^2) - (4*a*c)
    if discriminante < 0:
        print(discriminante)
        return x1, x2
    else:
        discriminante = discriminante^0.5
        x1 = (-b + discriminante ) / (2*a)
        x2 = (-b - discriminante ) / (2*a)
        return x1, x2
    

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x1, x2 = formulagen(a,b,c)

print(f"Los resultados de X1 y X2 son: \n\n x1={x1}\n\n x2={x2}\n\n")

