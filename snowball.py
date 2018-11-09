
def DPC(graph,vertices):

    for k in range(vertices-2, -1, -1):
        for j in range(0,k):
            for i in range(0,j):
                if graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])    
                if graph[j][k] != float('inf') and graph[k][i] != float('inf'):
                    graph[j][i] = min(graph[j][i], graph[j][k]+graph[k][i])
                if graph[i][j]+graph[j][i] < 0:
                    return False
    return True ,graph

def snowball(dist,vertices):
    graph = dist
    for k in range(vertices-1):
        for j in range(k-1, 0, -1):
            for i in range(0, k):
                dist[i][k] = min(dist[i][k], dist[i][j]+graph[j][k])
                dist[k][i] = min(dist[k][i], dist[j][i]+graph[k][j])


def executesnowball(graph,vertices):
    flag, graph = DPC(graph,vertices)
    if  flag == False:
        print "Input graph is not consistent"
    else:
        snowball(graph,vertices)    


def printSolution():
    for i in range(0, vertices):
        for j in range(0, vertices):
            if dist[i][j] == float('inf'):
                print float('inf')
            else:    
                print dist[i][j]
        print ""
