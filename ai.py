import util

class ai:
	def __init__(self, gameboard, height, width, weights):
		self.gameboard = gameboard
		self.height = height
		self.width = width
		self.weights = weights

	def getEndPositions(self, pos, rang, flying, mounted, isEnemy, isBoss):

		if isBoss:
			return [pos]

		else:

			#Need to fix the terrain part of things
			endPositions = []
			for x in range(self.height):
				for y in range(self.width):
					valid = self.gameboard.isValidMove(pos[0], pos[1], x, y,
															 rang, flying, mounted, isEnemy)
					if valid:
						endPositions.append((x,y))
					else:
						continue

			#Hackish
			endPositions.append(pos)
			return endPositions


	def enemyEvaluationFuntion(self, selfCharacter, pos, target):

		'''

		expected kill - ULTRA HIGHT WEIGHT

		expected death

		expected damage done - HIGH WEIGHT

		expected damage taken

		if did not attack: distance to closest enemy

		defense bonus

		'''
		features = util.Counter()
		gameboard = self.gameboard

		characters = gameboard.getCharacters()

		currentHealth = selfCharacter.getCurrentHealth()

		expectedDeath = 0
		expectedKill = 0
		damageGiven = 0
		damageTaken = 0

		if target != None:
			fightResult = self.gameboard.fight(selfCharacter, target, True, pos)

			damageGiven = fightResult[0]
			damageTaken = fightResult[1]

			if damageTaken > currentHealth:
				expectedDeath = 1

			if damageGiven > target.getCurrentHealth():
				expectedKill = 1

		features["expectedDeath"] = expectedDeath
		features["expectedKill"] = expectedKill*10
		features["damageGiven"] = damageGiven
		features["damageTaken"] = damageTaken

		features["lordDead"] = 0

		enemies = []
		for character in characters:
			if character[0].isEnemy() != selfCharacter.isEnemy():
				if character[0] == target:
					if character[0].isLord() and expectedKill:
						features["lordDead"] = 100
					elif expectedKill == 0:
						enemies.append(character)
				else:
					enemies.append(character)

		nearestEnemyDistance = float("inf")
		for enemy  in enemies:
			nearestEnemyDistance = min(nearestEnemyDistance, self.gameboard.manhattanDistance(pos[0], pos[1], enemy[1][0], enemy[1][1]))
			#nearestEnemyDistance = min(nearestEnemyDistance, self.gameboard.aStarSearch( pos[0], pos[1], enemy[1][0], enemy[1][1], charRange, flying, mounted))

		features["nearestEnemyDistance"] = -nearestEnemyDistance

		featureNames = features.keys()
		weightedSum = 0

		for featureName in featureNames:
			weightedSum += features[featureName]

		return weightedSum





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
	def evaluationFunction(self, selfCharacter, switchWeapons, pos, target):

		features = util.Counter()
		gameboard = self.gameboard

		features["terrainDefBonus"] = gameboard.getTerrainDefenseBonus(pos[0], pos[1])
		features["terrainAvoidBonus"] = gameboard.getTerrainAvoidBonus(pos[0], pos[1])

		oweights = selfCharacter.getPrimOffensiveWeights()
		dweights = selfCharacter.getPrimDefensiveWeights()

		if switchWeapons:
			oweights = selfCharacter.getSecOffensiveWeights()
			dweights = selfCharacter.getSecDefensiveWeights()

		currentHealth = selfCharacter.getCurrentHealth()
		maxHealth = selfCharacter.getMaxHealth()

		weights = oweights
		if currentHealth < (.5 * maxHealth):
			weights = dweights

		#get characters returns a list of 2-tuples: (character, characterPosition)
		characters = gameboard.getCharacters()


		# Expected battle results against target

		expectedDeath = 0
		expectedKill = 0
		damageGiven = 0
		damageTaken = 0

		if target != None:
			if switchWeapons:

				selfCharacter.switchWeapons()
				fightResult = self.gameboard.fight(selfCharacter, target, True, pos)

				damageGiven = fightResult[0]
				damageTaken = fightResult[1]

				if damageTaken > currentHealth:
					expectedDeath = 1

				if damageGiven > target.getCurrentHealth():
					expectedKill = 1

			else:
				fightResult = self.gameboard.fight(selfCharacter, target, True, pos)

				damageGiven = fightResult[0]
				damageTaken = fightResult[1]

				if damageTaken > currentHealth:
					expectedDeath = 1

				if damageGiven > target.getCurrentHealth():
					expectedKill = 1


		features["expectedDeath"] = expectedDeath
		features["expectedKill"] = expectedKill
		features["damageGiven"] = damageGiven
		features["damageTaken"] = damageTaken

		features["bossDead"] = 0
		features["allEnemiesDead"] = 0

		# grab all enemies and allies
		enemies = []
		allies = []
		for character in characters:
			if character[0].isEnemy() != selfCharacter.isEnemy():
				if character[0] == target:
					if character[0].isBoss() and expectedKill:
						features["bossDead"] = 1
					elif expectedKill == 0:
						enemies.append(character)
				else:
					enemies.append(character)
			elif character[0] != selfCharacter:
				allies.append(character[0])

		if enemies == []:
			features["allEnemiesDead"] = 1


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
			if gameboard.isInRange(enemy[0], enemy[1], pos):
				numEnemiesInRange += 1
				
				primWeapon = enemy[0].getWeaponType()
				secWeapon = enemy[0].getSecondaryWeaponType()

				if (primWeapon == "axe") or (secWeapon == "axe"):
					numAxeUsersInRange += 1

				if (primWeapon == "lance") or (secWeapon == "lance"):
					numLanceUsersInRange += 1

				if (primWeapon == "sword") or (secWeapon == "sword"):
					numSwordUsersInRange += 1

				if (primWeapon == "bow") or (secWeapon == "bow"):
					numArchersInRange += 1

				if enemy[0].isBoss():
					bossInRange = 1


		#features["numEnemiesInRange"] = numEnemiesInRange
		features["numArchersInRange"] = numArchersInRange
		features["numAxeUsersInRange"] = numAxeUsersInRange
		features["numLanceUsersInRange"] = numLanceUsersInRange
		features["numSwordUsersInRange"] = numSwordUsersInRange
		features["bossInRangeWhileEnemiesStillAlive"] = (bossInRange and (len(enemies) > 1))
		features["bossInRangeWhileEnemiesAllDead"] = (bossInRange and (len(enemies) == 1))

		features["inRangeOfOneUnit"] = (numEnemiesInRange == 1)
		features["inRangeOfTwoUnits"] = (numEnemiesInRange == 2)
		features["inRangeOfThreeUnits"] = (numEnemiesInRange == 3)
		features["inRangeOfFourUnits"] = (numEnemiesInRange == 4)
		features["inRangeOfFiveUnitsOrMore"] = (numEnemiesInRange >= 5)


		# calculate distance to nearest enemy

		charRange = selfCharacter.getRange()
		flying = selfCharacter.isFlying()
		mounted = selfCharacter.isMounted()
		
		nearestEnemyDistance = float("inf")
		for enemy  in enemies:
			nearestEnemyDistance = min(nearestEnemyDistance, self.gameboard.manhattanDistance(pos[0], pos[1], character[1][0], character[1][1]))
			#nearestEnemyDistance = min(nearestEnemyDistance, self.gameboard.aStarSearch( pos[0], pos[1], enemy[1][0], enemy[1][1], charRange, flying, mounted))	

		features["nearestEnemyDistance"] = nearestEnemyDistance

		# return weighted sum of features
		featureNames = features.keys()
		weightedSum = 0

		for featureName in featureNames:
			weightedSum += features[featureName]*weights[featureName]

		return weightedSum

	def calculateMove(self, character):
		if not character.moveable():
			return None

		characters = self.gameboard.getCharacters()

		position = (0,0)
		for charTuple in characters:
			if charTuple[0] == character:
				position = charTuple[1]

		rang = character.getRange()
		flying = character.isFlying()
		mounted = character.isMounted()
		isEnemy = character.isEnemy()
		isBoss = character.isBoss()
		endPositions = self.getEndPositions(position, rang, flying, mounted, isEnemy, isBoss)

		bestScore = -float("inf")
		bestTargetAttcked = None
		bestSwitchWeapons = False
		bestPosition = None

		for pos in endPositions:

			#try both types of weapons as well as each enemy to attack
			primWeapon = character.getWeaponType()
			secWeapon = character.getSecondaryWeaponType()

			targets = self.gameboard.getTargets(character, pos)

			localBestScore = -float("inf")
			localTargetAttacked = None
			localSwitchWeapons = False

			for target in targets:

				if character.isEnemy():
					primWeaponScore = self.enemyEvaluationFuntion(character, pos, target)
				else:
					primWeaponScore = self.evaluationFunction(character, False, pos, target)
				
				score = primWeaponScore
				switchWeapons = False

				if secWeapon != None:
					if character.isEnemy():
						secWeaponScore = self.enemyEvaluationFuntion(character, pos, target)
					else:
						secWeaponScore = self.evaluationFunction(character, True, pos, target)
					
					if secWeaponScore > primWeaponScore:
						score = secWeaponScore
						switchWeapons = True

				if score > localBestScore:
					localBestScore = score
					localTargetAttacked = target
					localSwitchWeapons = switchWeapons

			if localBestScore > bestScore:
				bestScore = localBestScore
				bestTargetAttcked = localTargetAttacked
				bestSwitchWeapons = localSwitchWeapons
				bestPosition = pos

		#print character.getName()
		#print (bestPosition, bestSwitchWeapons, bestTargetAttcked)
		return (bestPosition, bestSwitchWeapons, bestTargetAttcked)
