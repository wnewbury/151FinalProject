import sys

class gameBoard:
    def __init__(self, board, characters, height, width, mapLords):
        self.height = height
        self.width = width
        self.lords = mapLords
        self.board = [[None for i in xrange(width)] for i in xrange(height)]
        
        for x in range(height):
            for y in range(width):
                self.board[x][y] = gameSpace(characters[x][y], board[x][y])
    
    def getTerrain(self, x, y):
        return self.board[x][y].getTerrain()

    def getCharacters(self):
        characters = list()
        for x in range(self.height):
            for y in range(self.width):
                character = self.board[x][y].getCharacter()
                if character != False:
                    characters.append((character, (x,y)))

        return characters
                

    def isLose(self):
        lords = 0
        for x in range(height):
            for y in range(width):
                if self.board[x][y].hasLord():
                    lord += 1

        if lords == self.lords:
            return false
        else:
            return true

    def isWin(self):
        enemies = 0
        for x in range(height):
            for y in range(width):
                if self.board[x][y].hasLord():
                    enemies += 1

        if enemies == 0:
            return true
        else:
            return false

    def Display(self):
        for x in xrange(self.height):
            for i in self.board[x]:
                character = i.getCharacter()
                if character != False:
                    sys.stdout.write("migal" + " ")
                else:
                    sys.stdout.write(str(i.getTerrain()) + " ")
                sys.stdout.flush()
            print "\n"

class gameSpace:
    def __init__(self, character, terrain):
        self.character = character
        self.terrain = terrain

    def getTerrain(self):
        return self.terrain

    def getCharacter(self):
        if self.character != None:
            return self.character
        else:
            return False

    def isFilled(self):
        return self.character == None

    def hasLord(self):
        return self.character.isLord()

    def hasEnemy(self):
        return self.character.isEnemy()
    
