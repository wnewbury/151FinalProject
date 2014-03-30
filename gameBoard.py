class gameBoard
    def __init__(self, board, characters, height, width, mapLords):
        self.height = height
        self.width = width
        self.board = board
        self.characters = characters
        self.lords = mapLords

    
    def getBoard():
        return self.board

    def getCharacters():
        return self.characters

    def isLose():
        lords = 0
        for x in height:
            for y in width:
                if characters == 0:
                    continue
                elif characters[x][y].type == "lord":
                    lords += 1
                else:
                    continue

        if lords == self.lords:
            return false
        else:
            return true

    def isWin():
        enemies = 0
        for x in height:
            for y in width:
                if characters[x][y] and characters[x][y].faction == "enemy"
                    enemies += 1

        if enemies == 0:
            return true
        else:
            return false
