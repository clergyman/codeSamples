import sys

def diff(a,b)  : return a-b

def ratio(a,b) : return float(a)/b

def readData(dataList, filename):
	f = open(filename, 'r')
		
	for line in f:
		
		lineData = line.strip().split();
		lineData = map(int,lineData)
		if (len(lineData)>1):
			dataList.append(tuple(lineData))
			
def scheduleWithFunc(func, dataList):
	return sorted(dataList, key= (lambda t : (func(t[0],t[1]), t[0] )), reverse = True) 
	
		

data = []

readData(data,"jobs.txt")

schedule = scheduleWithFunc(diff,data)	

#ratio 67311454237
#diff 69119377652
			
			
def countWeightedComplTimes(sch):
	wTimesSum = 0
	timeElapsed = 0
	for p in sch: 
	#print p, diff(p[0], p[1])
		timeElapsed=timeElapsed+p[1]
		wTimesSum = wTimesSum + timeElapsed*p[0]
	return wTimesSum	
		
	
			
sys.stdout.write(str(countWeightedComplTimes(schedule)))
			