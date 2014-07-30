import sys
import numpy as np

class Node:
	def __init__(self, ident=0):
		self.neibhours = []
		self.id = ident
		self.explored = False
		self.allNeibhoursExplored = False
		self.shortestPaths = []
		self.shortestPaths.append( (self,0) )
		self.weight = 0
	
	def verbose(self):
		return ("ID: "+str(self.id)+ "Neibs: "+str(self.neibhours))

class Arc:
	def __init__(self,T,H,LEN):
		self.tail = T
		self.head = H
		self.length = LEN
	
	def verbose(self):
		return ("Tail: "+str(self.tail)+ " Head: "+str(self.head)+ " len: "+str(self.length))


class DirGraph:
	def __init__(self):
		self.Nodes = []
		self.Arcs	= []

	def populateFromFile (self, filename):
		f = open(filename, 'r')

		metadata = f.readline().strip().split(" ")
		numNodes = int(metadata[0])
		numEdges = int(metadata[1])

		for i in range (0,numNodes + 1):
			self.Nodes.append(Node(i)) # Node#0 is thespecial Node for reweighting procedure
			if not i == 0: #Nodes[0] laready exists
				self.Nodes[0].neibhours.append( (i,0) ) #outcoming arc from 0th to i-th node
				self.Arcs.append(Arc(0,i,0))

		for line in f:
			lineData = map(int,line.strip().split(" "))

			if len(lineData) < 3: continue

			tail = lineData[0]
			head = lineData[1]
			length = lineData[2]

			self.Nodes[tail].neibhours.append( (head, length) )
			self.Arcs.append(Arc(tail,head,length))
			
		for node in self.Nodes:
			print node.verbose() 
			
		for arc in self.Arcs:
			print arc.verbose() 
	
	
	def inArcs(self, Id):
		res = [a for a in self.Arcs if a.head == Id]
		
		if res:
			#r = [a.verbose() for a in res]
			#print "NODE#", str(Id), " incoming arcs:", r
		
			return res
		else: return []

	def BellmanFord(self,src):
		n = len(self.Nodes)
		
		INF = np.iinfo('int32').max
		A = np.ones([n+1,n],'int32')*INF
		A[0,src] = 0
		for i in range(1,n+1):
			print
			print "budget ",i
			for nod in self.Nodes:
				print "node", nod.verbose()
				a1 = A[i-1,nod.id]
				a2 = INF
				for e in self.inArcs(nod.id):
					p1 = A[i-1,e.tail]
					if p1 < INF : a3 = A[i-1,e.tail] + e.length
					else: a3 = INF
					print "incoming arc: ", e.verbose()
					#a3 = A[i-1,e.tail] + e.length
					a2 = a3 if a3 < a2 else a2
				print "a1 ", a1, " a2 ", a2
				A[i,nod.id] = min(a1,a2)
			print "budget res:"
			print A

		has_neg_cycles = False
		for i in range(n):
			if not A[n-1,i] == A[n,i]:
				has_neg_cycles = True
				break

		return A[n-1] if not has_neg_cycles else []


g1 = DirGraph()
g1.populateFromFile('input\TC1.txt')

sys.stdout.write(str(g1.BellmanFord(0)))
