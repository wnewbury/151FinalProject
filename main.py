from gameBoard import gameBoard
from character import weapon, character, stats
from ai import ai
import random

import util

class runGame:
    def __init__(self, mapName):
        self.mapBoard = self.generateBoard(mapName)
        self.mapCharacters = self.generateCharacters(mapName)
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

    def generateCharacters(self, mapName):
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
            lynPrimOweights["damageTaken"] = -1.5
            lynPrimOweights["bossDead"] = 50.0
            lynPrimOweights["allEnemiesDead"] = 100.0

            lynPrimOweights["numArchersInRange"] = -.5
            lynPrimOweights["numAxeUsersInRange"] = 1.0
            lynPrimOweights["numLanceUsersInRange"] = -1.0
            lynPrimOweights["numSwordUsersInRange"] = 0
            lynPrimOweights["bossInRangeWhileEnemiesStillAlive"] = -5.0
            lynPrimOweights["bossInRangeWhileEnemiesAllDead"] = 1.0

            lynPrimOweights["inRangeOfOneUnit"] = 1.0
            lynPrimOweights["inRangeOfTwoUnits"] = 1.0
            lynPrimOweights["inRangeOfThreeUnits"] = 1.0
            lynPrimOweights["inRangeOfFourUnits"] = -.5
            lynPrimOweights["inRangeOfFiveUnitsOrMore"] = -1.0

            lynPrimOweights["nearestEnemyDistance"] = -.2


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
            lynPrimDweights["bossInRangeWhileEnemiesAllDead"] = -2.0

            lynPrimDweights["inRangeOfOneUnit"] = -.2
            lynPrimDweights["inRangeOfTwoUnits"] = -2.0
            lynPrimDweights["inRangeOfThreeUnits"] = -4.0
            lynPrimDweights["inRangeOfFourUnits"] = -4.0
            lynPrimDweights["inRangeOfFiveUnitsOrMore"] = -5.0

            lynPrimDweights["nearestEnemyDistance"] = 1.0


            lynStats = stats(17, 5, 10, 12, 7, 3, 0, 5, 5)
            lyn = character("Lyn", "Lord", ironSword, None, False, False, lynStats, 17, lynPrimOweights, lynPrimDweights, lynSecOweights, lynSecDweights)


            #kent
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

            kentPrimOweights["numArchersInRange"] = -.5
            kentPrimOweights["numAxeUsersInRange"] = -1.0
            kentPrimOweights["numLanceUsersInRange"] = .25
            kentPrimOweights["numSwordUsersInRange"] = 2.0
            kentPrimOweights["bossInRangeWhileEnemiesStillAlive"] = -5.0
            kentPrimOweights["bossInRangeWhileEnemiesAllDead"] = -2.0

            kentPrimOweights["inRangeOfOneUnit"] = 2.0
            kentPrimOweights["inRangeOfTwoUnits"] = 1.5
            kentPrimOweights["inRangeOfThreeUnits"] = 1.0
            kentPrimOweights["inRangeOfFourUnits"] = 1.0
            kentPrimOweights["inRangeOfFiveUnitsOrMore"] = -.5



            kentPrimOweights["nearestEnemyDistance"] = -.2

            # defensive weights (primary weapon)
            kentPrimDweights["terrainDefBonus"] = 5.0
            kentPrimDweights["terrainAvoidBonus"] = 5.0

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
            kentPrimDweights["bossInRangeWhileEnemiesAllDead"] = -5.0

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

            kentSecOweights["numArchersInRange"] = -.25
            kentSecOweights["numAxeUsersInRange"] = 2.0
            kentSecOweights["numLanceUsersInRange"] = -1.0
            kentSecOweights["numSwordUsersInRange"] = .5
            kentSecOweights["bossInRangeWhileEnemiesStillAlive"] = -5.0
            kentSecOweights["bossInRangeWhileEnemiesAllDead"] = 2.0

            kentSecOweights["inRangeOfOneUnit"] = 2.0
            kentSecOweights["inRangeOfTwoUnits"] = 2.0
            kentSecOweights["inRangeOfThreeUnits"] = 1.5
            kentSecOweights["inRangeOfFourUnits"] = .5
            kentSecOweights["inRangeOfFiveUnitsOrMore"] = -.5

            kentSecOweights["nearestEnemyDistance"] = -.2


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

            kentStats = stats(21, 7, 7, 7, 2, 7, 1, 9, 7)
            kent = character("Kent", "Cavalier", ironSword, ironLance, False, False, kentStats, 21, kentPrimOweights, kentPrimDweights, kentSecOweights, kentSecDweights)


            #sain
            sainPrimOweights = kentPrimOweights
            sainPrimDweights = kentPrimDweights
            sainSecOweights = kentSecOweights
            sainSecDweights = kentSecDweights

            sainStats = stats(20, 9, 6, 8, 4, 6, 0, 9, 7)
            sain = character("Sain", "Cavalier", ironSword, ironLance, False, False, sainStats, 20, sainPrimOweights, sainPrimDweights, sainSecOweights, sainSecDweights)


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

            wilPrimOweights["nearestEnemyDistance"] = -.2


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
            wilPrimDweights["bossInRangeWhileEnemiesAllDead"] = 10

            wilPrimDweights["inRangeOfOneUnit"] = -.2
            wilPrimDweights["inRangeOfTwoUnits"] = -3.0
            wilPrimDweights["inRangeOfThreeUnits"] = -5.0
            wilPrimDweights["inRangeOfFourUnits"] = -6.0
            wilPrimDweights["inRangeOfFiveUnitsOrMore"] = -8.0

            wilPrimDweights["nearestEnemyDistance"] = -.2

            wilStats = stats(20, 6, 5, 5, 6, 5, 0, 6, 5)
            wil = character("Wil", "Archer", ironBow, None, False, False, wilStats, 20, wilPrimOweights, wilPrimDweights, wilSecOweights, wilSecDweights)


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

            florinaPrimOweights["numArchersInRange"] = -7.0
            florinaPrimOweights["numAxeUsersInRange"] = -1.0
            florinaPrimOweights["numLanceUsersInRange"] = 0
            florinaPrimOweights["numSwordUsersInRange"] = 1.0
            florinaPrimOweights["bossInRangeWhileEnemiesStillAlive"] = -6.0
            florinaPrimOweights["bossInRangeWhileEnemiesAllDead"] = -.1

            florinaPrimOweights["inRangeOfOneUnit"] = 1.0
            florinaPrimOweights["inRangeOfTwoUnits"] = .5
            florinaPrimOweights["inRangeOfThreeUnits"] = -.5
            florinaPrimOweights["inRangeOfFourUnits"] = -2.0
            florinaPrimOweights["inRangeOfFiveUnitsOrMore"] = -4.0

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

            florinaPrimDweights["inRangeOfOneUnit"] = -.2
            florinaPrimDweights["inRangeOfTwoUnits"] = -3.0
            florinaPrimDweights["inRangeOfThreeUnits"] = -5.0
            florinaPrimDweights["inRangeOfFourUnits"] = -6.0
            florinaPrimDweights["inRangeOfFiveUnitsOrMore"] = -7.0

            florinaPrimDweights["nearestEnemyDistance"] = 1.0

            florinaStats = stats(17, 5, 7, 9, 7, 4, 4, 4, 7)
            florina = character("Florina", "PegKnight", slimLance, None, False, False, florinaStats, 17, florinaPrimOweights, florinaPrimDweights, florinaSecOweights, florinaSecDweights)
            


            #enemies

            #L1 Brigands
            L1BrigandPrimOweights = util.Counter()
            L1BrigandPrimDweights = util.Counter()
            L1BrigandSecOweights = None
            L1BrigandSecDweights = None

            L1BrigandStats = stats(20, 5, 1, 5, 0, 3, 0, 12, 5)
            brigand1 = character("Brig1", "Brigand", ironAxe, None, True, False, L1BrigandStats, 20, L1BrigandPrimOweights, L1BrigandPrimDweights, L1BrigandSecOweights, L1BrigandSecDweights)

            #L2 Brigands
            L2BrigandPrimOweights = util.Counter()
            L2BrigandPrimDweights = util.Counter()
            L2BrigandSecOweights = None
            L2BrigandSecDweights = None

            L2BrigandStats = L1BrigandStats
            brigand2 = character("Brig2", "Brigand", ironAxe, None, True, False, L2BrigandStats, 20, L2BrigandPrimOweights, L2BrigandPrimDweights, L2BrigandSecOweights, L2BrigandSecDweights)
            brigand3 = character("Brig3", "Brigand", ironAxe, None, True, False, L2BrigandStats, 20, L2BrigandPrimOweights, L2BrigandPrimDweights, L2BrigandSecOweights, L2BrigandSecDweights)

            #Mercs
            mercPrimOweights = util.Counter()
            mercPrimDweights = util.Counter()
            mercSecOweights = None
            mercSecDweights = None

            mercenaryStats = stats(16, 3, 5, 6, 0, 2, 0, 8, 5)
            merc1 = character("Merc1", "Mercenary", ironSword, None, True, False, mercenaryStats, 16, mercPrimOweights, mercPrimDweights, mercSecOweights, mercSecDweights)
            merc2 = character("Merc2", "Mercenary", ironSword, None, True, False, mercenaryStats, 16, mercPrimOweights, mercPrimDweights, mercSecOweights, mercSecDweights)

            #Archers
            archerPrimOweights = util.Counter()
            archerPrimDweights = util.Counter()
            archerSecOweights = None
            archerSecDweights = None

            archerStats = stats(17, 3, 3, 3, 0, 3, 0, 6, 5)
            archer1 = character("Archer1", "Archer", ironBow, None, True, False, archerStats, 17, archerPrimOweights, archerPrimDweights, archerSecOweights, archerSecDweights)
            archer2 = character("Archer2", "Archer", ironBow, None, True, False, archerStats, 17, archerPrimOweights, archerPrimDweights, archerSecOweights, archerSecDweights)

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
            mapCharacters[4][8] = brigand1
            mapCharacters[8][13] = brigand2
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
            if not character[0].isEnemy():
                Allies.append(character[0])
        random.shuffle(Allies)
        return Allies

    def getEnemyCharacters(self):
        characters = self.gameboard.getCharacters()
        Enemies = []
        for character in characters:
            if character[0].isEnemy():
                Enemies.append(character[0])
        random.shuffle(Enemies)        
        return Enemies

def main():
    game = runGame("bom")

    game.Display()

    turn = 0
    while not game.hasEnded():
        #game.askInput()
        
        if turn % 2 == 0:
            characters = game.getAllyCharacters()
        else:
            characters = game.getEnemyCharacters()

        for character in characters:
            result = game.ai.calculateMove(character)

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

            game.gameboard.moveCharacter(character, position[0], position[1])

            if character2 != None:
                game.gameboard.fight(character, character2)

            if game.hasEnded():
                break

        game.gameboard.endTurn()

        game.Display()

        turn += 1
        
        print "Turn = " + str(turn)




    print "interesting"


if __name__ == "__main__":
    main()
