n = int(input("Valor a obtener factorial"))
resp = 1


lista1 = [1,3,5,10,3,4,5,6]
while n != 0:
    resp = n*resp
    n -=1   
print(resp)