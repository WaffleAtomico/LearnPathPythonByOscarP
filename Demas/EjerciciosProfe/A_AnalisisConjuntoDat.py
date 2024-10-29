'''1h Aprox'''

# Naranja,-,Rojo,Azul,Blanco,-,Naranja,-,Blanco,Negro,Negro,Rojo,Blanco,-,Naranja,-,Azul,Naranja,Negro,Rojo,Rojo,Blanco,Negro,Naranja,Azul

# Azul,Negro,-,Rojo,-,-,Naranja,Azul,Azul,-,Blanco,Azul,Naranja,-,Negro,Blanco,Azul,Naranja,Negro,Azul,Azul,Rojo,-,Azul,Rojo

# Azul,Rojo,Naranja,-,Blanco,Negro,Blanco,Rojo,-,-,Blanco,Azul,-,Negro,-,Rojo,-,Negro,-,-,Naranja,-,Blanco,Rojo,-


class Solution:
    
    def Azulejos():
        Colores = {"Azul": 0, "Negro" :0, "Rojo":0, "Naranja":0, "Blanco":0}

        matrix = []
        orden = input("Colores: ").split(',')
        cal = 0

        # for x in orden.split(','):
        matrix = [orden[i:i+5] for i in range(0, len(orden), 5)]
          
        #Horizontal
        for x in matrix:
            aux = x.copy()
            cant = aux.count('-')
            if cant > 0 :
                for _ in range(cant):
                    aux.remove('-')       
            if len(aux) != len(set(aux)):
                return "Invalido"
            else:
                #Regla 3
                cal += 2 if len(set(aux)) == 5 else 0
            print(aux) 
            for vals in aux:
                Colores[vals] += 1
                
        #Vertical        
        matrixV = [list(x) for x in zip(*matrix)]
        for x in matrixV:
            aux = x.copy()
            cant = aux.count('-')
            if cant > 0 :
                for _ in range(cant):
                    aux.remove('-')
            if len(aux) != len(set(aux)):
                return "Invalido"
            else:
                #Regla 4
                cal += 7 if len(set(aux)) == 5 else 0
                
        for x in Colores:
            if Colores.get(x) == 5:
                cal+=10
        # print(ColoresV)        
        # for x in ColoresV:
        #     if ColoresV.get(x) == 5:
        #         cal+=10
        return cal
        

if __name__ == "__main__":
    problema = Solution
    print(problema.Azulejos())