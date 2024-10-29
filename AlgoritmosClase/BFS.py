# https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

def bfs(grafo, inicio):
    visitados = []
    cola= [inicio]
    while cola:
        nodo_actual = cola.pop(0)
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)
          
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                cola.append(vecino)
    return visitados


grafo = {"A": ["B", "D"],
         "B":["A","C", "E"],
         "C":["B",],
         "D":["A","E", "F"],
         "E":["A","D"],
         "F":["D"],
         }

print(f"Orden de visita {bfs(grafo, "A")}")