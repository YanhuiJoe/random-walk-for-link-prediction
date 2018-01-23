# x = y = 1
# y = 2
# print(x, y)

#coding = utf-8

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('edge.txt',sep='\t', encoding='latin1')

lst = []

''''''
for i in range(df.shape[0]):
    a, b, c = df['a'][i], df['b'][i], df['c'][i]
    lst.append((a,b,c))

G1 = nx.Graph()
G2 = nx.Graph()
G1.add_weighted_edges_from(lst)
G2.add_weighted_edges_from(lst)
#ss = tt = G1
#G1.remove_edge(1, 0)
# print(G1.edges())
# print(G2.edges())
# print(G1.edge)
# print(G1.get_edge_data(1, 0))
# print(G1.neighbors(0))

# a = nx.k_core(G1)
# print(a)
# print(nx.transitivity(G1))
# print(nx.triangles(G1))
'''
if (1, 0) in G1.edges(1):
    print('Y')
'''


maxd = 0
for md in range(len(G1)):
    maxd = max(maxd, G1.degree(md))
#print(maxd)
#print(G1.edge[1][0]['weight'])
''''''
c0 = c1 = 0
for u in range(len(G1)):
    for v in range(len(G1)):
        for w in range(len(G1)):
            if (u, v) in G1.edges(u) and (u, w) in G1.edges(u) and (v, w) in G1.edges(v):
                c0 += 1
                #print((u, v), (v, w), (u, w), end=' ')
                x, y, z = G1.degree(u), G1.degree(v), G1.degree(w)
                #d, e, f = G1.edge[u][v]['weight'], G1.edge[u][w]['weight'], G1.edge[v][w]['weight']
                #print(d, e, f, end='\t')
                if (x+y>z and y+z>x and x+z>y) or (x==maxd or y==maxd or z==maxd):
                    cnt = 1
                    #print('Yes!')
                else:
                    c1 += 1
                    #print()

print((c0-c1)/c0)
