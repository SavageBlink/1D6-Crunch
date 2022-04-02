# This code is contributed by pratham76
# Python3 implementation to find the
# shortest path in a directed
# graph from source vertex to
# the destination vertex

INFINITE = 1000000000

class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second

# Class of the node
class Node:
	# Adjacency list that shows the
	# vertexNumber of child vertex
	# and the weight of the edge
	def __init__(self, vertexNumber):	
		self.vertexNumber = vertexNumber
		self.children = []

	# Function to add the child for
	# the given node
	def Add_child(self, vNumber, length):
		p = Pair(vNumber, length);
		self.children.append(p);
	
# Function to find the distance of
# the node from the given source
# vertex to the destination vertex
# returns dist = [distnode1, distnode2, ...], path = [previousnode1, previousnode2, ...]
def dijkstraDist(network, startNode):
	# Stores distance of each
	# vertex from source vertex
	path = []
	dist = [INFINITE for i in range(len(network))]
	
	# bool array that shows
	# whether the vertex 'i'
	# is visited or not
	visited = [False for i in range(len(network))]
	
	for i in range(len(network)):	
		path.append(-1)
	dist[startNode] = 0
	path[startNode] = -1
	current = startNode
	
	# Set of vertices that has
	# a parent (one or more)
	# marked as visited
	sett = set()	
	while True:
		# Mark current as visited
		visited[current] = True
		for i in range(len(network[current].children)):
			v = network[current].children[i].first
			if visited[v]:
				continue
			
			# Inserting into the
			# visited vertex
			sett.add(v)
			alt = dist[current] + network[current].children[i].second
			
			# Condition to check the distance
			# is correct and update it
			# if it is minimum from the previous
			# computed distance
			if alt < dist[v]:
				dist[v] = alt
				path[v] = current
		if current in sett:
			sett.remove(current)
		if len(sett) == 0:
			break
		
		# The new current
		minDist = INFINITE
		index = 0
		
		# Loop to update the distance
		# of the vertices of the graph
		for a in sett:
			if dist[a] < minDist:
				minDist = dist[a]
				index = a
		current = index
	return dist, path

# Function to print the path
# from the source vertex to
# the destination vertex
def printPath(path, i, s):
	if i != s:
		# Condition to check if
		# there is no path between
		# the vertices
		if (path[i] == -1):
			print("Path not found!!")
			return
		printPath(path, path[i], s)
		print(str(path[i]) + " ")

def getPath(path, startNode, destNode):
	if destNode == startNode:
		return [startNode]
	else:
		# Condition to check if
		# there is no path between
		# the vertices
		if (path[destNode] == -1):
			return []; # path not found
		else:
			p = getPath(path, startNode, path[destNode])
			p.append(destNode)
			return p

#nodes = [node1, node2, ...]
#arcs = [
#[node1, node2, cost1],
#[node3, node4, cost2],
#...
#]
def parseNetwork(nodes, arcs):
	network = []
	
	# Loop to create the nodes
	for i in range(len(nodes)):
		a = Node(nodes[i])
		network.append(a)
	
	for i in range(len(arcs)):
		if network[arcs[i][0]] and network[arcs[i][1]]:
			network[arcs[i][0]].Add_child(arcs[i][1], arcs[i][2])
	
	return network

# Driver Code
if __name__=='__main__':
	nodes = [0, 1, 2, 3, 4]
	
	arcs = [
		[0, 1, 1],
		[0, 2, 4],
		[1, 2, 2],
		[1, 3, 6],
		[2, 3, 3],
	]
	
	startNode = 1
	dist, path = dijkstraDist(parseNetwork(nodes, arcs), startNode)

	# Loop to print the distance of
	# every node from source vertex
	print("Distances")
	for i in range(len(dist)):
		if dist[i] == INFINITE:
			print("{} -> {}: {}".format(startNode, i, "IMPOSSIBLE"))
		else:
			print("{} -> {}: {}".format(startNode, i, dist[i]))
	
	print()
	print("Path")
	for i in range(len(nodes)):
		p = getPath(path, startNode, nodes[i]);
		if len(p) == 0:
			print("{} -> {}: {}".format(startNode, nodes[i], "IMPOSSIBLE"))
		else:
			s = "{} -> {}: ".format(startNode, nodes[i])
			for j in range(len(p) - 1):
				s = s + str(p[j]) + " -> "
			s = s + str(p[len(p) - 1])
			print(s)
	#print(dist)
	#print(path)
	#printPath(path, 3, startNode)