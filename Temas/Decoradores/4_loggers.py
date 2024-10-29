#Un ejemplo muy usado son los loggers en funciones, para saber que recibimos y que enviamos a cierta funcion

def log(fichero_log): #El decorador
    def decorador_log(func): #El que recibe la funcion
        def decorador_funcion(*args, **kwargs): #Los argumentos que recibe
            with open(fichero_log, 'a') as opened_file: #Creamos archivo
                output = func(*args, **kwargs) #Le entregamos los argumentos
                opened_file.write(f"{output}\n") #Escribe la suma, resta o division
        return decorador_funcion
    return decorador_log

@log('ficherosalida.log') #Este texto mostramos
def suma(a, b):
    return a + b

@log('ficherosalida.log')
def resta(a, b):
    return a - b

@log('ficherosalida.log')
def multiplicadivide(a, b, c):
    return a*b/c

suma(10, 30)
resta(7, 23)
multiplicadivide(5, 10, 2)


'''
otro ejemplo, puede ser en flask
En donde solicita una autenticacion antes
Ejemplo...
'''

autenticado = True

def requiere_autenticación(f):
    def funcion_decorada(*args, **kwargs):
        if not autenticado:
            print("Error. El usuario no se ha autenticado")
        else:
            return f(*args, **kwargs)
    return funcion_decorada

@requiere_autenticación
def di_hola():
    print("Hola")
    
di_hola()


