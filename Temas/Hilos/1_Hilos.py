# https://realpython.com/python-gil/
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

print("Sin hilos")
start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds: ', end - start)


print("Con hilos")
t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

'''
No hay mucha diferencia, solo unos pocos microseguntos
El GIL: Python Global Interpreter Lock 
El GIL permite que se puedan ejecutar cosas con "Buen tiempo", pero una por una
El lenguaje esta hecho para que sea digerible, para iniciar
Los hilos al hacer procesos mientras se ejecutan otros
pueden tener problemas al tratar de apuntar hacia variables, QUE SON OBJETOS
En pocas palabras, python se hace bolas a hacer referencia a sus variables con los hilos
'''

'''
El poder manejar hilos o quitar el GIL (Ejecutar solo uno por uno)
Haria aun mas lento el lenguaje, por eso no se quita o no se tiene planes de quitarlo, aun

PERO, laa gente es arraigada y le encanta resolver cosas
'''

