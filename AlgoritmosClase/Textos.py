frase = input("Escribe una frase: \n")
palabras = len(frase.split())
letras = 0
vocales = {
           'a': 0, 'e': 0,'i': 0,'o': 0,'u': 0,
           'A': 0,'E': 0, 'I': 0, 'O': 0, 'U': 0,
           'á': 0, 'é': 0,'í': 0,'ó': 0,'ú': 0,
           'Á': 0,'É': 0, 'Í': 0, 'Ó': 0, 'Ú': 0,
          }
char_vocalestilde = 'áéíóú'
for x in frase:
    if x.isalpha():
        letras += 1 
        if x in vocales.keys():
            vocales[x] += 1
    
print(f" Numero de palabras: {palabras}")
print(f" Numero de letras: {letras}")
print(" Cantidad de vocales existentes")
for x, y in vocales.items():
    if y != 0 :
        print(f" {x} : {y}")