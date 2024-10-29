#1h +

class Solution:
    def ProblemaD(bits, polinomio):
        print()
        grado = 0
        for x in polinomio:
            if x == '1':
                grado +=1
        print("grado: " ,grado)
        Mx = bits + '0'*grado
        
        valor_entero1 = int(Mx, 2)
        valor_entero2 = int(polinomio, 2)
        # print(Mx)
        # print(valor_entero1)
        # print(valor_entero2)
        resp = bin(int(valor_entero1 % valor_entero2))
        print(str(resp[2:]))
        return str(resp[2:])
        
        longitud = len(polinomio)
        restados = 0
        recorrrido = len(Mx)
        residuo = ''
        for x, y in zip(polinomio, Mx[restados:longitud]):
                # print(f"{x}, {y}, {r} = {int(x) ^ int(y), int(r)}")
                residuo += ""+f"{int(x) ^ int(y)}"
        print("Primer residuo", residuo) 
        residuo += Mx[longitud]
        residuo = residuo[residuo.find('1'):]
        print("Primer residuo", residuo) 

        
        for _ in range(recorrrido-grado):
            print("Recorrido de elementos ", Mx[restados:longitud])
            aux = ''
            print(f"{residuo}\n{polinomio}")
            for x, y in zip(polinomio, residuo[restados:longitud]):
                
                print(f"{x}, {y}, = {int(x) ^ int(y)}")
                aux += ""+f"{int(x) ^ int(y)}"
            residuo = aux
            print("Residuo2 ", residuo)  
            residuo += Mx[longitud]
            residuo = residuo[residuo.find('1'):]
            print("Residuo3 ", residuo)
            longitud +=1    
            restados +=1

            
            
            
        
        return Mx[::-grado]
        # D = 10
        # G = 2
        # CRC = D%G
        
        
if __name__ == "__main__":
    problema = Solution
    # bits = input("Bits: ")
    # polinomio = input("Polinomio ")
    bits = "100100"
    polinomio = "1101"
    problema.ProblemaD(bits, polinomio)
    



'''
def crc_ccitt_16(data):
    crc = 0xFFFF  # Valor inicial del CRC
    for byte in data:
        crc ^= (byte << 8)  # XOR con el byte actual desplazado
        for _ in range(8):  # Procesar cada bit
            if crc & 0x8000:  # Si el bit más significativo es 1
                crc = (crc << 1) ^ 0x1021  # Desplazar y XOR con el polinomio
            else:
                crc <<= 1  # Solo desplazar
            crc &= 0xFFFF  # Mantener solo los últimos 16 bits
    return crc

# Ejemplo de uso
data = b'Hello, World!'  # Datos a verificar
crc_result = crc_ccitt_16(data)
print(f"CRC-CCITT (16-bit) de '{data.decode()}' es: 0x{crc_result:04X}")
'''