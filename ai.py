class ai:
	def __init__(self, gameboard, height, width, weights):
		self.gameboard = gameboard
		self.height = height
		self.width = width
		self.weights = weights

	def getEndPositions(self, pos, rang, flying, mounted):
		#Need to fix the terrain part of things
		endPositions = []
		for x in range(self.height):
			for y in range(self.width):
				valid = self.gameboard.isValidMove(pos[0], pos[1], x, y,
														 rang, flying, mounted)
				if valid:
					endPositions.append((x,y))
				else:
					continue

		#Hackish
		endPositions.append(pos)
		return endPositions

	def evaluationFunction(self, position, pos):
		return self.gameboard.manhattanDistance(position[0], position[1], pos[0], pos[1])

	def calculateMove(self, character):
		characters = self.gameboard.getCharacters()

		position = (0,0)
		for charTuple in characters:
			if charTuple[0] == character:
				position = charTuple[1]

		rang = character.getRange()
		flying = character.isFlying()
		mounted = character.isMounted()
		endPositions = self.getEndPositions(position, rang, flying, mounted)

		print endPositions

		positionUsed = position
		positionScore = 0
		for pos in endPositions:
			score = self.evaluationFunction(position, pos)

			if score > positionScore:
				positionScore = score
				positionUsed = pos

		print positionUsed
