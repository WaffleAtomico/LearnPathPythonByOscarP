import sys

def test1():
    x=0
    
def test2():
    print("hello world")
    
def test3():
    x=1
    y=5
    return x+y
    

resp = sys.getsizeof(test2())

print("Tamano de la funcion: ", resp)


print(sys.getsizeof(1.0))                  # 24
print(sys.getsizeof(""))                   # 41
print(sys.getsizeof("Hello!"))             # 47
print(sys.getsizeof(dict()))               # 64
print(sys.getsizeof(dict({'A':1})))        # 184
print(sys.getsizeof(dict({'A':1, 'B':2}))) # 184


variables = {
    "int": 5,
    "float": 5.3,
    "str": "Hola",
    "list": [],
    "tuple": (),
    "dict": {},
    "set": set(),
    "bool": True,
}

# Función para mostrar el tamaño de cada variable
def mostrar_tamaños(variables):
    for tipo, valor in variables.items():
        print(f"Tamaño de {tipo}: {sys.getsizeof(valor)} bytes")

# Llamamos a la función
mostrar_tamaños(variables)


frase = "Anita lava la tina"
# frase = "Subibus"
frase_formateada = frase.lower().replace(" ", '')
print(frase_formateada == frase_formateada[::-1])