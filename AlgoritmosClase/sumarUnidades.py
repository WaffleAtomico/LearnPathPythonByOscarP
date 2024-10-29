numero = input("Escribe un numero: ")
numero = ' '.join(numero).split()
numero = list( map(lambda x: int(x), numero) )
print(sum(numero))