# 33 minutos 
# Resolucion teorica como en 15, pero depuracion 15
class Solution:
    def JuegoNumerico(Numero):
        if Numero == 6174:
            return 0
        if Numero == 0:
            return 0
        
        numero = str(Numero)
        if len(numero) < 4:
            numero = '0'*(4 - len(numero)) + numero
            
        if numero[0] == numero[1] == numero[2] == numero[3]:
            return 8
        
        cont = 0
        while numero != "6174":
            if len(numero) < 4:
                numero = '0'*(4 - len(numero)) + numero
            numero = ' '.join(numero).split()
            numero.sort()
            resp = ''
            for x in numero:
                resp = resp + f"{x}"      
            numero = resp
            numero = str(int(numero[::-1]) - int(numero) )
            cont +=1
        return cont
        

if __name__ == "__main__":
    problema = Solution
    iteraciones = int(input("Iteraciones: "))
    valores = []
    while iteraciones != 0:
        numero = int(input("Numero: "))
        valores.append(numero)
        iteraciones -= 1
    for x in valores:
        print(problema.JuegoNumerico(x))