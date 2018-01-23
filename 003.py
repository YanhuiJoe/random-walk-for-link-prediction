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
# G2 = nx.Graph()
# G2.add_weighted_edges_from(lst)

#caculate the average shortest path length of the network
aspl = nx.average_shortest_path_length(G)
shortest_path_len = math.ceil(aspl)
#
matrixA = np.zeros((len(G),len(G)))
matrixD = np.zeros((len(G),len(G)))
matrixP = np.zeros((len(G),len(G)))
# print(matrix)
for j in G.edges():
    matrixA[j[0]][j[1]] = matrixA[j[1]][j[0]] = 1
    matrixP[j[0]][j[1]], matrixP[j[1]][j[0]] = 1./G.degree(j[0]), 1./G.degree(j[1])
# print(matrixA.shape)
# print(matrixA)
# print(matrixP)
for dm in range(matrixD.shape[0]):
    matrixD[dm][dm] = 1./G.degree(dm)
# print(matrixD)
M = np.dot(matrixD, matrixA)
# print(M)

def piVector(t, x):
    if t == 0:
        arr1 = np.zeros(len(G))
        arr1[x] = 1
        return np.dot(matrixP.transpose(),arr1)
    else:
        return np.dot(matrixP.transpose(),piVector(t-1, x))
# print(piVector(0))
# print(piVector(1))
# print(piVector(2))
# print(piVector(3, 2))
def Res(u, v, shortest_path_len):

    LRW = (1./(2*G.number_of_edges()))*(G.degree(u)*piVector(shortest_path_len,u)[v]+G.degree(v)*piVector(shortest_path_len,v)[u])
    return LRW

for edge in G.edges():
    print(edge, end='\t')
    print("LRW:", Res(edge[0],edge[1],shortest_path_len),end='\t')
    SRW = 0
    for sp in range(shortest_path_len):
        SRW += Res(edge[0], edge[1], sp)
    print("SRW:", SRW)
