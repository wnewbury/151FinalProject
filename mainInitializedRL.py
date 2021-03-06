from gameBoard import gameBoard
from character import weapon, character, stats
from ai import ai
import random
import reinforcement

import util

class runGame:
    def __init__(self, mapName, weights):
        self.mapBoard = self.generateBoard(mapName)
        self.mapCharacters = self.generateCharacters(mapName, weights)
        self.height = len(self.mapBoard)
        self.width = len(self.mapBoard[0])
        self.gameboard = gameBoard(self.mapBoard, self.mapCharacters,
                                   self.height, self.width, self.mapLords)
        self.weights = []
        self.ai = ai(self.gameboard, self.height, self.width, self.weights)

    def generateBoard(self, mapName):
        mapBoard = [[]]
        if mapName == "bom":
            mapBoard = [[0,0,0,0,0,1,0,0,0,2,0,0,0,0,3],
                    [0,1,1,1,0,0,0,0,2,0,0,1,1,1,0],
                    [0,1,1,1,0,1,0,0,0,0,0,1,0,1,1],
                    [2,0,0,0,0,1,1,1,0,0,0,2,0,0,0],
                    [1,1,1,0,0,0,0,1,0,0,0,0,0,0,0],
                    [0,3,1,1,1,1,1,1,1,1,1,0,0,2,0],
                    [0,0,1,1,1,0,0,1,0,0,0,0,1,1,1],
                    [0,0,0,0,0,0,0,1,0,0,1,0,1,0,1],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,2],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,2,2]]

        return mapBoard

    def generateCharacters(self, mapName, weights):
        mapCharacters = [[]]
        if mapName == "bom":
            mapCharacters = [[None for i in xrange(15)] for j in xrange(10)]
            self.mapLords = 1

            #weapons in map
            ironAxe = weapon("Iron Axe", "axe", 8, 75, 0, 1, 10)
            steelAxe = weapon("Steel Axe", "axe", 11, 65, 0, 1, 15)
            
            ironSword = weapon("Iron Sword", "sword", 5, 90, 0, 1, 5)
            maniKatti = weapon("Mani Katti", "sword", 8, 80, .20, 1, 3)

            slimLance = weapon("Slim Lance", "lance", 4, 85, .05, 1, 4)
            ironLance = weapon("Iron Lance", "lance", 7, 80, 0, 1, 8)

            ironBow = weapon("Iron Bow", "bow", 6, .85, 0, 2, 5)


            #characters

            #lyn
            lynPrimOweights = weights["lynPrimOweights"]
            lynPrimDweights = weights["lynPrimDweights"]
            lynSecOweights = None
            lynSecDweights = None

            lynStats = stats(19, 5, 10, 12, 8, 2, 1, 5, 5)
            lyn = character("Lyn", "Lord", maniKatti, None, False, False, lynStats, 19, lynPrimOweights, lynPrimDweights, lynSecOweights, lynSecDweights)


            #kent
            kentPrimOweights = weights["kentPrimOweights"]
            kentPrimDweights = weights["kentPrimDweights"]
            kentSecOweights = weights["kentSecOweights"]
            kentSecDweights = weights["kentSecDweights"]

            kentStats = stats(22, 6, 6, 8, 3, 5, 1, 9, 7)
            kent = character("Kent", "Cavalier", ironSword, ironLance, False, False, kentStats, 22, kentPrimOweights, kentPrimDweights, kentSecOweights, kentSecDweights)


            #sain
            sainPrimOweights = weights["sainPrimOweights"]
            sainPrimDweights = weights["sainPrimDweights"]
            sainSecOweights = weights["sainSecOweights"]
            sainSecDweights = weights["sainSecDweights"]

            sainStats = stats(21, 9, 4, 8, 4, 7, 1, 9, 7)
            sain = character("Sain", "Cavalier", ironSword, ironLance, False, False, sainStats, 21, sainPrimOweights, sainPrimDweights, sainSecOweights, sainSecDweights)


            #wil
            wilPrimOweights = weights["wilPrimOweights"]
            wilPrimDweights = weights["wilPrimDweights"]
            wilSecOweights = None
            wilSecDweights = None

            wilStats = stats(20, 6, 5, 5, 6, 5, 0, 6, 5)
            wil = character("Wil", "Archer", ironBow, None, False, False, wilStats, 20, wilPrimOweights, wilPrimDweights, wilSecOweights, wilSecDweights)


            #florina
            florinaPrimOweights = weights["florinaPrimOweights"]
            florinaPrimDweights = weights["florinaPrimDweights"]
            florinaSecOweights = None
            florinaSecDweights = None

            florinaStats = stats(17, 5, 7, 9, 7, 4, 4, 4, 7)
            florina = character("Florina", "PegKnight", slimLance, None, False, False, florinaStats, 17, florinaPrimOweights, florinaPrimDweights, florinaSecOweights, florinaSecDweights)
            


            #enemies

            #L1 Brigands
            L1BrigandPrimOweights = util.Counter()
            L1BrigandPrimDweights = util.Counter()
            L1BrigandSecOweights = None
            L1BrigandSecDweights = None

            L1BrigandStats = stats(20, 3, 1, 5, 0, 3, 0, 12, 5)
            brigand1 = character("Brig1", "Brigand", ironAxe, None, True, False, L1BrigandStats, 20, L1BrigandPrimOweights, L1BrigandPrimDweights, L1BrigandSecOweights, L1BrigandSecDweights)

            #L2 Brigands
            L2BrigandPrimOweights = util.Counter()
            L2BrigandPrimDweights = util.Counter()
            L2BrigandSecOweights = None
            L2BrigandSecDweights = None

            L2BrigandStats = stats(21, 4, 2, 5, 0, 3, 0, 12, 5)
            brigand2 = character("Brig2", "Brigand", ironAxe, None, True, False, L2BrigandStats, 21, L2BrigandPrimOweights, L2BrigandPrimDweights, L2BrigandSecOweights, L2BrigandSecDweights)
            brigand3 = character("Brig3", "Brigand", ironAxe, None, True, False, L2BrigandStats, 21, L2BrigandPrimOweights, L2BrigandPrimDweights, L2BrigandSecOweights, L2BrigandSecDweights)

            #Mercs
            mercPrimOweights = util.Counter()
            mercPrimDweights = util.Counter()
            mercSecOweights = None
            mercSecDweights = None

            mercenaryStats = stats(16, 4, 7, 5, 0, 3, 0, 9, 5)
            merc1 = character("Merc1", "Mercenary", ironSword, None, True, False, mercenaryStats, 16, mercPrimOweights, mercPrimDweights, mercSecOweights, mercSecDweights)
            merc2 = character("Merc2", "Mercenary", ironSword, None, True, False, mercenaryStats, 16, mercPrimOweights, mercPrimDweights, mercSecOweights, mercSecDweights)

            #Archers
            archerPrimOweights = util.Counter()
            archerPrimDweights = util.Counter()
            archerSecOweights = None
            archerSecDweights = None

            archerStats = stats(18, 1, 3, 3, 0, 3, 0, 7, 5)
            archer1 = character("Archer1", "Archer", ironBow, None, True, False, archerStats, 18, archerPrimOweights, archerPrimDweights, archerSecOweights, archerSecDweights)
            archer2 = character("Archer2", "Archer", ironBow, None, True, False, archerStats, 18, archerPrimOweights, archerPrimDweights, archerSecOweights, archerSecDweights)

            #Migal
            migalPrimOweights = util.Counter()
            migalPrimDweights = util.Counter()
            migalSecOweights = None
            migalSecDweights = None

            migalStats = stats(25, 7, 3, 5, 2, 5, 0, 12, 5)
            migal = character("Migal", "Brigand", steelAxe, None, True, True, migalStats, 25, migalPrimOweights, migalPrimDweights, migalSecOweights, migalSecDweights)

            #initialize characters on map
            mapCharacters[9][2] = kent
            mapCharacters[8][4] = sain
            mapCharacters[6][3] = lyn
            mapCharacters[6][5] = wil
            mapCharacters[4][4] = florina

            mapCharacters[7][8] = archer1
            mapCharacters[4][8] = brigand2
            mapCharacters[8][13] = brigand1
            mapCharacters[3][11] = archer2
            mapCharacters[2][12] = brigand3
            mapCharacters[6][14] = merc1
            mapCharacters[0][11] = merc2
            mapCharacters[0][13] = migal

        return mapCharacters

    def getCharacterAtPosition(self, position):
        characters = self.gameboard.getCharacters()

        for characterTuple in characters:
            if characterTuple[1] == position:
                return characterTuple[0]
        print "no character at position"
        return False

    def getCharacterByName(self, name):
        characters = self.gameboard.getCharacters()

        for characterTuple in characters:
            if characterTuple[0].getName() == name:
                return characterTuple[0]
        print "character does not exist"
        return False

    def askInput(self):
        command = raw_input("Input command to perform: ")

        if command == "move":
            char = raw_input("Input name of character to move: ")
            character = self.getCharacterByName(char)
            while character == False:
                char = raw_input("Reinput name: ")
                character = self.getCharacterByName(char)

            x = raw_input("X coordinate to move to: ")
            while (int(x) < 0) or (int(x) > 9):
                x = raw_input("Please input valid coordinate: ")
            y = raw_input("Y coordinate to move to: ")
            while (int(y) < 0) or (int(y) > 14):
                y = raw_input("Please input valid coordinate: ")

            self.gameboard.moveCharacter(character, int(x), int(y))
        elif command == "attack":
            char1 = raw_input("Input name of character to attack with: ")
            character1 = self.getCharacterByName(char1) 
            while character1 == False:
                char1 = raw_input("Reinput name: ")
                character1 = self.getCharacterByName(char1)

            char2 = raw_input("Input name of character to attack: ")
            character2 = self.getCharacterByName(char2)
            while character2 == False:
                char2 = raw_input("Reinput name: ")
                character2 = self.getCharacterByName(char2)

            self.gameboard.fight(character1, character2)
        elif command == "endTurn":
            self.gameboard.endTurn()
        elif command == "auto":
            char = raw_input("Input name of character to automate: ")
            character = self.getCharacterByName(char)
            while character == False:
                char = raw_input("Reinput name: ")
                character = self.getCharacterByName(char)

            result = self.ai.calculateMove(character)

            if result == None:
                print "Already acted"
                return

            position = result[0]
            #print position
            character2 = result[2]
            #print character2
            switch = result[1]
            #print switch

            if switch:
                character.switchWeapons()

            self.gameboard.moveCharacter(character, position[0], position[1])

            if character2 != None:
                self.gameboard.fight(character, character2)
        self.Display()

    def Display(self):
        self.gameboard.Display()


    def hasEnded(self):
        return self.gameboard.isWin() or self.gameboard.isLose()
    #To be used at some point
    #def playTurn(self):
        #self.gameboard.getCharacters()

    def calculateMove(self, character):
        return self.ai.calculateMove(character)

    def getAllyCharacters(self):
        characters = self.gameboard.getCharacters()
        Allies = []
        for character in characters:
            if not character[0].isEnemy() and character[0].getName() != "Lyn":
                Allies.append(character[0])
        random.shuffle(Allies)
        Lyn = self.getCharacterByName("Lyn")
        Allies.append(Lyn)
        return Allies

    def getEnemyCharacters(self):
        characters = self.gameboard.getCharacters()
        Enemies = []
        for character in characters:
            if character[0].isEnemy():
                Enemies.append(character[0])
        random.shuffle(Enemies)        
        return Enemies

def createWeights():

      weights = util.Counter()

      #lyn
      lynPrimOweights = util.Counter()
      lynPrimDweights = util.Counter()
      lynSecOweights = None
      lynSecDweights = None

      # offensive (normal) weights
      lynPrimOweights["terrainDefBonus"] = 1.0
      lynPrimOweights["terrainAvoidBonus"] = 1.0

      lynPrimOweights["expectedDeath"] = -500.0
      lynPrimOweights["expectedKill"] = 5.0
      lynPrimOweights["damageGiven"] = 1.0
      lynPrimOweights["damageTaken"] = -3.0
      lynPrimOweights["bossDead"] = 50.0
      lynPrimOweights["allEnemiesDead"] = 100.0

      lynPrimOweights["numArchersInRange"] = -.5
      lynPrimOweights["numAxeUsersInRange"] = 1.0
      lynPrimOweights["numLanceUsersInRange"] = -1.0
      lynPrimOweights["numSwordUsersInRange"] = 0
      lynPrimOweights["bossInRangeWhileEnemiesStillAlive"] = -5.0
      lynPrimOweights["bossInRangeWhileEnemiesAllDead"] = 1.0

      lynPrimOweights["inRangeOfOneUnit"] = 2.0
      lynPrimOweights["inRangeOfTwoUnits"] = 1.0
      lynPrimOweights["inRangeOfThreeUnits"] = -1.0
      lynPrimOweights["inRangeOfFourUnits"] = -5.0
      lynPrimOweights["inRangeOfFiveUnitsOrMore"] = -10.0

      lynPrimOweights["nearestEnemyDistance"] = -2.0

      lynPrimOweights["adjacentToEnemy"] = -500.0


      # defensive weights
      lynPrimDweights["terrainDefBonus"] = 5.0
      lynPrimDweights["terrainAvoidBonus"] = 5.0

      lynPrimDweights["expectedDeath"] = -500.0
      lynPrimDweights["expectedKill"] = 1.0
      lynPrimDweights["damageGiven"] = 1.0
      lynPrimDweights["damageTaken"] = -5.0
      lynPrimDweights["bossDead"] = 50.0
      lynPrimDweights["allEnemiesDead"] = 100.0

      lynPrimDweights["numArchersInRange"] = -2.5
      lynPrimDweights["numAxeUsersInRange"] = -.1
      lynPrimDweights["numLanceUsersInRange"] = -5.0
      lynPrimDweights["numSwordUsersInRange"] = -1.0
      lynPrimDweights["bossInRangeWhileEnemiesStillAlive"] = -10.0
      lynPrimDweights["bossInRangeWhileEnemiesAllDead"] = 2.0

      lynPrimDweights["inRangeOfOneUnit"] = -.2
      lynPrimDweights["inRangeOfTwoUnits"] = -3.0
      lynPrimDweights["inRangeOfThreeUnits"] = -4.0
      lynPrimDweights["inRangeOfFourUnits"] = -4.0
      lynPrimDweights["inRangeOfFiveUnitsOrMore"] = -5.0

      lynPrimDweights["nearestEnemyDistance"] = 1.0

      weights["lynPrimOweights"] = lynPrimOweights
      weights["lynPrimDweights"] = lynPrimDweights
      weights["lynSecOweights"] = lynSecOweights
      weights["lynSecDweights"] = lynSecDweights


      # kent
      kentPrimOweights = util.Counter()
      kentPrimDweights = util.Counter()
      kentSecOweights = util.Counter()
      kentSecDweights = util.Counter()

      # offensive (normal) weights (primary weapon - lance)
      kentPrimOweights["terrainDefBonus"] = 1.0
      kentPrimOweights["terrainAvoidBonus"] = 1.0

      kentPrimOweights["expectedDeath"] = -500.0
      kentPrimOweights["expectedKill"] = 5.0
      kentPrimOweights["damageGiven"] = 1.0
      kentPrimOweights["damageTaken"] = -1.0
      kentPrimOweights["bossDead"] = 50.0
      kentPrimOweights["allEnemiesDead"] = 100.0

      kentPrimOweights["numArchersInRange"] = 1.0
      kentPrimOweights["numAxeUsersInRange"] = -1.0
      kentPrimOweights["numLanceUsersInRange"] = .8
      kentPrimOweights["numSwordUsersInRange"] = 1.0
      kentPrimOweights["bossInRangeWhileEnemiesStillAlive"] = -5.0
      kentPrimOweights["bossInRangeWhileEnemiesAllDead"] = -2.0

      kentPrimOweights["inRangeOfOneUnit"] = 4.0
      kentPrimOweights["inRangeOfTwoUnits"] = 4.0
      kentPrimOweights["inRangeOfThreeUnits"] = 2.0
      kentPrimOweights["inRangeOfFourUnits"] = 1.0
      kentPrimOweights["inRangeOfFiveUnitsOrMore"] = -2.0

      kentPrimOweights["nearestEnemyDistance"] = -2.0


      # defensive weights (primary weapon)
      kentPrimDweights["terrainDefBonus"] = 3.0
      kentPrimDweights["terrainAvoidBonus"] = 3.0

      kentPrimDweights["expectedDeath"] = -500.0
      kentPrimDweights["expectedKill"] = 1.0
      kentPrimDweights["damageGiven"] = 1.0
      kentPrimDweights["damageTaken"] = -5.0
      kentPrimDweights["bossDead"] = 50.0
      kentPrimDweights["allEnemiesDead"] = 100.0

      kentPrimDweights["numArchersInRange"] = -2.5
      kentPrimDweights["numAxeUsersInRange"] = -4.0
      kentPrimDweights["numLanceUsersInRange"] = -1.0
      kentPrimDweights["numSwordUsersInRange"] = -1.0
      kentPrimDweights["bossInRangeWhileEnemiesStillAlive"] = -10.0
      kentPrimDweights["bossInRangeWhileEnemiesAllDead"] = 5.0

      kentPrimDweights["inRangeOfOneUnit"] = -.2
      kentPrimDweights["inRangeOfTwoUnits"] = -1.0
      kentPrimDweights["inRangeOfThreeUnits"] = -3.0
      kentPrimDweights["inRangeOfFourUnits"] = -4.0
      kentPrimDweights["inRangeOfFiveUnitsOrMore"] = -5.0

      kentPrimDweights["nearestEnemyDistance"] = 1.0

      
      # secondary weapon
      # offensive (normal) weights (secondary weapon)
      kentSecOweights["terrainDefBonus"] = 1.0
      kentSecOweights["terrainAvoidBonus"] = 1.0

      kentSecOweights["expectedDeath"] = -500.0
      kentSecOweights["expectedKill"] = 5.0
      kentSecOweights["damageGiven"] = 1.0
      kentSecOweights["damageTaken"] = -1.0
      kentSecOweights["bossDead"] = 50.0
      kentSecOweights["allEnemiesDead"] = 100.0

      kentSecOweights["numArchersInRange"] = 1.0
      kentSecOweights["numAxeUsersInRange"] = 3.0
      kentSecOweights["numLanceUsersInRange"] = -1.0
      kentSecOweights["numSwordUsersInRange"] = 1.0
      kentSecOweights["bossInRangeWhileEnemiesStillAlive"] = -5.0
      kentSecOweights["bossInRangeWhileEnemiesAllDead"] = 2.0

      kentSecOweights["inRangeOfOneUnit"] = 4.0
      kentSecOweights["inRangeOfTwoUnits"] = 3.0
      kentSecOweights["inRangeOfThreeUnits"] = 1.5
      kentSecOweights["inRangeOfFourUnits"] = .5
      kentSecOweights["inRangeOfFiveUnitsOrMore"] = -2.0

      kentSecOweights["nearestEnemyDistance"] = -2.0


      # defensive weights (secondary weapon)
      kentSecDweights["terrainDefBonus"] = 5.0
      kentSecDweights["terrainAvoidBonus"] = 5.0

      kentSecDweights["expectedDeath"] = -500.0
      kentSecDweights["expectedKill"] = 1.0
      kentSecDweights["damageGiven"] = 1.0
      kentSecDweights["damageTaken"] = -5.0
      kentSecDweights["bossDead"] = 50.0
      kentSecDweights["allEnemiesDead"] = 100.0

      kentSecDweights["numArchersInRange"] = -2.5
      kentSecDweights["numAxeUsersInRange"] = -.1
      kentSecDweights["numLanceUsersInRange"] = -4.0
      kentSecDweights["numSwordUsersInRange"] = -1.0
      kentSecDweights["bossInRangeWhileEnemiesStillAlive"] = -10.0
      kentSecDweights["bossInRangeWhileEnemiesAllDead"] = -2.0

      kentSecDweights["inRangeOfOneUnit"] = -.2
      kentSecDweights["inRangeOfTwoUnits"] = -2.0
      kentSecDweights["inRangeOfThreeUnits"] = -3.0
      kentSecDweights["inRangeOfFourUnits"] = -4.0
      kentSecDweights["inRangeOfFiveUnitsOrMore"] = -5.0

      kentSecDweights["nearestEnemyDistance"] = 1.0

      weights["kentPrimOweights"] = kentPrimOweights
      weights["kentPrimDweights"] = kentPrimDweights
      weights["kentSecOweights"] = kentSecOweights
      weights["kentSecDweights"] = kentSecDweights


      # sain
      sainPrimOweights = kentPrimOweights
      sainPrimDweights = kentPrimDweights
      sainSecOweights = kentSecOweights
      sainSecDweights = kentSecDweights

      weights["sainPrimOweights"] = sainPrimOweights
      weights["sainPrimDweights"] = sainPrimDweights
      weights["sainSecOweights"] = sainSecOweights
      weights["sainSecDweights"] = sainSecDweights
      


      #wil
      wilPrimOweights = util.Counter()
      wilPrimDweights = util.Counter()
      wilSecOweights = None
      wilSecDweights = None

      # offensive (normal) weights
      wilPrimOweights["terrainDefBonus"] = 1.0
      wilPrimOweights["terrainAvoidBonus"] = 1.0

      wilPrimOweights["expectedDeath"] = -500.0
      wilPrimOweights["expectedKill"] = 5.0
      wilPrimOweights["damageGiven"] = 2.0
      wilPrimOweights["damageTaken"] = -1.5
      wilPrimOweights["bossDead"] = 50.0
      wilPrimOweights["allEnemiesDead"] = 100.0

      wilPrimOweights["numArchersInRange"] = 1.0
      wilPrimOweights["numAxeUsersInRange"] = -.5
      wilPrimOweights["numLanceUsersInRange"] = -.5
      wilPrimOweights["numSwordUsersInRange"] = -.5
      wilPrimOweights["bossInRangeWhileEnemiesStillAlive"] = -5.0
      wilPrimOweights["bossInRangeWhileEnemiesAllDead"] = 1.0

      wilPrimOweights["inRangeOfOneUnit"] = 1.0
      wilPrimOweights["inRangeOfTwoUnits"] = -.2
      wilPrimOweights["inRangeOfThreeUnits"] = -4.0
      wilPrimOweights["inRangeOfFourUnits"] = -5.0
      wilPrimOweights["inRangeOfFiveUnitsOrMore"] = -7.0
      wilPrimOweights["adjacentToEnemy"] = -5000.0

      wilPrimOweights["nearestEnemyDistance"] = -.5


      # defensive weights
      wilPrimDweights["terrainDefBonus"] = 5.0
      wilPrimDweights["terrainAvoidBonus"] = 5.0

      wilPrimDweights["expectedDeath"] = -500.0
      wilPrimDweights["expectedKill"] = 1.0
      wilPrimDweights["damageGiven"] = 1.0
      wilPrimDweights["damageTaken"] = -5.0
      wilPrimDweights["bossDead"] = 50.0
      wilPrimDweights["allEnemiesDead"] = 100.0

      wilPrimDweights["numArchersInRange"] = -.2
      wilPrimDweights["numAxeUsersInRange"] = -10.0
      wilPrimDweights["numLanceUsersInRange"] = -10.0
      wilPrimDweights["numSwordUsersInRange"] = -10.0
      wilPrimDweights["bossInRangeWhileEnemiesStillAlive"] = -10.0
      wilPrimDweights["bossInRangeWhileEnemiesAllDead"] = 5.0

      wilPrimDweights["inRangeOfOneUnit"] = -.2
      wilPrimDweights["inRangeOfTwoUnits"] = -3.0
      wilPrimDweights["inRangeOfThreeUnits"] = -5.0
      wilPrimDweights["inRangeOfFourUnits"] = -6.0
      wilPrimDweights["inRangeOfFiveUnitsOrMore"] = -8.0
      wilPrimDweights["adjacentToEnemy"] = -100.0

      wilPrimDweights["nearestEnemyDistance"] = -.2

      weights["wilPrimOweights"] = wilPrimOweights
      weights["wilPrimDweights"] = wilPrimDweights
      weights["wilSecOweights"] = wilSecOweights
      weights["wilSecDweights"] = wilSecDweights

      #florina
      florinaPrimOweights = util.Counter()
      florinaPrimDweights = util.Counter()
      florinaSecOweights = None
      florinaSecDweights = None

      # offensive (normal) weights
      florinaPrimOweights["terrainDefBonus"] = 1.0
      florinaPrimOweights["terrainAvoidBonus"] = 1.0

      florinaPrimOweights["expectedDeath"] = -500.0
      florinaPrimOweights["expectedKill"] = 5.0
      florinaPrimOweights["damageGiven"] = 1.0
      florinaPrimOweights["damageTaken"] = -2.0
      florinaPrimOweights["bossDead"] = 50.0
      florinaPrimOweights["allEnemiesDead"] = 100.0

      florinaPrimOweights["numArchersInRange"] = -500.0
      florinaPrimOweights["numAxeUsersInRange"] = -2.0
      florinaPrimOweights["numLanceUsersInRange"] = 0
      florinaPrimOweights["numSwordUsersInRange"] = 1.0
      florinaPrimOweights["bossInRangeWhileEnemiesStillAlive"] = -6.0
      florinaPrimOweights["bossInRangeWhileEnemiesAllDead"] = -.1

      florinaPrimOweights["inRangeOfOneUnit"] = .2
      florinaPrimOweights["inRangeOfTwoUnits"] = -2.0
      florinaPrimOweights["inRangeOfThreeUnits"] = -3.0
      florinaPrimOweights["inRangeOfFourUnits"] = -5.0
      florinaPrimOweights["inRangeOfFiveUnitsOrMore"] = -10.0

      florinaPrimOweights["nearestEnemyDistance"] = -.2


      # defensive weights
      florinaPrimDweights["terrainDefBonus"] = 5.0
      florinaPrimDweights["terrainAvoidBonus"] = 5.0

      florinaPrimDweights["expectedDeath"] = -500.0
      florinaPrimDweights["expectedKill"] = 1.0
      florinaPrimDweights["damageGiven"] = 1.0
      florinaPrimDweights["damageTaken"] = -5.0
      florinaPrimDweights["bossDead"] = 50.0
      florinaPrimDweights["allEnemiesDead"] = 100.0

      florinaPrimDweights["numArchersInRange"] = -20.0
      florinaPrimDweights["numAxeUsersInRange"] = -3.0
      florinaPrimDweights["numLanceUsersInRange"] = -1.0
      florinaPrimDweights["numSwordUsersInRange"] = -.2
      florinaPrimDweights["bossInRangeWhileEnemiesStillAlive"] = -10.0
      florinaPrimDweights["bossInRangeWhileEnemiesAllDead"] = -5.0

      florinaPrimDweights["inRangeOfOneUnit"] = -1.0
      florinaPrimDweights["inRangeOfTwoUnits"] = -3.0
      florinaPrimDweights["inRangeOfThreeUnits"] = -5.0
      florinaPrimDweights["inRangeOfFourUnits"] = -6.0
      florinaPrimDweights["inRangeOfFiveUnitsOrMore"] = -15.0

      florinaPrimDweights["nearestEnemyDistance"] = 1.0

      weights["florinaPrimOweights"] = florinaPrimOweights
      weights["florinaPrimDweights"] = florinaPrimDweights
      weights["florinaSecOweights"] = florinaSecOweights
      weights["florinaSecDweights"] = florinaSecDweights

      return weights

def main():
      numGames = 0
      maxGames = 150
      iteration = 0

      discountFactor = .99
      learningRate = .7
      explorationRate = 1.0

      weights = createWeights()

      while( numGames < maxGames):

            print "Starting Game ", numGames

            # start new game
            game = runGame("bom", weights)
            #game.Display()

            turn = 0
            maxTurns = 100
            while not game.hasEnded():

                  #print "Turn = " + str(turn)

                  allyCharacters = game.getAllyCharacters()        
                  enemyCharacters = game.getEnemyCharacters()

                  allAllyCharNames = []
                  for character in allyCharacters:
                        allAllyCharNames.append( character.getName() )

                  rewards = util.Counter()
                  baseFeatures = util.Counter()
                  baseEvaluationScores = util.Counter()
                  endEvaluationScores = util.Counter()
                  useOffensiveWeights = util.Counter()

                  for character in allyCharacters:
                        # damage given, damage taken, enemies killed, hero killed
                        rewards[character.getName()] = (0, 0, 0, 0)

                  for allyCharacter in allyCharacters:

                        # get ally char's current position
                        allCharacters = game.gameboard.getCharacters()
                        allyCharPos = (0,0)
                        for charTuple in allCharacters:
                              if charTuple[0] == allyCharacter:
                                    allyCharPos = charTuple[1]

                        evalResult = game.ai.evaluationFunctionRL(allyCharacter, False, allyCharPos, None)
                        baseEvaluationScore = evalResult[0]
                        features = evalResult[1]

                        offensiveWeights = 0
                        healthThreshold = 7
                        if allyCharacter.getCurrentHealth() >= healthThreshold:
                              offensiveWeights = 1

                        result = 0

                        if random.randrange(0,100) < explorationRate*100:
                              result = game.ai.randomMoveRL(allyCharacter)
                        else:
                              result = game.ai.calculateMoveRL(allyCharacter)

                        if result == None:
                              #print "Already acted"
                              continue

                        position = result[0]
                        #print position
                        enemyCharacter = result[2]
                        #print enemyCharacter
                        switch = result[1]
                        #print switch

                        endEvaluationScore = result[3]

                        allyCharName = allyCharacter.getName()

                        baseFeatures[allyCharName] = features
                        baseEvaluationScores[allyCharName] = baseEvaluationScore
                        endEvaluationScores[allyCharName] = endEvaluationScore
                        useOffensiveWeights[allyCharName] = offensiveWeights

                        if switch:
                              allyCharacter.switchWeapons()

                        game.gameboard.moveCharacter(allyCharacter, position[0], position[1])

                        if enemyCharacter != None:
                              fightResult = game.gameboard.fightRL(allyCharacter, enemyCharacter)

                              enemyDamage = fightResult[0]
                              heroDamage = fightResult[1]
                              heroDead = fightResult[2]
                              enemyDead = fightResult[3]

                              charRewards = list(rewards[allyCharName])
                              charRewards[0] += enemyDamage
                              charRewards[1] += heroDamage
                              charRewards[2] += enemyDead
                              charRewards[3] += heroDead
                              rewards[allyCharName] = tuple(charRewards)

                        if game.hasEnded():
                              break

                  # recalculate characters in case some have died
                  allyCharacters = game.getAllyCharacters()        
                  enemyCharacters = game.getEnemyCharacters()

                  for enemyCharacter in enemyCharacters:
                        result = game.ai.calculateMoveRL(enemyCharacter)

                        if result == None:
                              #print "Already acted"
                              continue

                        position = result[0]
                        #print position
                        allyCharacter = result[2]
                        #print allyCharacter
                        switch = result[1]
                        #print switch

                        if switch:
                              enemyCharacter.switchWeapons()

                        game.gameboard.moveCharacter(enemyCharacter, position[0], position[1])

                        if allyCharacter != None:
                              allyCharName = allyCharacter.getName()

                              fightResult = game.gameboard.fightRL(enemyCharacter, allyCharacter)

                              heroDamage = fightResult[0]
                              enemyDamage = fightResult[1]
                              enemyDead = fightResult[2]
                              heroDead = fightResult[3]

                              charRewards = list(rewards[allyCharName])

                              charRewards[0] += enemyDamage
                              charRewards[1] += heroDamage
                              charRewards[2] += enemyDead
                              charRewards[3] += heroDead

                              rewards[allyCharName] = tuple(charRewards)

                        if game.hasEnded():
                              break

                  game.gameboard.endTurnRL()

                  #game.Display()

                  turn += 1 
                  iteration += 1

                  if game.gameboard.isWin():
                        print "WIN"
                  #else:
                  #      print "FAIL"

                  totalDamageDealt = 0
                  totalDamageTaken = 0
                  totalEnemiesKilled = 0
                  totalAlliesKilled = 0

                  for charName in allAllyCharNames:
                        totalDamageDealt += rewards[charName][0]
                        totalDamageTaken += rewards[charName][1]
                        totalEnemiesKilled += rewards[charName][2]
                        totalAlliesKilled += rewards[charName][3]

                  sharedReward = 0
                  if game.gameboard.isWin():
                        sharedReward += 1000
                  if game.gameboard.isLose():
                        sharedReward -= 1000

                  sharedReward += .25*totalDamageDealt*.1
                  sharedReward -= .25*totalDamageTaken*.1
                  sharedReward += .25*totalEnemiesKilled*10
                  sharedReward -= .25*totalAlliesKilled*100

                  for charName in allAllyCharNames:
                        damageGiven = rewards[charName][0]
                        damageTaken = rewards[charName][1]
                        enemiesKilled = rewards[charName][2]
                        allyKilled = rewards[charName][3]

                        characterRewards = (.1*damageGiven) - (.1*damageTaken) + (10*enemiesKilled) - (100*allyKilled)

                        finalReward = sharedReward + characterRewards

                        baseEvaluationScore = baseEvaluationScores[charName]
                        endEvaluationScore = endEvaluationScores[charName]
                        features = baseFeatures[charName]

                        # not really sure why this bug happens sometimes
                        if features == 0:
                              continue

                        charWeights = 0
                        if useOffensiveWeights[charName] == 1:
                              charWeights = character.getPrimOffensiveWeights()
                        else:
                              charWeights = character.getPrimDefensiveWeights()

                        newWeights = reinforcement.RL(character, charWeights, baseEvaluationScore, endEvaluationScore, features, finalReward, learningRate, discountFactor)

                        if useOffensiveWeights[charName] == 1:
                              character.setPrimOffensiveWeights(newWeights)

                              if character.getName() == "Lyn":
                                    weights["lynPrimOweights"] = newWeights

                              elif character.getName() == "Kent":

                                    if character.getWeaponType() == "lance":
                                          weights["kentPrimOweights"] = newWeights

                                    else:
                                          weights["kentSecOweights"] = newWeights

                              elif character.getName() == "Sain":

                                    if character.getWeaponType() == "lance":
                                          weights["sainPrimOweights"] = newWeights

                                    else:
                                          weights["sainSecOweights"] = newWeights

                              elif character.getName() == "Wil":
                                    weights["wilPrimOweights"] = newWeights

                              else:
                                    weights["florinaPrimOweights"] = newWeights

                        else:
                              character.setPrimDefensiveWeights(newWeights)

                              if character.getName() == "Lyn":
                                    weights["lynPrimDweights"] = newWeights

                              elif character.getName() == "Kent":

                                    if character.getWeaponType() == "lance":
                                          weights["kentPrimDweights"] = newWeights
                                    else:
                                          weights["kentSecDweights"] = newWeights

                              elif character.getName() == "Sain":

                                    if character.getWeaponType() == "lance":
                                          weights["sainPrimDweights"] = newWeights

                                    else:
                                          weights["sainSecDweights"] = newWeights

                              elif character.getName() == "Wil":
                                    weights["wilPrimDweights"] = newWeights

                              else:
                                    weights["florinaPrimDweights"] = newWeights

                  if turn >= maxTurns:
                        break

            numGames += 1

            if (numGames%15) == 0:
                  explorationRate -= .1
                  learningRate -= .04

      explorationRate = 0

      #output final weights
      weightKeys  = weights.keys()
      for key in weightKeys:
            print "Printing ", key, ": "
            print weights[key]

      '''

      f = open('resultsInitialized.txt','w')
      for key in weightKeys:
            f.write(str(key))
            f.write('\n')
            f.write(str(weights[key]))
            f.write('\n')
            f.write('\n')
      f.close()

      '''

      print "ENTERING TESTING PHASE"

      numGames = 0
      maxGames = 50
      iteration = 0

      wins = 0

      while( numGames < maxGames):

            print "Starting Game ", numGames

            # start new game
            game = runGame("bom", weights)
            #game.Display()

            turn = 0
            maxTurns = 100
            while not game.hasEnded():

                  #print "Turn = " + str(turn)

                  allyCharacters = game.getAllyCharacters()        
                  enemyCharacters = game.getEnemyCharacters()



                  for allyCharacter in allyCharacters:

                        result = game.ai.calculateMoveRL(allyCharacter)

                        if result == None:
                              continue

                        position = result[0]
                        #print position
                        enemyCharacter = result[2]
                        #print enemyCharacter
                        switch = result[1]
                        #print switch

                        endEvaluationScore = result[3]


                        if switch:
                              allyCharacter.switchWeapons()

                        game.gameboard.moveCharacter(allyCharacter, position[0], position[1])

                        if enemyCharacter != None:
                              game.gameboard.fightRL(allyCharacter, enemyCharacter)


                        if game.hasEnded():
                              break

                  # recalculate characters in case some have died
                  allyCharacters = game.getAllyCharacters()        
                  enemyCharacters = game.getEnemyCharacters()

                  for enemyCharacter in enemyCharacters:
                        result = game.ai.calculateMoveRL(enemyCharacter)

                        if result == None:
                              #print "Already acted"
                              continue

                        position = result[0]
                        #print position
                        allyCharacter = result[2]
                        #print allyCharacter
                        switch = result[1]
                        #print switch

                        if switch:
                              enemyCharacter.switchWeapons()

                        game.gameboard.moveCharacter(enemyCharacter, position[0], position[1])

                        if allyCharacter != None:

                              game.gameboard.fightRL(enemyCharacter, allyCharacter)


                        if game.hasEnded():
                              break

                  game.gameboard.endTurnRL()

                  #game.Display()

                  turn += 1 
                  iteration += 1

                  if game.gameboard.isWin():
                        print "WIN"
                        wins += 1
                  #else:
                  #      print "FAIL"


                  if turn >= maxTurns:
                        break

            numGames += 1

      #output final statistics
      print "Wins: ", wins
      print "Losses: ", maxGames - wins



if __name__ == "__main__":
    main()
