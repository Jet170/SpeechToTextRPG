input = "shoot 952 arrows"
arrows = 25
if("shoot" in input):
	parsed = str.split(input)
	modNumber = 1
	try:
		modNumber = int(parsed[1])
	except:
		modNumber=1
	arrows=arrows-modNumber
print(arrows)
