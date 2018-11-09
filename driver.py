import time
import sys
import pygraphviz as pgv
import networkx as nx
import itertools as it
import planarity 
import random
from networkx.algorithms import bipartite
import numpy as np
import networkx as nx
import snowball as sb
import floydWarshall as fw
import matplotlib.pyplot as plt



vertex = [50,100,1000,5000]

def createMatrix(vertices):

	#************* Reading from file ****************************************

	filename = 'planar_'+str(vertices)+'_nodes.txt'

	x,y = np.loadtxt(filename, delimiter = "\t", unpack = True)

	#************************************************************************

	#************ Generating Incident Matrix ********************************

	G = nx.Graph()
	G.add_nodes_from([1,vertices])


	for x1,y1 in zip(x,y):
		x1 = int(x1)
		y1 = int(y1)
		G.add_edge(x1,y1,weight = random.randint(1,1001))

	#**************************************************************************

	#************ Generating 2D adjacency matric ******************************

	A = nx.adjacency_matrix(G)
	b = A.todense()

	gr = []
	gr = nx.to_numpy_matrix(G)
	llist = []
	graph = []
	counter = 0
	c = 0
	for x in np.nditer(gr):
		c += 1
		if counter == vertices:
			counter = 0
			graph.append(llist)
			llist = []

		if x == 0:
			llist.append(float('inf'))
			counter += 1
		else:
			llist.append(int(x))
			counter += 1	
	return graph		

#************************************************************************

#***************** Executing and measuring time **************

vertex = [50,100]

def createMatrix(vertices):

	#************* Reading from file ****************************************

	filename = 'planar_'+str(vertices)+'_nodes.txt'

	x,y = np.loadtxt(filename, delimiter = "\t", unpack = True)

	#************************************************************************

	#************ Generating Incident Matrix ********************************

	G = nx.Graph()
	G.add_nodes_from([1,vertices])


	for x1,y1 in zip(x,y):
		x1 = int(x1)
		y1 = int(y1)
		G.add_edge(x1,y1,weight = random.randint(1,1001))

	#**************************************************************************

	#************ Generating 2D adjacency matric ******************************

	A = nx.adjacency_matrix(G)
	b = A.todense()

	gr = []
	gr = nx.to_numpy_matrix(G)
	llist = []
	graph = []
	counter = 0
	c = 0
	for x in np.nditer(gr):
		c += 1
		if counter == vertices:
			counter = 0
			graph.append(llist)
			llist = []

		if x == 0:
			llist.append(float('inf'))
			counter += 1
		else:
			llist.append(int(x))
			counter += 1	
	return graph		

#************************************************************************

#***************** Executing and measuring time **************

FTIME = []
STIME = []

for value in vertex:

	graph = createMatrix(value)

	start = time.time()
	fw.floydWarshall(graph,value)
	end = time.time()
	FTIME.append(end - start)


	flag, graph = sb.DPC(graph,value)		

	if flag == True:
		start = time.time()
		sb.snowball(graph,value)
		end = time.time()
		STIME.append(end - start)

# for duration in FTIME:
# 	print duration

# for duration in STIME:
# 	print duration

plt.plot(vertex, FTIME, 'r--', label = 'Floyd Warshall Algorithm')
plt.plot(vertex, STIME, 'b--', label = 'Snowball Algorithm')	
# plt.xscale("log")
plt.xlabel('vertices')
plt.ylabel('Running time (seconds)')
plt.title('Comparision of Floyd Warshall Algorithm and Snowball Algorithm')
plt.legend()
plt.show()
