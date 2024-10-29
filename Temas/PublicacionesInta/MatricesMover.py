mylist = [
        [1,2,3,],
        [4,5,6],
        [7,8,9],]

print(mylist)

# print(*mylist) #No se puede desempaquetar en un FOR
# print(zip(*mylist))
# for i in zip(*mylist):
#     print(i)

transponse = [list(i) for i in zip(*mylist)]
print(transponse)

print()
matrix= [   [0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,1,0],
            [0,1,0,0,1,0,1,1],
            [0,1,0,0,1,0,0,0],
            [0,1,0,1,0,0,1,0],
            [1,0,0,1,0,1,0,1],
            [0,1,1,1,0,1,0,1],
            [0,0,0,0,0,0,1,1],
            ]

bordes = [] 

print(matrix[0])
print(matrix[-1])

matrix_x = len(matrix[0])
matrix_y = len(matrix)
matrixH = [list(i) for i in zip(*matrix)]

print(matrixH[0][1:-1])
print(matrixH[-1][-2:0:-1])

print(matrixH[0][1:-1].count(0))
print(matrixH[-1][-2:0:-1].count(0))
