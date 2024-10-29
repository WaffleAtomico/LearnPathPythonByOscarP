import re

def arremedar(text: list[chr]) -> chr:
    vocales = "aeiouáéíóú"
    filteredList = list(map(lambda x: (x := 'i' ) if x in vocales else x.lower, text))
    print("".join(filteredList))
    
frase = "que haces, quiero ese cofre"
# print(sorted(frase))
# print(type(frase))
# print(frase[2])
arremedar(frase)

nuevo_txt = re.sub(r"[aeiouAEIOU]", "i", frase)
print(nuevo_txt)
#C o java, o la mayoria
# for(int i = 0; i<=10; i++){


# }


# sumar_puntos(frase)
#Salida esperada "Qii hicis, qiiiri isi cifri"


