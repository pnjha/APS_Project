
def floydWarshall(dist,vertices): 

	for k in range(vertices-1): 
		for i in range(vertices-1): 
			for j in range(vertices-1): 
				dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j]) 
	# printSolution(dist) 

def printSolution(dist,vertices): 
	print "Shortest distances between every pair of vertices" 
	for i in range(vertices-1): 
		for j in range(vertices-1): 
			if(dist[i][j] == float('inf')): 
				print float('inf'), 
			else: 
				print "%7d\t" %(dist[i][j]), 
			if j == vertices-1: 
				print "" 
