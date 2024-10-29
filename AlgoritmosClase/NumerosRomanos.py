# Igual, mejor hacer un diccionario para los ifs
# para devolver un valor por default, podemos agregar un valores.get(n, 0)
# Por si no se encuentra
def valorletra(letra):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000}
    return valores.get(letra, 0)



def valor_numero(num):
    # Parceo de decimales a romanos
    # Si, fue necesario usar los anteriores ya que si se me hizo mas dificil hacer la resta
    valores = {1: 'I', 4: 'IV', 5: 'V', 9:'IX', 10:'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 900: 'CM', 1000: 'M'}
    return valores.get(num, "")
    
def valor_numero_menor(num_mayor):
    #Guardamos el valor si es menor al que tenemos
    otros_valores = [4, 9, 40, 90, 900]
    numeros_especificos = [1, 5, 10, 50, 100, 1000]  
    # Evaluamos si esta en un valor cerrado
    if num_mayor in otros_valores or num_mayor in numeros_especificos:
        return num_mayor
    # Si no esta en un valor cerrado, entonces vamos revisando cual es el menor que tenga EN LOS ESPECIFICOS
    numero_menor = 0
    for x in numeros_especificos:
        if num_mayor > x:
            numero_menor = x
    return numero_menor


def numeros_decimal(numDec):
    result = ""
    # Hacemos un arreglo de nuestra entrada, para evaluar cada valor por separado
    numero_partido = [int(x) for x in str(numDec)]
    # Multiplicamos depende de su posicion, teniendo en cuenta que no sera mayor a 9999
    match len(numero_partido):
        case 2:
            numero_partido[0] = 10 * numero_partido[0]
        case 3:
            numero_partido[0] = 100 * numero_partido[0]
            numero_partido[1] = 10 * numero_partido[1]
        case 4:
            numero_partido[0] = 1000 * numero_partido[0]
            numero_partido[1] = 100 * numero_partido[1]
            numero_partido[2] = 10 * numero_partido[2] 
              
    for x in range(0, len(numero_partido)):
        copia = numero_partido[x]
        result += valor_numero(valor_numero_menor(copia))
        copia = copia - valor_numero_menor(copia)
        while copia > 0:
            result += valor_numero(valor_numero_menor(copia))
            copia -= valor_numero_menor(copia)            
    return result
    
    

def numeros_romanos(num):
    longitud = len(num)
    # Si la longitud es de 1, es una sola letra, por ende, un valor fijo
    if longitud == 1:
        return valorletra(num)
    
    result = 0
    pos_letra = 0    
    while pos_letra < longitud:
        int_act = valorletra(num[pos_letra])
        if pos_letra < longitud-1:
            int_post = valorletra(num[pos_letra+1])
            if int_act < int_post:
                result += int_post - int_act
                pos_letra += 2
            else:
                result += int_act
                pos_letra += 1
        else:
            result += int_act
            pos_letra +=1
       
    return result


n_dec = [1,2,3,4,5,6,7,8,9,10,94,3999]



for x in range(1, 30):
    dec = numeros_decimal(x)
    print(f"{x} Numero de decimal a romano {dec} y romano a decimal: {numeros_romanos(dec)}")
    
    
# for x in n_dec:
#     print(f"Resultado de x {x}:      {numeros_decimal(x)}\n\n")

'''
n_romanos = ["I", "II", "III","IV","V","VI","VII","VIII", "IX", "X", "XCIV","MCMXCIV", "MMMCMXCIX"]
for x in n_romanos:
    print(f"Resultado {x}:",numeros_romanos(x))
'''

    # print(f"Resultado {x}: ",numeros_romanosII(x))
    
    
    
'''
def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                res = res - d[s[i]]
            else:
                res = res + d[s[i]]
        res = res + d[s[-1]]
        return res
'''