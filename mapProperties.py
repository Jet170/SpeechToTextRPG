import csv
import os
class mapData:
	file = open('mapConfig.csv') #Chooses which file to use
	configRead = csv.reader(file, delimiter=',')
	rowCounter=0
	unitName=""
	unitConverter="1"
	pixelsX="1"
	pixelsY="1"
	for row in configRead:
		if rowCounter==1:
			colCounter=0
			for col in row:
				if colCounter==0:
					unitName = row[0]
				elif colCounter==1:
					unitConverter = row[1]
				elif colCounter==2:
					pixelsX = row[2]
				elif colCounter==3:
					pixelsY = row[3]
				colCounter+=1
		rowCounter+=1
	def __init__(self): #Does Nothing
		pass
	def printStats(self): #Prints map stats
		print(self.unitName + " " + self.unitConverter + " " + self.pixelsX + " " + self.pixelsY)
	def getUnitName(self):
		return self.unitName
	def getUnitConverter(self):
		return float(self.unitConverter)
	def getPixelsX(self):
		return int(self.pixelsX)
	def getPixelsY(self):
		return int(self.pixelsY)
	
	
		
	
