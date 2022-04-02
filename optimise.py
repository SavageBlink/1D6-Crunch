from parse import Parsing
from dijkstra import *

def optimise(parsed, startNode, endNode):
	nodesStart = [int(x) for x in parsed["noeudStart"]]
	nodesEnd = [int(x) for x in parsed["noeudEnd"]]
	consumption = [float(x) for x in parsed["consommation"]]

	nodes = [int(x) for x in list(set(nodesStart).union(parsed["noeudEnd"]))]
	arcs = []

	for i in range(len(nodesStart)):
		arcs.append([nodesStart[i], nodesEnd[i], consumption[i]])

	network = parseNetwork(nodes, arcs)
	dist, path = dijkstraDist(network, startNode)
	p = getPath(network, path, startNode, endNode)
	#d = getDist(network, dist, endNode)
	r = []
	for i in range(len(p) - 1):
		for j in range(len(arcs)):
			if arcs[j][0] == p[i] and arcs[j][1] == p[i + 1]:
				r.append([p[i], p[i + 1], arcs[j][2]])
				break
	return r

# Driver Code
"""if __name__=='__main__':
	r = optimise(Parsing("consommation_jeu_de_donnee.txt"), 1, 10000)
	c = 0
	for i in range(len(r)):
		c = c + r[i][2]
	print("Consumption: ", c)
	print(r)"""

def formatOptimise(start,end,filename= None):
	if(filename == None):
		filename = "consommation_jeu_de_donnee_faux.txt"
	print("In formatOptimise")
	r = optimise(Parsing(filename), start, end)
	c = 0
	for i in range(len(r)):
		c = c + r[i][2]
	#print("Consumption: ", c)
	print("returning r...")
	return r
