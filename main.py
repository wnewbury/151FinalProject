from gameBoard import gameBoard

class runGame:
    def __init__(self, mapName):
        self.mapBoard = self.generateBoard(mapName)
        self.mapCharacters = self.generateCharacters(mapName)
        self.height = len(self.mapBoard)
        self.width = len(self.mapBoard[0])
        self.gameBoard = gameBoard(self.mapBoard, self.mapCharacters,
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

            #Need to implement characters first
            #mapCharacters[5][5] = 4

        return mapCharacters


def main():
    game = runGame("bom")
    game.gameBoard.Display()
    
    

if __name__ == "__main__":
    main()
