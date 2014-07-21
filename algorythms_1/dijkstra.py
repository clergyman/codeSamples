import sys

class Node:
	def __init__(self, ident=0, adjacencyList=None):
		self.neibhours = adjacencyList
		self.id = ident
		self.explored = False
		self.allNeibhoursExplored = False
		self.shortestPaths = []
		self.shortestPaths.append( (self,0) )
		
class SimpleGraph:
	def __init__(self):
		self.Nodes = []
	
	def populateFromFile (self, filename):
		f = open(filename, 'r')
		
		for line in f:
			lineData = line.strip().split("\t");
			idCounter = int(lineData[0])
			neibhourList = [(tuple(map(int,elem.split(',')))) for elem in lineData[1:]]
			self.Nodes.append(Node(idCounter,neibhourList))
		
		self.nodeQuant = len(self.Nodes)
			
	def countShortestPaths(self, srcVertex):
		
		sys.stdout.write(str(self.Nodes[0].id)+"\n")
		sys.stdout.write(str(srcVertex)+"\n")
		
		sourceVertex =  [x for x in (self.Nodes) if (x.id == srcVertex)][0]
		sys.stdout.write(str(sourceVertex)+"\n")
		candidate = (sourceVertex,100000)
		weHaveACandidate = True
		
		while (weHaveACandidate):
			newPath = 100000
			weHaveACandidate = False
			for item in sourceVertex.shortestPaths:
				
		
				if item[0].allNeibhoursExplored: continue
				oldPath = item[1]
				for cnd_tuple in item[0].neibhours:
					cnd = [x for x in (self.Nodes) if (x.id == cnd_tuple[0])][0]
					if (cnd).explored: continue
					if (oldPath+cnd_tuple[1]) < newPath:
						newPath = oldPath+cnd_tuple[1]
						candidate = (cnd,newPath)
						weHaveACandidate = True
			
			sourceVertex.shortestPaths.append( (candidate[0], newPath) )
			candidate[0].explored = True
			if set([i[0] for i in candidate[0].neibhours]).issubset(set(([i[0] for i in sourceVertex.shortestPaths]))):
				candidate.allNeibhoursExplored=True
		
		for path in sourceVertex.shortestPaths:
			sys.stdout.write(str(path[0].id)+" ->>>>>>>>> "+str(path[1])+"\n")
	
				
			
			
g1 = SimpleGraph()
g1.populateFromFile('dijkstraData.txt')
g1.countShortestPaths(1)
sys.stdout.write(str(g1.Nodes[0].neibhours[0]))
			