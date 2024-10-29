numeros = [1,2,3,4,5]
print(cuadrados := [x**2 for x in numeros])

print(list(map(lambda x: x**2, numeros)))

'''
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16],
'''