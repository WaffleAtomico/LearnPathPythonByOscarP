frase = "nombre#categoria%folio"
frase = frase[:frase.find("#")] + ' ' + frase[frase.find("#")+1:frase.find("%")]  + ' ' +  frase[frase.find("%")+1:]
print(frase)