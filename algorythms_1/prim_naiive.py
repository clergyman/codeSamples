import sys

class Node:
	def __init__(self, ident=0, adjacencyList=None):
		self.neibhours = adjacencyList
		self.id = ident
		self.explored = False
		self.allNeibhoursExplored = False
		self.shortestPaths = []
		self.shortestPaths.append( (self,0) )
		
	def verbose(self):
		return ( "Node. ID: "+str(self.id)+" neibhourList: "+str(self.neibhours)+" explored: " +str(self.explored)+ "  allexplored: "+str(self.allNeibhoursExplored))
		
		
		
class SimpleGraph:
	def __init__(self):
		self.Nodes = []


	def NodeById(self, ID):
		listCandidate = [n for n in self.Nodes if n.id == ID]
		if (listCandidate): return listCandidate[0]
		else : return None
	
	def allNeibhoursExplored(self, nodeId):
		testNode = self.NodeById(nodeId)
		res = True
			
			
		if testNode :
			for arch in testNode.neibhours:
				if self.NodeById(arch[0]).explored == False:
					res = False
					break
		
			testNode.allNeibhoursExplored = res
			
		return res

	# example of input file
	# 1	80,982	163,8164	170,2620	145,648	200,8021	173,2069	92,647	26,4122	140,546	11,1913	160,6461	27,7905	40,9047	150,2183	61,9146	159,7420	198,1724	114,508	104,6647	30,4612	99,2367	138,7896	169,8700	49,2437	125,2909	117,2597	55,6399	
	# 2	42,1689	127,9365	5,8026	170,9342	131,7005	172,1438	34,315	30,2455	26,2328	6,8847	11,1873	17,5409	157,8643	159,1397	142,7731	182,7908	93,8177	
	# 3	57,1239	101,3381	43,7313	41,7212	91,2483	31,3031	167,3877	106,6521	76,7729	122,9640	144,285	44,2165	6,9006	177,7097	119,7711	
	# 4	162,3924	70,5285	195,2490	72,6508	126,2625	121,7639	31,399	118,3626	90,9446	127,6808	135,7582	159,6133	106,4769	52,9267	190,7536	78,8058	75,7044	116,6771	49,619	107,4383	89,6363	54,313	
	# 5	200,4009	112,1522	25,3496	23,9432	64,7836	56,8262	120,1862	2,8026	90,8919	142,1195	81,2469	182,8806	17,2514	83,8407	146,5308	147,1087	51,22	

		
	def populateFromFile (self, filename):
		f = open(filename, 'r')
		
		for line in f:
			lineData = line.strip().split("\t");
			idCounter = int(lineData[0])
			neibhourList = [(tuple(map(int,elem.split(',')))) for elem in lineData[1:]]
			self.Nodes.append(Node(idCounter,neibhourList))
		
		self.nodeQuant = len(self.Nodes)
		
	# example of input file
	# 500 2184
	# 1 2 6807
	# 2 3 -8874
	# 3 4 -1055
	# 4 5 4414
	# 5 6 1728
	# 6 7 -2237
	# 7 8 -7507
	# 8 9 7990
	# 9 10 -5012
	# 10 11 7353
	# 11 12 -6736
	# 12 13 -7604

	def populateFromFile_type_2 (self, filename):
		f = open(filename, 'r')
		
		for line in f:
			lineData = line.strip().split( );
			if len(lineData) < 3 : continue
			neibs = (map(int,lineData[:-1]))
			arc = int(lineData[2])
			
			nodeCandidate = [x for x in self.Nodes if x.id == neibs[0]]
			if nodeCandidate:
				nodeCandidate[0].neibhours.append( (neibs[1],arc) )
			else:
				self.Nodes.append(Node(neibs[0],[(neibs[1],arc)]))
					
			nodeCandidate = [x for x in self.Nodes if x.id == neibs[1]]
			if nodeCandidate:
				nodeCandidate[0].neibhours.append( (neibs[0],arc) )
			else:
				self.Nodes.append(Node(neibs[1],[(neibs[0],arc)]))
			
			
			
		#self.Nodes.append(Node(7,[]))

		
	def countMinSpanTree(self, srcVertex):
		
		sys.stdout.write(str(self.Nodes[0].id)+"\n")
		sys.stdout.write(str(srcVertex)+"\n")
		
		sourceVertex =  self.NodeById(srcVertex)
		#sys.stdout.write(str(sourceVertex)+"\n")
		candidate = (sourceVertex,100000)
		weHaveACandidate = True
		minSpanTreeWeight = 0
		
		spanTreeEdge = [sourceVertex]
		sourceVertex.explored = True
		
		while (spanTreeEdge):
			
			print('span tree len: '+str(len(spanTreeEdge)))
			newArc = 100000
			candidate = tuple()
			newArcSource = object()
			
			for item in spanTreeEdge:
				for cnd_tuple in item.neibhours:
					cnd = self.NodeById(cnd_tuple[0])
					#print("candidate: "+str(cnd_tuple[0]))
			
					if (cnd).explored: continue
					if (cnd_tuple[1]) < newArc:
						candidate = (cnd,cnd_tuple[1])
						newArcSource = item
						newArc = cnd_tuple[1]
			
			if not candidate: continue
			candidate[0].explored = True
			
			print("Appending: "+candidate[0].verbose()+" ARCH: "+str(newArc))
			spanTreeEdge.append( candidate[0] )
			minSpanTreeWeight=minSpanTreeWeight+candidate[1]
			
			spanTreeEdge = [x for x in spanTreeEdge if self.allNeibhoursExplored(x.id) != True]
			
			# if set([i[0] for i in candidate[0].neibhours]).issubset(set(([i[0] for i in sourceVertex.shortestPaths]))):
				# candidate.allNeibhoursExplored=True
		
		# for path in sourceVertex.shortestPaths:
			# sys.stdout.write(str(path[0].id)+" ->>>>>>>>> "+str(path[1])+"\n")
	
		print("RES: "+str(minSpanTreeWeight))		
			
			
g1 = SimpleGraph()
g1.populateFromFile_type_2('edges.txt')
#g1.countShortestPaths(1)
#sys.stdout.write(str(g1.Nodes[0].neibhours))
g1.countMinSpanTree(2)			