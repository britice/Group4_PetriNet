import copy

class Transition:
	def __init__(self, name, inputNames, outputNames):
		self.name = name
		self.inputNames = copy.deepcopy(inputNames)
		self.outputNames = copy.deepcopy(outputNames)
		
	def getName(self):
		return self.name
	
	# canFire()
	# Inputs: currentState - a dictionary with the key being the string
	#         name of the position and the value being the number of tokens
	# Outputs: True if the transition can fire, else False
	def canFire(self, currentState):
		
		for placeName in self.inputNames:
			if currentState[ placeName ] == 0:
				return False
		return True
		
	# fire()
	# Inputs: currentState - a dictionary with the key being the string
	#         name of the position and the value being the number of tokens
	# Outputs: True if the transition fires, else False
	#          currentState is changed in-place
	def fire(self, currentState):
		
		if not self.canFire(currentState):
			return False
		
		for placeName in self.inputNames:
			currentState[ placeName ] -= 1
			
		for placeName in self.outputNames:
			currentState[ placeName ] += 1
			
		return True
		
	def toString(self):
		
		s = "Name: " + self.name + "\nInputs:"
		for inputName in self.inputNames:
			s += " " + inputName
		s += "\nOutputs:"
		for outputName in self.outputNames:
			s += " " + outputName
			
		return s