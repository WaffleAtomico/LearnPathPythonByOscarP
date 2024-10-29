month = int(input("Ingrese la cantidad de meses a calcular "))
for i in range(month):
    finalcost =+ int(input(f"Ingrese gastos de mes {i+1}: "))
print(f"El acumulado de gastos es de {finalcost}")
print(f"El promedio es {finalcost/month}")