import networkx as nx
vis = []
v = []

G = nx.Graph()

import sys
f = open(sys.argv[1],"r")
list_vertice = []
nv = int(f.readline())
#print (nv)
v = f.readline().replace("\n","").split(" ")
#print (v)
G.add_nodes_from(v)
ne = int(f.readline())
for x in range(ne):
    edge = f.readline().replace("\n","").split(" ")
    G.add_edge(edge[0],edge[1])

f.close()

print("lista de vértices:")
print(v)
#verifica lista de visinhos
# v é a lista de arestas
# vs é um determinado indice
# retorno é a lista de vértices visinhos
print("visinhos do nó ",v[2],":")
print(list(G.adj[v[2]]))



#comando abaixo irá desenhar o grafo
import matplotlib.pyplot as plt
options = {
    "font_size": 5,
    "node_size": 100,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 1,
    "with_labels":True, 
    "font_color":"red",
    "arrowsize":10,
}
nx.draw_networkx(G,
    pos=nx.spring_layout(G), 
    **options
    )

plt.savefig('demo.pdf')
#print (G.number_of_nodes())
#print (G.number_of_edges())


               
        
