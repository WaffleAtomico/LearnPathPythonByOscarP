resp = ""
resp = input("Nombre del producto: ")
productos = []

while resp != "no":
    cantidad = int(input("Digite cantidad: "))
    precio = int(input("Digite precio: "))
    productos.append([resp, cantidad, precio])
    resp = input("Nombre del producto: ")

c1 = 15
c2 = 11
c3 = 16
c4 = 10
c5 = 10
c6 = 10
print(f"|{'-'*(c1+c2+c3)}Ticket{'-'*(c4+c5+c6)}|")
print(f"|{"Producto":<{c1}}| {"Cantidad":<{c2}}|{"Precio unitario":>{c3}}|{"Importe":>{c4}}|{"Iva(16%)":>{c5}}|{"Total":>{c6}}|")

for x in productos:
    importe = x[1]*x[2]
    iva = importe*0.16
    print(f"|{x[0]:<{c1}}|{x[1]:<{c2+1}}|${x[2]:>{c3-1}.2f}|${importe:>{c4-1}.2f}|${iva:>{c5-1}.2f}|${iva+importe:>{c6-1}.3f}|")
    
print(f"|{'_'*(c1+c2+c3+c4+c5+c6+6)}|")
