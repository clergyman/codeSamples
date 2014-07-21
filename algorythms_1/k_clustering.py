#implements the k-clustering greedy algorythm

#the graph should be represented by Nodes to implement union-find
#the list of edges should be present too, to implement the greedy algorythm edge choice

# the input file is as follows:
# [number_of_nodes]
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]

class Node:
	def __init__(self, ident=0):
		self.id = ident
		self.leader = ident
		
	def isLeader(self) : return self.id == self.leader



class Edge:
	def __init__(self, node1, node2, dist):
		self.start = node1
		self.end = node2
		self.distance = dist
		
class SimpleGraph:
	def __init__(self):
		self.Nodes = []
		self.Edges = []

		
	# input file example
	# 500
	# 1 2 6808
	# 1 3 5250
	# 1 4 74
	# 1 5 3659
	# 1 6 8931
	# 1 7 1273
	# 1 8 7545
	def populateFromFile (self, filename):
		f = open(filename, 'r')
		
		for line in f:
			lineData = map(int,line.strip().split( ));
			
			if len(lineData) < 3: #this is 1st row - the one with number of nodes
				#populate the initial nodes with themselves as leaders
				self.Nodes  = [Node(i) for i in range(1,(lineData[0])+1)] #the list of nodes is done
			else:
				self.Edges.append(Edge(*lineData)) #one line one edge		


	def NodeById(self, ID):
		listCandidate = [n for n in self.Nodes if n.id == ID]
		if (listCandidate): return listCandidate[0]
		else : return None
		
	def getLeader(self, ID):
		n = self.NodeById(ID)
		pretendent = n
		while (not pretendent.isLeader()):
			pretendent = self.NodeById(pretendent.leader)
			
		#print("Get Leader working: ID: " + str(ID)+ " leader: "+str(pretendent.id))
		return pretendent.id
		
	def mergeClusters(self, old, new):
		oldLeaderID = self.getLeader(old)
		newLeaderID = self.getLeader(new)
		
		oldLeader = [n for n in self.Nodes if n.id == oldLeaderID][0]
		oldLeader.leader = newLeaderID
		
		#print("Merging cluster with leader " + str(oldLeaderID)+ " with leader: "+str(newLeaderID))
		
				
	def clusterNum(self):
		leaders = [self.getLeader(nod.id) for nod in self.Nodes]
		return len(set(leaders))
		
	def inTheSameCluster(self,ID1, ID2):
		lead1 = self.getLeader(ID1)
		lead2 = self.getLeader(ID2)
		
		return lead1 == lead2
		
	def clasterify(self, K):
		
		sortedEdges = sorted(self.Edges, key = lambda edge : edge.distance)
		i = 0
		while (self.clusterNum() > K):
			edgeCandidate = sortedEdges[i]
			print("checking edge # "+str(edgeCandidate.distance)+" number of clusters: "+str(self.clusterNum()))
			i=i+1
			if not self.inTheSameCluster(edgeCandidate.start, edgeCandidate.end):
				self.mergeClusters(edgeCandidate.start, edgeCandidate.end)
			
		#find the next max dist since we've finished with the loop
		
		while True:
			edgeCandidate = sortedEdges[i]
			if not self.inTheSameCluster(edgeCandidate.start, edgeCandidate.end):
				break
			else:
				i=i+1
		
		print("THE NEXT EDGE: "+str(sortedEdges[i].distance))	
		
				
g1 = SimpleGraph()
g1.populateFromFile("clustering1.txt")
#g1.populateFromFile("clustering1.txt")
g1.clasterify(4)
print("Done")