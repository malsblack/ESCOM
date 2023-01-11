import networkx as nx
import random
import ast




n=int(input("Ingresa el tamaño del nodo: \n"))
nodos=[]
aristas=[]

for i in range(n):
    nodos.append(input("Ingresa el nodo: {}\n".format(i+1)))
    aristas.append(ast.literal_eval(input("Ingresa la arista del nodo {} en forma '(nodo,arista)'\n".format(i+1))))

grafo=nx.Graph() #Se crea el nodo

for i in aristas:
    print(i)