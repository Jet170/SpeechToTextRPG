import csv
import os
import mapProperties
from shutil import copyfile
#Its reading correctly but its not writing at all!!!

class characterData:
	file = open('charactersConfig.csv') #Chooses which file to use
	configRead = csv.reader(file, delimiter=',')
	fileData = []
	for row in configRead: #Puts stuff from the config file into an array (fileData)
		rowData = []
		for col in row:
			rowData.append(col)
		fileData.append(rowData)
	def __init__(self):#Adds any necessary names
		characterNames = []
		for fi in os.walk('.'):
			if(".csv" in fi):
				characterNames.append(fi)
		for name in characterNames:
			name = str.lower(name)
			foundName = False
			for row in self.fileData:
				if name == row[0]:
					foundName = True
			if foundName==False:
				self.fileData.append([name, "0", "0"])
	def setCoords(self, name, x, y):#Sets the coordinates of name to x and y
		if(x<0):
			x=0
		if (y<0):
			y=0
		for row in self.fileData:
			if row[0]==name:
				row[1]=str(x)
				row[2]=str(y)
				break
	def printCoords(self): #Prints all of the coordinates
		for row in self.fileData:
			print(row[0] + " " + row[1] + " " + row[2])
	def writeData(self):	#writes data in fileData to characters.csv
		file2=open("tempCharactersConfig.csv", 'w', newline='')
		configWrite = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		configWrite.writerows(self.fileData)
		file2.close()
		copyfile("tempCharactersConfig.csv", "charactersConfig.csv")
	def getCharacterX(self, name):
		for row in self.fileData:
			if row[0]==name:
				return(int(row[1]))
	def getCharacterY(self, name):
		for row in self.fileData:
			if row[0]==name:
				return(int(row[2]))
	def move(self, text):
		parsed = str.split(text)
		amount = 0
		name = None
		for data in parsed:
			try:
				amount = int(data)
			except:
				amount = amount
		if(amount = 0):
			if(data=="one")
				amount=1
			if(data=="two")
				amount=2
			if(data=="three")
				amount=3
			if(data=="four")
				amount=4
			if(data=="five")
				amount=5
			if(data=="six")
				amount=6
			if(data=="seven")
				amount=7
			if(data=="eight")
				amount=8
			if(data=="nine")
				amount=9
			if(data=="ten")
				amount=10
			if(data=="eleven")
				amount=11
			if(data=="twelve")
				amount=12
			if(data=="thirteen")
				amount=13
			if(data=="fourteen")
				amount=14
			if(data=="fifteen")
				amount=15
			if(data=="sixteen")
				amount=16
			if(data=="seventeen")
				amount=17
			if(data=="eighteen")
				amount=18
			if(data=="nineteen")
				amount=19
		for row in self.fileData:
			if row[0] in text:
				name = row[0]
		if(name==None):
			return
		mapp = mapProperties.mapData()
		amount = amount * mapp.getUnitConverter()
		if( "north" in parsed):
			x = self.getCharacterX(name)-amount
			if(x<0):
				x=0
			self.setCoords(name, x, self.getCharacterY(name))
		elif("south" in text):
			self.setCoords(name, self.getCharacterX(name)+amount, self.getCharacterY(name))
		elif("west" in text):
			y=self.getCharacterY(name)-amount
			if(y<0):
				y=0
			self.setCoords(name, self.getCharacterX(name), y)
		elif("east" in text):
			self.setCoords(name, self.getCharacterX(name), self.getCharacterY(name)+amount)	
