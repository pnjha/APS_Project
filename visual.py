import pygraphviz as pgv
import networkx as nx
import itertools as it
import planarity 
import random
from networkx.algorithms import bipartite
import numpy as np
import networkx as nx

# np.set_printoptions(threshold=np.nan)

x,y = np.loadtxt('planar_100_nodes.txt', delimiter = "\t", unpack = True)

G = nx.Graph()
G.add_nodes_from([1,100])


for x1,y1 in zip(x,y):
	x1 = int(x1)
	y1 = int(y1)
	G.add_edge(x1,y1,weight = random.randint(1,1001))

print "Is planar: ",planarity.is_planar(G)
print "Is connected: ",nx.is_connected(G)


A = nx.adjacency_matrix(G)
b = A.todense()

graph = []

# for lst in b:
# 	graph.append(list(lst))        


# print( type(A))
# print  type(b)
# print b[0][0]
# print( type(graph))
# print b

print float('inf')
graph = nx.to_numpy_matrix(G)

# graph = b.ravel().tolist()
print graph[0,2]

for x in np.nditer(graph, op_flags = ['readwrite']):
	if x == 0:
		 x[...] = float('inf')


# print type(graph)
print graph

# counter = 0
# llist = []
# temp = []
# for item in graph:
# 	counter += 1
# 	if counter == 11:
# 		llist.append(temp)
# 		temp = []
# 		counter = 0
# 	else:
# 		if item == 0:
# 			item == 99999
# 		temp.append(item)	

# print llist

# print(graph)

# for r in b:
# 	for b in r:
# 		print(b)

# with open('my_file.txt', 'w') as f:
# 	for item in llist:
# 		f.write("%s\n"% item)

# for r in b:
# 	print(*r)


















# #create random planar graph with n nodes and p probability of growing
# n=100
# p=0.6
# # while True:
# #     G=nx.gnp_random_graph(n,p)
# #     if is_planar(G)[0]:
# #         break

# while True:
#     G=nx.gnp_random_graph(n,p)
#     x = planarity.is_planar(G) 
#     print x
#     if x == True:
#         break
# # G = nx.grid_2d_graph(10, 10, periodic=False, create_using=None)
# # print G

# print "done"

# #visualize with pygraphviz
# A=pgv.AGraph()
# A.add_edges_from(G.edges())
# A.layout(prog='dot')
# A.draw('planar.png')

# import networkx as nx 

# # complete graph of 8 nodes, K8 
# G8=nx.complete_graph(8) 

# # K8 is not planar 
# print(planarity.is_planar(G8)) 

# # Will display false because G8...