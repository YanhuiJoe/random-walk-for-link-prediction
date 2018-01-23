'''#*.*_coding = utf-8_*.*'''

import pandas as pd
import networkx as nx
import numpy as np
import math
import matplotlib.pyplot as plt

#import the graph to Networkx
df = pd.read_csv('edge.txt',sep='\t', encoding='latin1')
lst = []
for i in range(df.shape[0]):
    a, b, c = df['a'][i], df['b'][i], df['c'][i]
    lst.append((a,b,c))

G = nx.Graph()
G.add_weighted_edges_from(lst)

#caculate the average shortest path length of the network
aspl = nx.average_shortest_path_length(G)
shortest_path_len = math.ceil(aspl)
#
matrixA = np.zeros((len(G),len(G)))
matrixD = np.zeros((len(G),len(G)))
matrixP = np.zeros((len(G),len(G)))

allSumWeight = sum(G.get_edge_data(weig[0],weig[1])['weight']for weig in G.edges())
# print(allSumWeight)
''''''
for j in G.edges(data='weight'):
    matrixA[j[0]][j[1]] = matrixA[j[1]][j[0]] = j[2]
    U, V = G.neighbors(j[0]), G.neighbors(j[1])
    sumU = sum(G.get_edge_data(j[0],pp)['weight']for pp in U)
    sumV = sum(G.get_edge_data(j[1],qq)['weight'] for qq in V)
    matrixP[j[0]][j[1]], matrixP[j[1]][j[0]] = j[2]/sumU, j[2]/sumV

for dm in range(matrixD.shape[0]):
    matrixD[dm][dm] = 1./sum(matrixA[dm])

M = np.dot(matrixD, matrixA)
# print(matrixA)
# print(matrixD)
# print(matrixP)
''''''
def piVector(t, x):
    if t == 0:
        arr1 = np.zeros(len(G))
        arr1[x] = 1
        return np.dot(matrixP.transpose(),arr1)
    else:
        return np.dot(matrixP.transpose(),piVector(t-1, x))

def Res(u, v, shortest_path_len):

    LRW = (1./(2*allSumWeight))*(sumWeight(u)*piVector(shortest_path_len,u)[v]+sumWeight(v)*piVector(shortest_path_len,v)[u])
    return LRW

def sumWeight(tNode):
    V = G.neighbors(tNode)
    return sum(G.get_edge_data(tNode,qq)['weight'] for qq in V)

for edge in G.edges(data='weight'):
    print(edge, end='\t')
    LRW = Res(edge[0],edge[1],shortest_path_len)
    print("LRW:", LRW,end='\t')
    SRW = 0
    for sp in range(shortest_path_len):
        SRW += Res(edge[0], edge[1], sp)
    print("SRW:", SRW)
