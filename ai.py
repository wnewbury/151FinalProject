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


	def enemyEvaluationFuntion(self, character, position, pos, attackedEnemy):

		'''

		expected kill - ULTRA HIGHT WEIGHT

		expected death

		expected damage done - HIGH WEIGHT

		expected damage taken

		if did not attack: distance to closest enemy

		defense bonus



		'''
		return 0

	'''

	in range should also be based on currently equiped weapon

	defensive mode and offensive mode
		divided on 50 percent health line

	if in range of enemy units: 

		terrain defense bonus
		terrain avoid bonus

	in range of an axe user

	in range of a lance user

	in range of a sword user

	in range of a bow user

	in range of one unit

	in range of two units

	in range of three units

	in range of four units

	in range of five units

	in range of more than 5 units

	in range of boss and other enemies

	expected damage taken if all enemies in range attack

	expected death if all enemies in range attack

		note: less expected health should make things worse


	expected death

	expected kill

	predicted damage taken

	predicted damage given

	attacked enemy killable by ally



	is archer in range of attack by cqc


	'''
	def evaluationFunction(self, selfCharacter, equippedWeapon, pos, targets):


		# if character is below half health use defensive weights
		healthModifierOffensive = 2
		healthModifierDefensive = 1
		if selfCharacter.getCurrentHealth() < (.5 * selfCharacter.getMaxHealth()):
			healthModifierOffensive = 1
			healthModifierDefensive = 2

		oweights = selfCharacter.getOffensiveWeights()
		dweights = selfCharacter.getDefensiveWeights()

		gameboard = self.gameboard
		characters = gameboard.getCharacters()

		# grab all enemies and allies
		enemies = []
		allies = []
		for character in characters:
			if character[0].isEnemy():
				enemies.append(character[0])

			elif character[0] != selfCharacter:
				allies.append(character[0])


		#check which enemies would be in range
		numEnemiesInRange = 0
		numArchersInRange = 0
		numAxeUsersInRange = 0
		numLanceUsersInRange = 0
		numSwordUsersInRange = 0
		bossInRange = 0

		enemiesInRange = []
		for enemy in enemies:
			#enemyLocation = gameboard.GET_ENEMY_LOCATION
			if gameboard.isInRange(enemy, pos):
				numEnemiesInRange += 1
				
				primWeapon = enemy.getWeaponType()
				secWeapon = enemy.getSecondaryWeaponType()

				if (primWeapon == "axe") or (secWeapon == "axe"):
					numAxeUsersInRange += 1

				if (primWeapon == "lance") or (secWeapon == "lance"):
					numLanceUsersInRange += 1

				if (primWeapon == "sword") or (secWeapon == "sword"):
					numSwordUsersInRange += 1

				if (primWeapon == "bow") or (secWeapon == "bow"):
					numArchersInRange += 1

				if enemy.isBoss():
					bossInRange = 1

		result = (0,0)
		damageNet = 0
		targetAttacked = None
		if targets != []:
			for target in targets:
				result = self.gameboard.fight(selfCharacter, target, True, pos)
				if (result[0] - result[1]) > damageNet:
					targetAttacked = target
					damageNet = (result[0] - result[1])

		return (damageNet, targetAttacked)

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

		positionUsed = position
		switchWeapons = False
		targetAttacked = None
		positionScore = 0
		for pos in endPositions:

			#try both types of weapons as well as each enemy to attack
			primWeapon = character.getWeaponType()
			secWeapon = character.getSecondaryWeaponType()

			targets = self.gameboard.getTargets(character, pos)

			score = max(self.evaluationFunction(character, primWeapon, pos, [])[0], self.evaluationFunction(character, secWeapon, pos, [])[0])

			temp = self.evaluationFunction(character, primWeapon, pos, targets)
			if temp[0] > score:
				targetAttacked = temp[1]
				score = temp[0]

			temp = self.evaluationFunction(character, secWeapon, pos, targets)
			if temp[0] > score:
				targetAttacked = temp[1]
				score = temp[0]
				switchWeapons = True

			if score > positionScore:
				positionScore = score
				positionUsed = pos

		return (positionUsed, switchWeapons, targetAttacked)
