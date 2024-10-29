'''
Si alguna vez te has encontrado con una función 
en Python que no sólo tiene una sentencia return,
sino que además devuelve un valor haciendo uso 
de yield, ya has visto lo que es un generador o generator.
'''
def funcion():
    return 5

def generador():
    yield 5
    
print(funcion())
print(generador()) #Entrega un objeto de tipo generador

'''
Una función generadora se diferencia de una función normal en que tras ejecutar el yield,
la función devuelve el control a quién la llamó, pero la función es pausada y el estado
(valor de las variables) es guardado. Esto permite que su ejecución pueda ser reanudada
más adelante.
'''

'''
Otra de las características que hacen a los generators diferentes, 
es que pueden ser iterados, ya que codifican los métodos __iter__() y __next__()
'''

a = generador()
print(next(a)) #Entrega 5
try:
    print(next(a)) #Entrega un error, ya que solo tenemos un elemento que entregar
except:
    print()
def generador():
    #Podemos ver que ahora entregamos distintos yields
    n = 1
    yield n #Cada uno

    n += 1
    yield n

    n += 1
    yield n

g = generador() #Siempre con generador()
print(next(g)) #next a la variable que significa la funcion
print(next(g))
print(next(g))  

print()

for i in generador():
    print(i) 
    
print()    
lista = [2, 4, 6, 8, 10]   #Se puede usar esta forma
al_cuadrado_generador = (x**2 for x in lista)
print(al_cuadrado_generador) #object generator

for i in al_cuadrado_generador:
    print(i, end=', ')
#Iteramos en nuestro generador para poder hacer
print()

'''
Llegados a este punto tal vez te preguntes para qué sirven los generadores.
Lo cierto es que aunque no existieran, podría realizarse lo mismo creando una clase que
implemente los métodos __iter__() y __next__().
Veamos un ejemplo de una clase que genera los primeros 10 números (0,9) al cuadrado
'''

class AlCuadrado:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > 9:
            raise StopIteration

        result = self.i ** 2
        self.i += 1
        return result
    
eleva_al_cuadrado = AlCuadrado()

for i in eleva_al_cuadrado:
    print(i)
    
#No es tan conveniente ya que es larga y hasta dificil de entender hasta cierto punto
print()

def primerosn(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums
    
print("Sin generador: ",sum(primerosn(100)))
print()
def primerosn(n):
    num = 0
    for i in range(n):
        yield num #Entregamos, pero como seguimos iterando en el rango, volvemos a entregar el numero
        num += 1
print("Con generador ",sum(primerosn(100)))

'''
Sin embargo, podemos realizar lo mismo con un generador. 
En este caso los valores serán generados uno por uno según se vayan necesitando.
'''

#Pero para ser mas especficos, en este ejemplo, es mas eficiente hacer esto
print("Mas eficiente",sum(range(100)))

