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

G = nx.Graph()
G.add_weighted_edges_from(lst)
G2 = nx.Graph()
G2.add_weighted_edges_from(lst)
#print(G.edge)
#nx.draw(G)
#plt.show()
#print(G.edge[11])
#G.remove_edge(0,1)
#print(G.edges())

'''
print(G.degree(11), G.degree(1))
s = set(G.edge[11])
t = set(G.edge[1])
print(s)
print(t)
'''

''''''
theta = 1.1
cnt = cnt1 = cnt2 = cnt3 = cnt4 = 0
for j in G.edges():
    #print(G.degree(j[0]), G.degree(j[1]))
    index = 0 if G.degree(j[0]) < G.degree(j[1]) else 1
    dmin = min(G.degree(j[0]), G.degree(j[1]))
    #print(index,dmin)
    if dmin <= 2:
        #cnt1 += 1
        continue
    if dmin == 3:
        #cnt4 += 1
        neig = list(G.edge[j[index]])
        maxi = 0
        for temp in neig:
            maxi = max(G.degree(temp), maxi)
        if maxi <= dmin:
            #cnt2 += 1
            continue
    s, t = set(G.edge[j[0]]), set(G.edge[j[1]])
    com = s & t
    cnt += 1
    #print(cnt, len(com)/len(s),len(com)/len(t))
    if len(com)/len(s) < theta and len(com)/len(t) < theta:
        #cnt3 += 1
        #print('Y')
        G2.remove_edge(j[0], j[1])
#print(cnt1, cnt4, cnt2, cnt3)
#print(G.edges())
#print(tt.edges())
print(set(G.edges()) - set(G2.edges()))
# for pp in G.edges():
#     print(pp[0], pp[1])

'''
neig = list(G.edge[0])
print(neig)
maxi = 0
for temp in neig:
    print(G.degree(temp),end=' ')

'''