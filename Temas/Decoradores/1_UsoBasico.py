'''
def helloDecorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
        
    return inner1

@mi_decorador 
def function_to_be_used():
    print("This is inside the function")
    
function_to_be_used = helloDecorator(function_to_be_used)

function_to_be_used()
'''

def mi_decorador(funcion): #este es el decorador
    def nueva_funcion(a, b):
        print("Se va a llamar") #Se llama
        c = funcion(a, b) #instanciamos la funcion recibida por el decorador
        print("Se ha llamado")
        return c #Devolvemos de todas maneras el valor, AQUI TERMINA
    #Retorna la nueva funcion, esta reciba a y b
    return nueva_funcion #Este trae el valor de c

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

print(suma(5,8))


def di_hola():
    print("Hola")
    
f1 = di_hola() #LLama a la funcion
f2 = di_hola # asigna a f2 la funcion, cada que se escriba f2, se le va a poder agregar argumentos

print(f1) # None, di_hola no devuelve nada
print(f2) # Objeto de tipo funcion

f2() #Se manda a llamar a la funcion

del f2 #Eliminamos el objeto de la funcion

di_hola() #Sigue existiendo
    