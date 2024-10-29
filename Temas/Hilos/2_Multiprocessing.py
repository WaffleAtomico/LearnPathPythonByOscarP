import time
from multiprocessing import Pool
COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start) #1.06xx (Mucho menos que 1.5xxx, que fue el anterior)
#El tiempo no se reduce a la mitad ya que la libreria tiene sus propios procesos

'''
Siguiendo con la explicacion, quiza no podamos usar hilos, pero si multiprocesamiento

The most popular way is to use a multi-processing approach where you use multiple processes 
instead of threads. Each Python process gets its own Python interpreter and memory space so 
the GIL won’t be a problem.

Lo que hace esta libreria es que usa otro proceso que no es multi-threading

Tambien depende del interprete
'''