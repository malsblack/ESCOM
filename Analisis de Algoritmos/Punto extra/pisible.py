class grafoo:
    def __init__(self,arista,n):
        self.adjlist=[[] for _ in range(n)]
        for (src, dest) in arista:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
def hamilton(graph, v, visited, path, n):
    if len(path) == n:
        print(path)
        return

    for w in graph.adjList[v]:
        if not visited[w]:
            visited[w] = True
            path.append(w)
            hamilton(graph, w, visited, path, n)
            visited[w] = False
            path.pop()

def encontrarcamino(graph, n):
    for start in range(n):
        path = [start]
        visited = [False] * n
        visited[start] = True
        hamilton(graph, start, visited, path, n)