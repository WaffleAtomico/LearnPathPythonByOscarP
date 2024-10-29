'''
codigo oscar penilla software :D
'''
#1
numeros1 = [3, 1, -3, 4, 20]
minimo = 0

valmin = min(numeros1)
for x in range(1, len(numeros1)):
    if numeros1[x] == valmin:
        minimo = x
        break
        
# for x in range(1, len(numeros1)):
#     if numeros1[x] < x:
#         min = x
        
print("Pos min", minimo)

#2
target = 'a'
palabra = "jajaja"
num = 0
for x in palabra:
    if x == target:
        num +=1
    
print(num)



#3

cont = 0
numeros2 = [40, 20, 2, 30, 5, 5, 10, 9, 8]
for x in range(0, len(numeros2)):
    if x == numeros2[x]:
        cont +=1
print(cont)


#4
cadena = "pepe pica papas"
cadena = "Hola tengo varias palabras a a a a"
target2 = cadena[0]
resp = True
for x in range(0, len(cadena)):
    if cadena[x] == ' ' and cadena[x+1 if x+1 < len(cadena) else x] == target:
        # print("Valocito ",x)
        resp = False
        break
        
print(resp)
