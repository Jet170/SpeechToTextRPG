import csv
#Its reading correctly but its not writing at all!!!
class gameStats:
	def __init__(self): #Use for setup if needed
		pass
	def checkCommand(self, input): #This runs every time speech is recorded
		file = open('config.csv') #Chooses which file to use
		configRead = csv.reader(file, delimiter=',')
		configWrite = csv.writer(file, delimiter=',')
		rowCounter = 0
		for row in configRead: #For each row in the file
			if(rowCounter!=0):
				rowCounter+=1
				if(row[0] in input):
					parsed = str.split(input)
					modNum = 1 #Number to modify the quantity by
					for word in parsed: #For each word in the input try to find a number
						try:
							modNum = int(word)
						except:
							modNum=modNum
					if row[1] in input: #If it was said to add
						row[4] = int(row[4]) + modNum
					if row[2] in input: #If it was said to subtract
						row[4] = int(row[4]) - modNum
					if row[3] in input: #If it was said to reset
						row[4]="0"
					break
	def printQuantities(self): #Prints all of the 
		file = open('config.csv') #Chooses which file to use
		config = csv.reader(file, delimiter=',')
		for row in config:
			print(row[0] + " " + row[4])
	



