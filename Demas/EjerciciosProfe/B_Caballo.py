#31 minutos

class Solution:
    def Caballo():
        y, x = input("MxN: ").split('x')
        x = int(x)
        y = int(y)
        caballo_y, caballo_x = input("IxJ: ").split(',') #2,1
        caballo_x = int(caballo_x)-1 #2-1 = 1
        caballo_y = int(caballo_y)-1 #1-1 = 0
        
        matrix = []
        for _ in range(y):
            matrix.append(["." for _ in range(x)])
            
        if caballo_x >= 0 and caballo_x <= x-1 and caballo_y >= 0 and caballo_y<= y-1:
            matrix[caballo_y][caballo_x] = 'K'

        for punto_Y in [caballo_y+2, caballo_y-2]:
            if  punto_Y >= 0 and punto_Y<= y-1:
                for punto_X in [caballo_x+1, caballo_x-1]:
                    if punto_X >= 0 and punto_X <= x-1:
                        matrix[punto_Y][punto_X] = 'o'
                        
        for punto_X in [caballo_x+2, caballo_x-2]:
            if punto_X >= 0 and punto_X <= x-1:
                for punto_Y in [caballo_y+1, caballo_y-1]:
                    if  punto_Y >= 0 and punto_Y<= y-1:
                         matrix[punto_Y][punto_X] = 'o'  
                                     
            # matrix[caballo_y+2][caballo_x+1] = 'o'
            # matrix[caballo_y+2][caballo_x-1] = 'o'
            # matrix[caballo_y-2][caballo_x+1] = 'o'
            # matrix[caballo_y-2][caballo_x-1] = 'o'    
        
            # matrix[caballo_y+1][caballo_x+2] = 'o'
            # matrix[caballo_y-1][caballo_x+2] = 'o'
            # matrix[caballo_y+1][caballo_x-2] = 'o'
            # matrix[caballo_y-1][caballo_x-2] = 'o'  
        for x in matrix:
            linea = ''.join(x)
            print(linea)
        
        
        
if __name__ == "__main__":
    problema = Solution
    problema.Caballo()