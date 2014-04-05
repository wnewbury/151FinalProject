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

    #Calculate distance between two points
    def manhattanDistance(self, p1x, p1y, p2x, p2y):
        return abs(p1x - p2x) + abs(p1y - p2y)

    #Determine if a given move is valid for a given character
    def isValidMove(self, p1x, p1y, p2x, p2y, charRange, flying):
        inrange = self.manhattanDistance(p1x, p1y, p2x, p2y) <= charRange
        if flying:
            return inrange
        else:
            validTerrain = self.board[p2x][p2y].isValidTerrain()
            isempty = self.board[p2x][p2y].getCharacter() == False
            return inrange and validTerrain

    #Perform a move of a character
    def moveCharacter(self, inputChar, newx, newy):
        for x in range(self.height):
            for y in range(self.width):
                character = self.board[x][y].getCharacter()
                if character != False and inputChar == character:
                    if character.moveable(): 
                        if self.isValidMove(x, y, newx, newy, character.getRange(),
                                            character.isFlying()):
                            self.board[x][y].changeCharacter(None)
                            self.board[newx][newy].changeCharacter(character)
                            character.moveUsed()
                            return
                        else:
                            print "invalid move\n"
                            return
                    else:
                        print "move already used\n"
                        return
        print "No such character to move\n"

    #HEURISTIC
    def obtainBestMove(self, character, position):
        #Insert heuristic!!! (Call out to another class, probably?)
        print "meh"

    #Engage one character in friendly conflict with another
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
        attackTerrain = self.board[p1x][p1y].getTerrain()
        defendTerrain = self.board[p2x][p2y].getTerrain()
        if character1.canAttack():
            if dist <= character1.weapRange():
                character1.fight(character2, dist, attackTerrain, defendTerrain)
                character1.attackUsed()
            else:
                print "invalid fight\n"
        else:
            print "already attacked\n"

    #Pull terrain of a square
    def getTerrain(self, x, y):
        return self.board[x][y].getTerrain()

    #Pull all the characters on the map
    def getCharacters(self):
        characters = list()
        for x in range(self.height):
            for y in range(self.width):
                character = self.board[x][y].getCharacter()
                if character != False:
                    characters.append((character, (x,y)))

        return characters
             
    #Check board for lose condition   
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

    #Check board for win condition
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

    #Display purposes - outputs grid of terrain/characters
    def Display(self):
        print "--------"*15
        for x in xrange(self.height):
            for i in self.board[x]:
                character = i.getCharacter()
                if character != False and character.isAlive():
                    sys.stdout.write(character.getName() + "\t")
                else:
                    sys.stdout.write(str(i.getTerrainDisplay()) + "\t")
                sys.stdout.flush()
            print "\n"
        print "--------"*15 + "\n"

    #End a turn - resets the move and attack counters for the characters
    def endTurn(self):
        #When we have actual two players, give the characters a side, then
        #check if its the appropriate side before reseting the actions
        print "ENDING TURN\n"
        for character in self.getCharacters():
            character[0].resetActions()

class gameSpace:
    def __init__(self, character, terrain):
        self.character = character
        self.terrain = terrain

    def getTerrainDisplay(self):
        if self.terrain == 0: 
            return "_"
        elif self.terrain == 2:
            return "^"
        elif self.terrain == 3:
            return "/|"
        elif self.terrain == 1:
            return "X"
        else:
            return "?"

    def getTerrain(self):
        return self.terrain

    def isValidTerrain(self):
        return not (self.terrain == 1)

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
    
