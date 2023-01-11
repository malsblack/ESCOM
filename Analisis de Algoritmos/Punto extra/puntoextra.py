import networkx as nx
import random
import ast



def hamilton(grafo, comienzo, visitado, estado, n):
    if len(estado) == n:
        print(estado)
        return

    for w in grafo.adjList[comienzo]:
        if not visitado[w]:
            visitado[w] = True
            estado.append(w)
            hamilton(grafo,comienzo,visitado,estado,n)
            visitado[w] = False
            estado.pop()


def recorrido(grafo,n):
    for comienzo in range(n):
        estado=[comienzo]
        visitado=[False]*n
        visitado[comienzo]=True
        hamilton(grafo,comienzo,visitado,estado,n)



n=int(input("Ingresa el tamaño del nodo: \n"))
nodos=[]
aristas=[]
aristas2=[]

for i in range(n):
    nodos.append(input("Ingresa el nodo: {}\n".format(i+1)))
    aristas.append(tuple(input("Ingresar la arista del nodo {} en forma 'ABC.....'\n").format(i+1)))

grafo=nx.Graph() #Se crea el nodo
for i in nodos:
    grafo.add_node(i)


grafo.add_edges_from(aristas)

print(aristas)
print(grafo.edges)
recorrido(grafo,n)

