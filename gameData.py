import csv
import os
from shutil import copyfile
#Its reading correctly but its not writing at all!!!

class gameStats:
	file = open('config.csv') #Chooses which file to use
	configRead = csv.reader(file, delimiter=',')
	fileData = []
	for row in configRead: #Puts stuff from the config file into an array (fileData)
		rowData = []
		for col in row:
			rowData.append(col)
		fileData.append(rowData)
	def __init__(self):
		pass
	def checkCommand(self, input): #This runs every time speech is recorded
		rowCounter = 0
		#self.fileData[1]=["Wow", "It", "Actually", "Worked", "YAY"]
		#self.fileData[1][0]="Changed!!!"
		for row in self.fileData: #For each row in the file
			if(rowCounter!=0):
				if(row[0] in input):
					parsed = str.split(input)
					modNum = 1 #Number to modify the quantity by
					for word in parsed: #For each word in the input try to find a number
						try:
							modNum = int(word)
						except:
							modNum=modNum
					if row[1] in input: #If it was said to add
						row[4] = str(int(row[4]) + modNum)
					if row[2] in input: #If it was said to subtract
						row[4] = str(int(row[4]) - modNum)
					if row[3] in input: #If it was said to reset
						row[4]="0"
					break
			rowCounter+=1
	def printQuantities(self): #Prints all of the quantities
		for row in self.fileData:
			print(row[0] + " " + row[4])
	def writeData(self):	#writes data in fileData to the file
		#configWrite =  csv.writer(file, delimiter=',')
		file2=open("tempConfig.csv", 'w', newline='')
		configWrite = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		configWrite.writerows(self.fileData)
		file2.close()
		copyfile("tempConfig.csv", "config.csv")
	def addVar(self, itemName, addCmd, rmCmd, resetCmd, startingQuantity): #Add a var to the file
		self.fileData.append([itemName, addCmd, rmCmd, resetCmd, startingQuantity])
	def getQuantity(name): #Gets the quantity of some variable
		for row in fileData:
			if(row[0]==name):
				return int(row[4])
	
