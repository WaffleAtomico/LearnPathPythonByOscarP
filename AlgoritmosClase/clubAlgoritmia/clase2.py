# Cadenas
frase = ""
#Inmutables, o sea, no tienen append, pero si +=
# ESO SI, += elimina una variable y crea una nueva

# Slicing
Cadena = "Hola mundo!"
print(Cadena[-1]) #El ultimo caracter
print(Cadena[0:4]) # Desde el 0 hasta el 3
print(Cadena[::-1]) #El -1 es salto, desde atras
print(Cadena[5:11:2]) #El 2 es salto


cadena = "ironman"
print(cadena[0:4])
print(cadena[4:])

cadena = "La pelicula del joker 2 es muy mala"
print(cadena[0:2])
print(cadena[3:11])
print(cadena[12:15])
print(cadena[16:21])
print(cadena[22:23])
print(cadena[24:26])
print(cadena[27:30])
print(cadena[31:])


cadena="reconocer"
print(cadena[::-1])



cadena = "Baby la vida es un ciclo."
lista1 = list(cadena)
print(lista1)
lista2 = cadena.split(" ")
print(lista2)
nuevacadena = "".join(lista1)
print(nuevacadena)

print("-".join(lista1))

cadena = "Hola que tal?"

listaresp = []
palabras = cadena.split(" ")
for x in palabras:
    print(x, end="") 
print()

cadena = "Condenadota"
listaresp = list(cadena)
print(listaresp)

cadena = "Hace frio esta mañana"
for x in cadena.split(" "):
    print(x[::-1], end=" ")
    



frase = "111"
print(frase.count('1'))

#Investigar counter
