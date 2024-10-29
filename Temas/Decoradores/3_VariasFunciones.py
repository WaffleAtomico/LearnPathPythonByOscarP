def operaciones(op):
    def suma(a,b):
        return a+b
    def resta(a,b):
        return a-b
    if op == "suma":
        return suma
    if op == "resta":
        return resta
    
funcion_suma = operaciones("suma")
print(funcion_suma(2,3))

funcion_resta = operaciones("resta")
print(funcion_resta(10,9))  

'''Esto es equivalente a @'''
def decorador(func):
    def envoltorio_func(a,b):
        print("Decorador antes de llamar a la funcion")
        c = func(a,b)
        print("Decorador despues de llamar a la funcion")
        return c
    return envoltorio_func #Devolvemos la direccion de memoria de la funcion, el objeto


def suma(a,b):
    print("Dentro de la suma") 
    return a+b

funcion_decorada = decorador(suma) #Le agregas la funcion ya que recibe funciones
funcion_decorada(5,8)

'''Si queremos que reciba argumentos especificos , agregariamos una funcion mas hacia afuera'''
print("\n---\n")

def mi_decorador(arg): # La funcion del decorador, que recibe argumentos
    def decorador_real(funcion): #El decorador para saber cual funcion va a ejecutar dentro
        def nueva_funcion(a, b):
            print(arg) #Imprimimos el texto antes
            c = funcion(a, b)
            print(arg) #Imprimimos el texto despues
            return c #Devolvemos
        return nueva_funcion #Devolvemos la funcion
    return decorador_real #Devolvemos el decorador real

@mi_decorador("Imprimer esto antes y después")
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8) #Cada que mandemos a llamar a suma, el decorador va a actuar antes



