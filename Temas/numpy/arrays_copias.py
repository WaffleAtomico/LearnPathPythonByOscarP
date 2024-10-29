import numpy as np

arr = np.array([1, 2, 3, 4, 5])
y = arr.copy() # <- la copia nos vale vrg, literalmente es hacer una copia 
x = arr.view() # <- COMO UN PUNTEROOOOOOO WEEEEEEEY
arr[0] = 42 #   <- SI MODIFICO A ESTE NACO, MODIFICO EL OTROOOOOOO
x[1] = 31   #   <- Pero a este se le modifica al nuevo tambien

print(arr)
print(x)
print(y) 