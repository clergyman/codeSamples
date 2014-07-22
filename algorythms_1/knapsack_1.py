import numpy as np
# Input file describes a knapsack instance, and it has the following format:
# [knapsack_size][number_of_items]
# [value_1] [weight_1]
# [value_2] [weight_2]
# ...
# For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
# You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

# The file implements simple knapsack solution and returns optimal value for the given input file 

class Item:
	def __init__(self, ID = 0, Value=0, Weight=0):
		self.id = ID
		self.value = Value
		self.weight = Weight
	
	def verbose(self):
		return ("Item instance. ID: "+str(self.id)+ " value: " +str(self.value)+" weight: "+str(self.weight))

class Knapsack:
	def __init__(self):
		self.capacity = 0
		self.Items = []
		
		
	# emample of input file
	# 1000  15
	# 16808 250
	# 50074 659
	# 8931 273
	# 27545 879
	# 77924 710
	# 64441 166
	# 84493 43
	# 7988 504
	# 82328 730
	# 78841 613
	# 44304 170
	# 17710 158
	# 29561 934
	# 93100 279
	# 51817 336

	def populateFromFile (self, filename):
		f = open(filename, 'r')
		
		i=0
		
		for line in f:
			
			lineData = map(int,line.strip().split( ));
			if i == 0 : 
				self.capacity = lineData[0]
			elif (lineData):
				self.Items.append(Item(i,lineData[0],lineData[1]))
			else: break	
			
			i = i+1
			
		self.filling = np.zeros( (len(self.Items)+1,self.capacity+1 ) )	
		#self.filling = np.zeros( (2,self.capacity+1 ) )	
		
	def itemById(self, ID):
		if ID not in [item.id for item in self.Items]: return None
		else: return [item for item in self.Items if item.id == ID][0]
		
	
	def optimalPack(self):
		for (i,x) , intermediate in np.ndenumerate (self.filling):
			if i == 0: continue
			currItem = self.itemById(i)
			
			if not currItem: return -1
			
			currValue = currItem.value
			currWeight = currItem.weight
			
			if (x-currWeight < 0) : self.filling[i][x] = self.filling[i-1][x]
			else: self.filling[i][x] =  max(self.filling[i-1][x] , (self.filling[i-1][x-currWeight]+currValue))
			
			#print ("ITER: i = "+str(i)+"x = "+str(x)+ " value = "+str(intermediate))
		print(self.filling)	
		
s1 = Knapsack()
#s1.populateFromFile("input\knapsack1.txt")
#s1.populateFromFile("TC1.txt")
s1.populateFromFile("knapsack_big.txt")


#print(s1.Items[2].verbose())
s1.optimalPack( )