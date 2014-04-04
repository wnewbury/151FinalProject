from gameBoard import gameBoard
from character import weapon, character, stats

class runGame:
    def __init__(self, mapName):
        self.mapBoard = self.generateBoard(mapName)
        self.mapCharacters = self.generateCharacters(mapName)
        self.height = len(self.mapBoard)
        self.width = len(self.mapBoard[0])
        self.gameboard = gameBoard(self.mapBoard, self.mapCharacters,
                                   self.height, self.width, self.mapLords)

    def generateBoard(self, mapName):
        mapBoard = [[]]
        if mapName == "bom":
            mapBoard = [[0,0,0,0,0,1,0,0,0,2,0,0,0,0,3],
                    [0,1,1,1,0,0,0,0,2,0,0,1,1,1,0],
                    [0,1,1,1,0,1,0,0,0,0,0,1,0,1,1],
                    [2,0,0,0,0,1,1,1,0,0,0,2,0,0,0],
                    [1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
                    [0,2,1,1,1,1,1,1,1,1,1,0,0,2,0],
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
            #lynStats = stats(FIX)
            #lyn = character("Lyn", "Lord", maniKatti, None, False, lynStats, FIX)

            #kentStats = stats(FIX)
            #kent = character("Kent", "Cavalier", ironSword, ironLance, False, kentStats, FIX)

            #sainStats = stats(FIX)
            #kent = character("Sain", "Cavalier", ironSword, ironLance, False, sainStats, FIX)

            wilStats = stats(20, 6, 5, 5, 6, 5, 0, 6, 5)
            wil = character("Wil", "Archer", ironBow, None, False, wilStats, 20)

            florinaStats = stats(17, 5, 7, 9, 7, 4, 4, 4, 7)
            florina = character("Florina", "PegKnight", slimLance, None, False, florinaStats, 17)

            #enemies
            #L1BrigandStats = stats(FIX)
            #brigand1 = character("Brigand1", "Brigand", ironAxe, None, True, L1BrigandStats, FIX)

            #L2BrigandStats = stats(FIX)
            #brigand2 = character("Brigand2", "Brigand", ironAxe, None, True, L2BrigandStats, FIX)
            #brigand3 = character("Brigand3", "Brigand", ironAxe, None, True, L2BrigandStats, FIX)

            #mercenayStats = stats(FIX)
            #merc1 = character("Merc1", "Mercenary", ironSword, None, True, mercenaryStats, FIX)
            #merc2 = character("Merc2", "Mercenary", ironSword, None, True, mercenaryStats, FIX)
            #merc3 = character("Merc3", "Mercenary", ironSword, None, True, mercenaryStats, FIX)

            #archerStats = stats(FIX)
            #archer1 = character("Archer1", "Archer", ironBow, None, True, archerStats, FIX)
            #archer2 = character("Archer2", "Archer", ironBow, None, True, archerStats, FIX)

            migalStats = stats(25, 7, 3, 5, 2, 5, 0, 12, 5)
            migal = character("Migal", "Brigand", steelAxe, None, True, migalStats, 25)


            #Need to implement characters first
            mapCharacters[5][5] = migal

            mapCharacters[7][5] = florina

        return mapCharacters

    def getCharacterAtPosition(self, position):
        characters = self.gameboard.getCharacters()

        for characterTuple in characters:
            if characterTuple[1] == position:
                return characterTuple[0]
            else:
                print "no character at position"

    def getCharacterByName(self, name):
        characters = self.gameboard.getCharacters()

        for characterTuple in characters:
            if characterTuple[0].getName() == name:
                return characterTuple[0]
            else:
                print "character does not exist"

    #def playPlayTurn():
        #self.gameboard.getCharacters()

        #self.getCharacterByName("Lyn")

        #kent


def main():
    game = runGame("bom")
    gameboard = game.gameboard


    gameboard.Display()
    migal = game.getCharacterAtPosition((5, 5))

    print "______________________________"

    gameboard.moveCharacter(migal, 6, 5)
    gameboard.Display()
    
    

if __name__ == "__main__":
    main()
