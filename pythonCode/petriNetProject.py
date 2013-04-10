from Transition import Transition
import sys
import copy

def parseFile(fileName, positions, transitions):

	infile = open(fileName, 'r')
	
	transLine = infile.readline()
	
	while transLine != "":
		# get the token name
		tName = transLine.strip()
		
		# get and split the input places line
		inputsLine = infile.readline().split()
		inputNames = []
		
		# i goes from 0 up to len of inputsLine, skipping odd ints
		for i in range( 0, len(inputsLine), 2 ):
			pName = inputsLine[ i ]
			numTokens = int(inputsLine[ i + 1 ])
			if pName in positions:
				if positions[pName] != numTokens:
					print "Conflicting information in the data file."
					print "Exiting..."
					sys.exit()
			else:
				positions[pName] = numTokens
			# add this input place name for this transition
			inputNames.append(pName)
		
		outputsLine = infile.readline().split()
		outputNames = []
		
		for i in range( 0, len(outputsLine), 2 ):
			pName = outputsLine[ i ]
			numTokens = int(outputsLine[ i + 1 ])
			if pName in positions:
				if positions[pName] != numTokens:
					print "Conflicting information in the data file."
					print "Exiting..."
					sys.exit()
			else:
				positions[pName] = numTokens
			outputNames.append(pName)
		
		transitions.append(Transition(tName, inputNames, outputNames))
		
		transLine = infile.readline()
			
	infile.close()


def makeTree(positions, numStatesPrinted, statesInTree, transitions):
	# Stops the whole recursion if 30 states have already been printed
	if numStatesPrinted > 30:
		return False
	
	# Saves the current state
	oldState = copy.deepcopy(positions)
	
	isDone = False
	
	# Goes through every transition and fires them, if they can
	for t in transitions:
		transfer = copy.deepcopy(oldState)
		
		if t.fire(transfer) == True:
			newState = copy.deepcopy(transfer)
			printOutState(oldState, newState, t)
			
			# If the new state is not in the tree, then keep recursing down the tree
			if inVector(newState, statesInTree) == False:
				statesInTree.append(newState)
				numStatesPrinted += 1
				
				isDone = makeTree(newState, numStatesPrinted, statesInTree, transitions)
		
		# If the number of states printed already equals 30, then stop the recursion
		if isDone == True:
			break
	
	return True
			

# Checks to see if position is already in the tree
def inVector(position, statesInTree):
	for state in statesInTree:
		if position == state:
			return True
	return False

# Prints out the marking vector
def printOutState(beforeState, afterState, theTransition):
	beforeNames = beforeState.keys()
	afterNames = afterState.keys()
	
	beforeNames.sort()
	afterNames.sort()
	
	print "(",
	
	for pName in beforeNames:
		print ("%d" % (beforeState[pName])),
	
	print (") at %s gives (" % (theTransition.getName())),
	
	for pName in afterNames:
		print ("%d" % (afterState[pName])),
	
	print ")"


def main():
	
	fileName = sys.argv[1]
	
	transitions = list()
	positions = dict()
	
	parseFile(fileName, positions, transitions)
	
	print "Transitions:"
	for transition in transitions:
		print transition.toString()
	
	print "Positions:"
	positionNames = positions.keys()
	positionNames.sort()
	for pName in positionNames:
		print ("Name: %s, Tokens: %d" % (pName, positions[pName]))
	
	
	statesInTree = list()
	statesInTree.append(positions)
	
	# The following print statements print out a key for the marking vector
	print "Key: (",
	
	positionNames = positions.keys()
	positionNames.sort()
	
	for pName in positionNames:
		print "%s" % (pName),
	
	print ")"
	
	makeTree(positions, 0, statesInTree, transitions)
	
main()
