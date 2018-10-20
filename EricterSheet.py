class testCharSheet:
	def __init__(self):
		pass
	arrows=25
	def shoot(self):
		testCharSheet.arrows=testCharSheet.arrows-1
class parseInput:
	kaz = testCharSheet()
	def __init__(self):
		pass
	def checkIfShoot(self, words):
		if("shoot" in words):
			parseInput.kaz.shoot()
			print(parseInput.kaz.arrows)
