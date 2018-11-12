import os
import random

nodeslist = [10,50,100,500,1000,5000,20000,50000,200000]

for node in nodeslist:
	filename = "planar_"+str(node)+"_nodes.txt"
	fileLines = []
	with open(filename) as f:
	    for line in f:
	    	line = line.rstrip('\n')
	    	temp = line.split('\t')
	    	weight = random.randint(-100, 100)
	    	# print temp
	    	line = str(temp[0])+"\t"+str(temp[1]) + "\t" + str(weight)+"\n"
	    	del temp[:]
	    	fileLines.append(line)
	
	fname = "planar_"+str(node)+"_nodes_negative.txt"
	    	
	f= open(fname,"w+")    	

	for item in fileLines:
		f.write(item)

	f.close()

	del fileLines[:]