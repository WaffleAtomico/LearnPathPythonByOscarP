# Hoja contable

name = input("Nombre: ")
lastname = input("Apellido: ")
print("Gastos:")

matches = [] #No idea que es una partida en realidad
# [345, "Gas", 2450.20],[3,"Papeleria", 954.00],[123, "Algo", 12.12]
for x in range(1,6):
    p = input(f"Partida {x} (máx. 5 dígitos): ")
    d = input("Descripción (máx. 20 letras): ")
    m = float(input("Monto mensual: $"))
    matches.append([p,d,m])

print(f"Nombre: {name} ", end='')
print(f"{lastname}")

guiones = 3

print(f"\"Hoja contable\"".upper())
# > Derecha         < Izquierda
print(f"{"ID":^{5+guiones}}{"Descripción":^{20+guiones}}{"Costo":^{9+guiones}}")
for x in range(0, 5):
    print(f"{matches[x][0]:>5}{"-"*guiones}{matches[x][1]:<20}{"-"*guiones}${matches[x][2]:>9.2f}")