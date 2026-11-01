from collections import deque

def bfs(grafo, inicio):
    visitados = {inicio}
    fila = deque([inicio])
    ordem = []

    while fila:
        atual = fila.popleft()
        ordem.append(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return ordem


def dfs(grafo, inicio):
    visitados = set()
    ordem = []

    def explorar(atual):
        visitados.add(atual)
        ordem.append(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                explorar(vizinho)

    explorar(inicio)
    return ordem

# Grafo de Teste (Lista de Adjacência)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print("BFS:", bfs(grafo, 'A'))
print("DFS:", dfs(grafo, 'A'))
