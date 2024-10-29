def izquierda(frase, cantidad):
    if cantidad <= len(frase):
        return frase[:cantidad]
    else:
        return ""
    
def derecha(frase, cantidad):
    if cantidad <= len(frase):
        return frase[-cantidad:]
    else:
        return ""

frase = "12345"
print(izquierda(frase, 5))
print(derecha(frase, 5))