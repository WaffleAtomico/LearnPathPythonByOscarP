# https://ellibrodepython.com/decoradores-python
def di_hola():
    print("Hola")
    
f1 = di_hola() #LLama a la funcion
f2 = di_hola # asigna a f2 la funcion, cada que se escriba f2, se le va a poder agregar argumentos

print(f1) # None, di_hola no devuelve nada
print(f2) # Objeto de tipo funcion

f2() #Se manda a llamar a la funcion

del f2 #Eliminamos el objeto de la funcion

di_hola() #Sigue existiendo