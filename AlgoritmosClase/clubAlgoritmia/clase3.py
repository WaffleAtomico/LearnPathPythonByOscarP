'''
Una funcion es un segmento de codigo que podemos recibir parametros
parametros, las variables sin recibir nada
Argumentos, ya cuando le das valores

Puede o no hacer un proceso
'''

def add(param1, param2):
    return param1+param2


'''
Decorators are a very powerful and useful tool in Python
since it allows programmers to modify the behaviour of a 
function or class. 

In Python, functions are first class objects which means
that functions in Python can be used or passed as arguments.
'''

    
def shout(text):
    return text.upper()

def wisper(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)
    
print(shout("Hello"))
yell = shout

print(yell("hello"))


greet(shout)
greet(wisper)


def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)
print(add_15(10))


def contador():
    conteo = 0
    def incrementar():
        nonlocal conteo
        conteo += 1
        return conteo
    
    return incrementar

mi_contador = contador()
print(mi_contador)
print(mi_contador)


contador_global = 0
def incrementar_contador():
    count = 0
    global contador_global
    contador_global += 1
    count +=1
    return count
def obtenerContador():
    return contador_global

print(f"{obtenerContador() } {incrementar_contador()}")

'''
@gfg_decorator 
def hello_decorator():
    print("Gfg")
'''  
'''Es equivalente a

def hello_decorator():
    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)
'''

