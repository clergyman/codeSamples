import sys

class Node:
	def __init__(self, ident=0, adjacencyList=None):
		self.neibhours = adjacencyList
		self.id = ident
		self.explored = False
		self.allNeibhoursExplored = False
		self.shortestPaths = []
		self.shortestPaths.append( (self,0) )
		
class ChainedHash:
	def __init__(self):
		self.Table = {}
		
	def lookup(self,num):
		
		res = False
		h = self.hashF(num);
		if h in self.Table:
			if num in self.Table[h]:
				res = True
		
		return res
		
	def insert(self,num):
		h = self.hashF(num);
		
		#sys.stdout.write("INSERTION num: "+str(num)+" hash: "+str(h)+"\n")			
		if h in self.Table:
			if num in self.Table[h]: #already in the hash table
				return
			else:
				self.Table[h].append(num)
		else:
			self.Table[h] = [num]
		#sys.stdout.write("TABLE: "+str(self.Table)+"\n")			
			
	
	def populateFromFile (self, filename):
		f = open(filename, 'r')
		
		for line in f:
			lineData = int(line.strip())
			self.insert(lineData)
			
		f.close()
			
	def hashF(self,inp):
		return inp % 15485863 
	
			
tab1 = ChainedHash()
tab1.populateFromFile('F2sum.txt')

def inspectHashTab2Sum(a,b):
	counter = 0
	time = 0
	additionalVal = 0
	
	for SUM in range (a, b+1):
		for k in tab1.Table:
			for val in tab1.Table[k]:
				additionalVal = SUM - val
				if tab1.lookup(additionalVal):
					counter = counter + 1
					continue
		
		sys.stdout.write(str(SUM)+"\n")
		
	return counter


sys.stdout.write(str(inspectHashTab2Sum(-10000,10000)))			