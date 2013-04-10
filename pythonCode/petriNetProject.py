from Transition import Transition
import sys

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
	
	
main()