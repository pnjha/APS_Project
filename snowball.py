#!/usr/bin/python3

import sys

INF = 9999999
SIZE = 4

dist = [
            [0, INF, INF, INF],
            [INF, 0, INF, INF],
            [INF, INF, 0, INF],
            [INF, INF, INF, 0]
        ]


graph = [
            [0,   5,  INF, 10], 
            [INF, 0,   3, INF], 
            [INF, INF, 0,   1], 
            [INF, INF, INF, 0]
        ]

# graph = [
#             [0, 1, INF, INF],
#             [INF, 0, -1, INF],
#             [INF, INF, 0, -1],
#             [-1, INF, INF, 0]
#         ]


def DPC():
    for k in range(SIZE-1, -1, -1):
        for j in range(0, k):
            for i in range(0, j):
                if graph[i][k] != INF and graph[k][j] != INF:
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])    
                if graph[j][k] != INF and graph[k][i] != INF:
                    graph[j][i] = min(graph[j][i], graph[j][k]+graph[k][i])
                if graph[i][j]+graph[j][i] < 0:
                    return False
    return True

def snowball():
    for k in range(0, SIZE):
        for j in range(k-1, -1, -1):
            for i in range(0, k):
                # if dist[i][j] != INF and graph[j][k] != INF:
                dist[i][k] = min(dist[i][k], dist[i][j]+graph[j][k])
                # if dist[j][i] != INF and graph[k][j] != INF:
                dist[k][i] = min(dist[k][i], dist[j][i]+graph[k][j])


# Execution starts from here
if DPC() == False:
    sys.exit("Input graph is not consistent")

# print("Graph after DPC is:")
# for i in range(0, SIZE):
#     for j in range(0, SIZE):
#         print(graph[i][j], end=" ")
#     print("\n")

snowball()

for i in range(0, SIZE):
    for j in range(0, SIZE):
        if dist[i][j] == INF:
            print("∞", end=" ")
        else:    
            print(dist[i][j], end=" ")
    print("\n")
