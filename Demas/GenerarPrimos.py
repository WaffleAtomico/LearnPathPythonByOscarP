# n = 499979

# Si encuentro un primo, lo guardo, y si el siguiente es divisible entre cada uno de los primos

# Debajo del 8?
# P = n - c - 2
# P = 8 - 2 - 2
# 4 = 8 - 2 - 2

#n = 60 #- primos = 17    - 183 instrucciones v1
#n = 60 #- primos = 17    - 101 instrucciones v2 VERIFICADO

#n = 10 #- primos = 4     - 8 instrucciones


n = 2
def generarprimos(n):
    numprimlist = []
    for x in range(2, n):
        root = (x ** 0.5)
        if root % 1 != 0:    # si fuera == es que es cerrada, como no es cerrada entonces no 
            a = 0
            for y in range( 0, (len(numprimlist)) ):
                if numprimlist[y] > root:
                    break
                if x % numprimlist[y] == 0:
                    a += 1
                    break
            if a == 0:
                numprimlist.append(x)
    return numprimlist

# print(numprimlist)
print(f"Cantidad de primos: {generarprimos(n)} \n{len(generarprimos(n))}") # \n En {itera} iteraciones")



''' v1
# Menores a n
n = 4
numprimlist = []
for x in range(2, n):
    a = 0
    for y in range(0, (len(numprimlist))):
        # print(f"x {x} % con {numprimlist[y]}")
        if x % numprimlist[y] == 0:
            a += 1
            break
    if a == 0:
        numprimlist.append(x)
    print("Lista completa ------------->>>>>>>",numprimlist)

print(len(numprimlist))
'''


''' v2


numprimlist = []
itera = 0
for x in range(2, n):
    # print(f"Actual value: {x}")
    a = 0
    # print(f"Isinstance {x ** 0.5} ",  (x ** 0.5) % 1 != 0 )
    root = (x ** 0.5)
    if root % 1 != 0:    # si fuera == es que es cerrada, como no es cerrada entonces no 
        for y in range( 0, (len(numprimlist)) ):
            # print(f"->{y}<-")
            # print(f" ==>  x {x} % con {numprimlist[y]}  ints ->", itera := itera+1)
            # print(f" > root {root} % con  '{numprimlist[y]}'  =  {root % numprimlist[y]} -> % { (root % numprimlist[y]) % 1 } -> mod igual a  { ((root % numprimlist[y]) % 1) == 0 } \n")
            if numprimlist[y] > root:
                break
            if x % numprimlist[y] == 0:
                a += 1
                break
        if a == 0:
            # print("Es primo")
            numprimlist.append(x)
        # else:
            # print("No es primo")
    # print("Lista completa ------------->>>>>>>",numprimlist)

'''










# ''' # Solucion
def sieve_of_eratosthenes(n):
    es_primo = [True] * (n)
    es_primo[0] = es_primo[1] = False 
    for i in range(2, int(n**0.5) + 1):
        if es_primo[i]:  # Si i es primo
            for j in range(i * i, n, i):
                es_primo[j] = False

    return [i for i in range(n) if es_primo[i]]

# Uso del algoritmo
# n = 499000

# primos = sieve_of_eratosthenes(n)
# print(f"Números primos hasta {n}: {primos} \n{len(primos)}")

# '''

n = 1000200
def countPrimes(n):
        if n<=2:
            return 0
        ref=[True]*(n)
        i=2
        while (i*i)<n:
            if ref[i]:
                for j in range(i*i,n,i):
                    ref[j]=False
            i+=1
        return [i for i in range(n) if ref[i]]
        return ref.count(True)-2
    
primos = countPrimes(n)
print(f"Números primos hasta {n}: {primos} ")

''' Solucion MEJOR

def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        ref=[True]*(n)
        i=2
        while (i*i)<n:
            if ref[i]:
                for j in range(i*i,n,i):
                    ref[j]=False
            i+=1
        return ref.count(True)-2

'''