class runGame:
    def __init__(mapName):
        self.mapBoard = self.generateBoard(mapName)
        self.mapCharacters = self.generateCharacters(mapName)
        self.height = len(self.board)
        self.width = len(self.board(1))

    def generateBoard(self, mapName):
        mapBoard = [[]]
        if mapName = "bom":
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
        else:
            continue

        return mapBoard

    def generateCharacters(self, mapName):
        mapBoard = [[]]
        if mapName = "bom":
            
        
