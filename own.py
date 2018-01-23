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
maxd = max(df['c'])
print(maxd)
G = nx.Graph()
G.add_weighted_edges_from(lst)
G2 = nx.Graph()
G2.add_weighted_edges_from(lst)

theta = 0.5
cnt = cnt1 = cnt2 = cnt3 = cnt4 = 0
for j in G.edges(data='weight'):
    #print(G.degree(j[0]), G.degree(j[1]))
    index = 0 if G.degree(j[0]) < G.degree(j[1]) else 1
    dmin = min(G.degree(j[0]), G.degree(j[1]))
    #print(index,dmin)
    if dmin <= 2:
        continue
    if dmin == 3:

        neig = list(G.edge[j[index]])
        maxi = 0
        for temp in neig:
            maxi = max(G.degree(temp), maxi)
        if maxi <= dmin:
            #cnt2 += 1
            continue
    s, t = set(G.edge[j[0]]), set(G.edge[j[1]])
    com = s & t
    # print(j[0], j[1], end=' : ')
    # print(com)
    comTotalDegree = 0
    for ctd in com:
        comTotalDegree += G.degree(ctd)
    sTotalD = 0
    for sd in s:
        sTotalD += G.degree(sd)
    tTotalD = 0
    for td in t:
        tTotalD += G.degree(td)
    #print(comTotalDegree/sTotalD, comTotalDegree/tTotalD)
    if comTotalDegree/sTotalD < theta and comTotalDegree/tTotalD < theta:

        G2.remove_edge(j[0], j[1])

print(set(G.edges()) - set(G2.edges()))
