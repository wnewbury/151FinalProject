from gameBoard import gameBoard
from character import weapon, character, stats
from ai import ai

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
                    [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
                    [0,3,1,1,1,1,1,1,1,1,1,0,0,2,0],
                    [0,0,1,1,1,0,0,1,0,0,2,0,1,1,1],
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
            ironAxe = weapon("Iron Axe", "axe", 8, .75, 0, 1, 10)
            steelAxe = weapon("Steel Axe", "axe", 11, .65, 0, 1, 15)
            
            ironSword = weapon("Iron Sword", "sword", 5, .90, 0, 1, 5)
            maniKatti = weapon("Mani Katti", "sword", 8, .80, .20, 1, 3)

            slimLance = weapon("Slim Lance", "lance", 4, .85, .05, 1, 4)
            ironLance = weapon("Iron Lance", "lance", 7, .80, 0, 1, 8)

            ironBow = weapon("Iron Bow", "bow", 6, .85, 0, 2, 5)

            #characters
            lynStats = stats(17, 4, 8, 10, 6, 2, 0, 5, 5)
            lyn = character("Lyn", "Lord", ironSword, None, False, False, lynStats, 17)

            kentStats = stats(21, 6, 6, 7, 2, 5, 1, 9, 7)
            kent = character("Kent", "Cavalier", ironSword, ironLance, False, False, kentStats, 21)

            sainStats = stats(20, 8, 5, 7, 4, 6, 0, 9, 7)
            sain = character("Sain", "Cavalier", ironSword, ironLance, False, False, sainStats, 20)

            wilStats = stats(20, 6, 5, 5, 6, 5, 0, 6, 5)
            wil = character("Wil", "Archer", ironBow, None, False, False, wilStats, 20)

            florinaStats = stats(17, 5, 7, 9, 7, 4, 4, 4, 7)
            florina = character("Florina", "PegKnight", slimLance, None, False, False, florinaStats, 17)
            
            #enemies
            L1BrigandStats = stats(20, 5, 1, 5, 0, 3, 0, 12, 5)
            brigand1 = character("Brig1", "Brigand", ironAxe, None, True, False, L1BrigandStats, 20)

            L2BrigandStats = L1BrigandStats
            brigand2 = character("Brig2", "Brigand", ironAxe, None, True, False, L2BrigandStats, 20)
            brigand3 = character("Brig3", "Brigand", ironAxe, None, True, False, L2BrigandStats, 20)

            mercenaryStats = stats(16, 3, 5, 6, 0, 2, 0, 8, 5)
            merc1 = character("Merc1", "Mercenary", ironSword, None, True, False, mercenaryStats, 16)
            merc2 = character("Merc2", "Mercenary", ironSword, None, True, False, mercenaryStats, 16)

            archerStats = stats(17, 3, 3, 3, 0, 3, 0, 6, 5)
            archer1 = character("Archer1", "Archer", ironBow, None, True, False, archerStats, 17)
            archer2 = character("Archer2", "Archer", ironBow, None, True, False, archerStats, 17)

            migalStats = stats(25, 7, 3, 5, 2, 5, 0, 12, 5)
            migal = character("Migal", "Brigand", steelAxe, None, True, True, migalStats, 25)


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

            self.Display()
        elif command == "attack":
            char1 = raw_input("Input name of character to attack with: ")
            character1 = self.getCharacterByName(char1) 
            while character1 == False:
                char1 = raw_input("Reinput name: ")
                character = self.getCharacterByName(char1)

            char2 = raw_input("Input name of character to attack: ")
            character2 = self.getCharacterByName(char2)
            while character2 == False:
                char2 = raw_input("Reinput name: ")
                character = self.getCharacterByName(char2)

            self.gameboard.fight(character1, character2)

            self.Display()
        elif command == "endTurn":
            self.gameboard.endTurn()

    def Display(self):
        self.gameboard.Display()


    def hasEnded(self):
        return self.gameboard.isWin() or self.gameboard.isLose()
    #To be used at some point
    #def playTurn(self):
        #self.gameboard.getCharacters()

    def calculateMove(self, character):
        return self.ai.calculateMove(character)



def main():
    game = runGame("bom")

    game.Display()

    game.calculateMove(game.getCharacterByName("Sain"))
    #while not game.hasEnded():
    #    game.askInput()

    #print "interesting"


if __name__ == "__main__":
    main()
