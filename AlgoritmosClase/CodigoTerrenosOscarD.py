#CODIGO NO ES MIO, ES DE UN COMPAÑERO
from typing import List

def checar_alrededor(posicion: tuple, matriz: List[List[int]]) -> bool:
    x = posicion[0]
    y = posicion[1]
    rows = len(matriz)
    cols = len(matriz[0])
    if x + 1 < rows and matriz[x + 1][y] == 5:
        return True
    elif x - 1 >= 0 and matriz[x - 1][y] == 5:
        return True
    elif y + 1 < cols and matriz[x][y + 1] == 5:
        return True
    elif y - 1 >= 0 and matriz[x][y - 1] == 5:
        return True
    else:
        return False

def revisar_condicion(posicion: tuple, matriz: List[List[int]], matriz_temporal: List[List[int]]) -> List[List[int]]:
    x = posicion[0]
    y = posicion[1]
    if ((x == 0 or x == (len(matriz) - 1)) or (y == 0 or y == (len(matriz[0]) - 1))) or checar_alrededor(posicion, matriz_temporal):
        matriz_temporal[x][y] = 5 #este es el valor considerado como abierto
    else:
        if matriz[x][y] == 1:
            if x + 1 < len(matriz) and matriz_temporal[x+1][y] == 0:
                matriz_temporal = revisar_condicion((x+1, y), matriz, matriz_temporal)
            if x - 1 >= 0 and matriz_temporal[x-1][y] == 0:
                matriz_temporal = revisar_condicion((x-1, y), matriz, matriz_temporal)
            if y + 1 < len(matriz[0]) and matriz_temporal[x][y+1] == 0:
                matriz_temporal = revisar_condicion((x, y+1), matriz, matriz_temporal)
            if y - 1 >= 0 and matriz_temporal[x][y-1] == 0:
                matriz_temporal = revisar_condicion((x, y-1), matriz, matriz_temporal)
    return matriz_temporal

def matriz_revisada(matriz: List[List[int]]) -> List[List[int]]:
    fila = len(matriz)
    matriz_temporal = [row[:] for row in matriz]
    for i in range(contar_ceros(matriz)):
        for i in range(fila):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 0:
                    matriz_temporal = revisar_condicion((i, j), matriz, matriz_temporal)
    return matriz_temporal

def contar_abiertas(matriz: List[List[int]]) -> int:
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 5:
                contador += 1
    return contador

def contar_ceros(matriz: List[List[int]]) -> int:
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                contador += 1
    return contador

def main():
    resultados = []
    casos = input("Ingrese el numero de casos: ")
    for _ in range(int(casos)):
        columnas = input("Ingrese el numero de columnas: ")
        filas = input("Ingrese el numero de filas: ")
        matriz = []
        for _ in range(int(filas)):
            matriz.append([int(i) for i in input()])
        terminado = matriz_revisada(matriz)
        resultados.append(contar_abiertas(terminado))
        for i in terminado:
            print(i)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()