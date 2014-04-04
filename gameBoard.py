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

    def manhattanDistance(self, p1x, p1y, p2x, p2y):
        return abs(p1x - p2x) + abs(p1y - p2y)

    def moveCharacter(self, inputChar, newx, newy):
        for x in range(self.height):
            for y in range(self.width):
                character = self.board[x][y].getCharacter()
                if character != False and inputChar == character:
                    if self.isValidMove(x, y, newx, newy, character.getRange()):
                        self.board[x][y].changeCharacter(None)
                        self.board[newx][newy].changeCharacter(character)
                        return
                    else:
                        print "invalid move"
        print "No such character to move"

    def obtainBestMove(self, character, position):
        #Insert heuristic!!! (Call out to another class, probably?)
        print "meh"

    def fight(self, character1, character2):
        #NOTE: does not currently account for terrain
        p1x, p2x, p2y, p1y = 0, 0, 0, 0
        for x in range(self.height):
            for y in range(self.width):
                character = self.board[x][y].getCharacter()
                if character == character1:
                    p1x = x
                    p1y = y
                if character == character2:
                    p2x = x
                    p2y = y
        dist = self.manhattanDistance(p1x, p1y, p2x, p2y)
        if dist <= character1.weapRange():
            character1.fight(character2, dist)
        else:
            print "invalid fight"

    def isValidMove(self, p1x, p1y, p2x, p2y, charRange):
        inrange = self.manhattanDistance(p1x, p1y, p2x, p2y) <= charRange
        validTerrain = self.board[p2x][p2y].isValidTerrain()
        isempty = self.board[p2x][p2y].getCharacter() == False
        return inrange and validTerrain

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
                if character != False and character.isAlive():
                    sys.stdout.write(character.getName() + " ")
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

    def isValidTerrain(self):
        return self.terrain == 0 or self.terrain == 2

    def getCharacter(self):
        if self.character != None:
            return self.character
        else:
            return False

    def changeCharacter(self, character):
        self.character = character

    def isFilled(self):
        return self.character == None

    def hasLord(self):
        return self.character.isLord()

    def hasEnemy(self):
        return self.character.isEnemy()

    def hasBoss(self):
        return self.character.isBoss()
    
