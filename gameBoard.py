import sys
import util
import sets

class gameBoard:
    def __init__(self, board, characters, height, width, mapLords):
        self.height = height
        self.width = width
        self.lords = mapLords
        self.board = [[None for i in xrange(width)] for i in xrange(height)]
        self.enemyTurn = False

        for x in range(height):
            for y in range(width):
                self.board[x][y] = gameSpace(characters[x][y], board[x][y])

    #Calculate distance between two points
    def manhattanDistance(self, p1x, p1y, p2x, p2y):
        return abs(p1x - p2x) + abs(p1y - p2y)

    #Determine if a given move is valid for a given character
    def isValidMove(self, p1x, p1y, p2x, p2y, charRange, flying, mounted, isEnemy):
        #inrange = self.manhattanDistance(p1x, p1y, p2x, p2y) <= charRange
        cost = self.aStarSearch(p1x, p1y, p2x, p2y, charRange, flying, mounted, isEnemy)
        inrange = (cost != None) and (cost < charRange)
        isempty = self.board[p2x][p2y].getCharacter() == False
        if flying:
            return inrange and isempty
        else:
            validTerrain = self.board[p2x][p2y].isValidTerrain(mounted)
            isempty = self.board[p2x][p2y].getCharacter() == False
            return inrange and validTerrain and isempty


    #Determine if a given location is valid for a given character
    def isValidLocation(self, x, y, flying, mounted):
        isempty = self.board[x][y].getCharacter() == False
        if flying:
            return isempty
        else:
            validTerrain = self.board[x][y].isValidTerrain(mounted)
            isempty = self.board[x][y].getCharacter() == False
            return validTerrain and isempty


    def isValidIntermediate(self, x, y, flying, mounted, isEnemy):
        character = self.board[x][y].getCharacter()
        isempty = (character == False)

        if isempty:
            if flying:
                return True
            else:
                validTerrain = self.board[x][y].isValidTerrain(mounted)
                return validTerrain

        else:

            ispassable = (character.isEnemy() == isEnemy)

            if ispassable:

                if flying:
                    return True
                else:
                    validTerrain = self.board[x][y].isValidTerrain(mounted)
                    return validTerrain

            else:
                return False


    def isValidNaiveIntermediate(self, x, y, flying, mounted):
        if flying:
            return True
        else:
            validTerrain = self.board[x][y].isValidTerrain(mounted)
            return validTerrain


    # get valid neighboring locations a given character can move through (along with their terrain cost)
    def getSuccessors(self, x, y, flying, mounted, isEnemy):
        possibleSuccessors = [ (x, y+1), (x-1, y), (x+1, y), (x, y-1), ]
        successors = []

        for possibleSuccessor in possibleSuccessors:
            xCoor = possibleSuccessor[0]
            yCoor = possibleSuccessor[1]

            # valid map location
            if (xCoor >= 0 and xCoor < self.height) and (yCoor >= 0 and yCoor < self.width):

                # can be passed through
                if self.isValidIntermediate(xCoor, yCoor, flying, mounted, isEnemy):
                    terrain = self.getTerrain(xCoor, yCoor)
                    terrainCost = 9999
                    if flying:
                        terrainCost = 1
                        successors.append( ((xCoor, yCoor), terrainCost) )
                    else:
                        # plain
                        if (terrain == 0):
                            terrainCost = 1
                        # mountain
                        elif (terrain == 2):
                            terrainCost = 4
                        # forest
                        elif (terrain == 3):
                            if mounted:
                                terrainCost = 3
                            else:
                                terrainCost = 2
                        successors.append( ( (xCoor, yCoor), terrainCost) )
        return successors




    def getNaiveSuccessors(self, x, y, flying, mounted):
        possibleSuccessors = [ (x, y+1), (x-1, y), (x+1, y), (x, y-1), ]
        successors = []

        for possibleSuccessor in possibleSuccessors:
            xCoor = possibleSuccessor[0]
            yCoor = possibleSuccessor[1]

            # valid map location
            if (xCoor >= 0 and xCoor < self.height) and (yCoor >= 0 and yCoor < self.width):

                # can be passed through
                if self.isValidNaiveIntermediate(xCoor, yCoor, flying, mounted):
                    terrain = self.getTerrain(xCoor, yCoor)
                    terrainCost = 9999
                    if flying:
                        terrainCost = 1
                        successors.append( ((xCoor, yCoor), terrainCost) )
                    else:
                        # plain
                        if (terrain == 0):
                            terrainCost = 1
                        # mountain
                        elif (terrain == 2):
                            terrainCost = 4
                        # forest
                        elif (terrain == 3):
                            if mounted:
                                terrainCost = 3
                            else:
                                terrainCost = 2
                        successors.append( ( (xCoor, yCoor), terrainCost) )
        return successors

    def aStarSearch(self, startX, startY, goalX, goalY, charRange, flying, mounted, isEnemy):

        if (startX == goalX) and (startY == goalY):
            return 0

        else:
            #reject if invalid goal
            if not(self.isValidLocation(goalX, goalY, flying, mounted)):
                return float("inf")
            else:
                startCoordinates = (startX, startY)
                goalCoordinates = (goalX, goalY)

                queue = util.PriorityQueue()
                start = (startCoordinates, None, 0)
                queue.push(start, 0)
                closed = sets.Set()

                while not(queue.isEmpty()):
                    top = queue.pop()
                    if (top[0][0] == goalX) and (top[0][1] == goalY):
                        #we've reached the end, return cost it took to get here
                        return top[2] 
                    elif not(top[0] in closed):
                        #expand top
                        successors = self.getSuccessors(top[0][0], top[0][1], flying, mounted, isEnemy)

                        for x in range(len(successors)):
                            cost = top[2] + successors[x][1]
                            if cost <= charRange:
                                queue.push( (successors[x][0], top, cost),
                                            cost + self.manhattanDistance(successors[x][0][0], successors[x][0][1], goalX, goalY) )             
                        closed.add(top[0])
                        continue
                    else:
                        continue
                return float("inf")


    def uninhibitedAStarSearch(self, startX, startY, goalX, goalY, charRange, flying, mounted):

        if (startX == goalX) and (startY == goalY):
            return 0

        else:

            startCoordinates = (startX, startY)
            goalCoordinates = (goalX, goalY)

            queue = util.PriorityQueue()
            start = (startCoordinates, None, 0)
            queue.push(start, 0)
            closed = sets.Set()

            while not(queue.isEmpty()):
                top = queue.pop()
                if (top[0][0] == goalX) and (top[0][1] == goalY):
                    #we've reached the end, return cost it took to get here
                    return top[2] 
                elif not(top[0] in closed):
                    #expand top
                    successors = self.getNaiveSuccessors(top[0][0], top[0][1], flying, mounted)

                    for x in range(len(successors)):
                        cost = top[2] + successors[x][1]
                        queue.push( (successors[x][0], top, cost),
                                    cost + self.manhattanDistance(successors[x][0][0], successors[x][0][1], goalX, goalY) )             
                    closed.add(top[0])
                    continue
                else:
                    continue
            return float("inf")


    def isInRange(self, unit, unitPos, targetPos):
        flying = unit.isFlying()
        mounted = unit.isMounted()
        charRange = unit.getRange()
        isEnemy = unit.isEnemy()

        x = targetPos[0]
        y = targetPos[1]

        # Ranged attack only
        if unit.getWeaponType() == "bow":
            possibleNeighbors = [ (x-2, y), (x-1, y+1), (x, y+2), (x+1, y+1), (x+2, y), (x+1, y-1), (x, y-2), (x-1, y-1) ]
            neighbors = []
            for possibleNeighbor in possibleNeighbors:
                xCoor = possibleNeighbor[0]
                yCoor = possibleNeighbor[1]

                if ((xCoor >= 0 and xCoor < self.height) and (yCoor >= 0 and yCoor < self.width)):
                    if self.isValidLocation(xCoor, yCoor, flying, mounted):
                        neighbors.append(possibleNeighbor)

            distances = []
            for neighbor in neighbors:
                distances.append( self.aStarSearch(unitPos[0], unitPos[1], neighbor[0], neighbor[1], charRange, flying, mounted, isEnemy ) )

            for distance in distances:

                if (distance != None) and (distance <= charRange):
                    return True

            return False

        # CQC only
        else:
            possibleNeighbors = [ (x, y+1), (x-1, y), (x+1, y), (x, y-1) ]
            neighbors = []
            for possibleNeighbor in possibleNeighbors:
                xCoor = possibleNeighbor[0]
                yCoor = possibleNeighbor[1]

                if ((xCoor >= 0 and xCoor < self.height) and (yCoor >= 0 and yCoor < self.width)):
                    if self.isValidLocation(xCoor, yCoor, flying, mounted):
                        neighbors.append(possibleNeighbor)

            distances = []
            for neighbor in neighbors:
                distances.append( self.aStarSearch(unitPos[0], unitPos[1], neighbor[0], neighbor[1], charRange, flying, mounted, isEnemy ) )

            for distance in distances:

                if (distance != None) and (distance <= charRange):
                    return True

            return False

    def getTargets(self, character, position):
        characterAlignment = character.isEnemy()

        x = position[0]
        y = position[1]

        targets = [None]

        # ranged
        if character.getWeaponType() == "bow":
            neighbors = [ (x-2, y), (x-1, y+1), (x, y+2), (x+1, y+1), (x+2, y), (x+1, y-1), (x, y-2), (x-1, y-1) ]

            for neighbor in neighbors:
                if (neighbor[0] >= 0 and neighbor[0] < self.height) and (neighbor[1] >= 0 and neighbor[1] < self.width):
                    char = self.board[neighbor[0]][neighbor[1]].getCharacter()
                    if char != False:
                        if char.isEnemy() != characterAlignment:
                            targets.append(char)

            return targets

        #CQC
        else:
            neighbors = [ (x, y+1), (x-1, y), (x+1, y), (x, y-1) ]

            for neighbor in neighbors:
                if (neighbor[0] >= 0 and neighbor[0] < self.height) and (neighbor[1] >= 0 and neighbor[1] < self.width):
                    char = self.board[neighbor[0]][neighbor[1]].getCharacter()
                    if char != False:
                        if char.isEnemy() != characterAlignment:
                            targets.append(char)

            return targets

    #Perform a move of a character
    def moveCharacter(self, inputChar, newx, newy):
        for x in range(self.height):
            for y in range(self.width):
                character = self.board[x][y].getCharacter()
                if character != False and inputChar == character:
                    if character.moveable(): 
                        if (newx == x) and (newy ==y):
                            return
                        if self.isValidMove(x, y, newx, newy, character.getRange(),
                                            character.isFlying(), character.isMounted(), character.isEnemy()):
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

    #Engage one character in friendly conflict with another
    def fight(self, character1, character2, mock = False, mockPos = False):
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

        if mockPos != False:
            p1x, p1y = mockPos[0], mockPos[1]

        dist = self.manhattanDistance(p1x, p1y, p2x, p2y)
        attackTerrain = self.board[p1x][p1y].getTerrain()
        defendTerrain = self.board[p2x][p2y].getTerrain()
        result = 0
        if character1.canAttack():
            if dist <= character1.weapRange():
                result = character1.fight(character2, dist, attackTerrain, defendTerrain, mock)
                if not mock:
                    character1.attackUsed()
                    if character1.status == 0:
                        self.board[p1x][p1y].removeCharacter()
                    elif character2.status == 0:
                        self.board[p2x][p2y].removeCharacter()
            else:
                print "invalid fight\n"
                
        else:
            print "already attacked\n"

        if result != None:
            return result

    #Pull terrain of a square
    def getTerrain(self, x, y):
        return self.board[x][y].getTerrain()

    def getTerrainDefenseBonus(self, x, y):
        tbonus = 0
        terrain  = self.getTerrain(x, y)
        if terrain == 2:
            tbonus = 1
        elif terrain == 3:
            tbonus = 2

        return tbonus
            
    def getTerrainAvoidBonus(self, x, y):
        tbonus = 0
        terrain  = self.getTerrain(x, y)
        if terrain == 2:
            tbonus = 20
        elif terrain == 3:
            tbonus = 30

        return tbonus

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
        for x in range(self.height):
            for y in range(self.width):
                if self.board[x][y].hasLord():
                    lords += 1

        if lords == self.lords:
            return False
        else:
            return True

    #Check board for win condition
    def isWin(self):
        enemies = 0
        for x in range(self.height):
            for y in range(self.width):
                if self.board[x][y].hasBoss():
                    enemies += 1

        if enemies == 0:
            return True
        else:
            return False

    #Display purposes - outputs grid of terrain/characters
    def Display(self):
        sys.stdout.write("-------")
        for y in range(self.width):
            if y < 10:
                sys.stdout.write(" " + str(y) +  " -----")
            else:
                sys.stdout.write(" " + str(y) +  " ----")
        sys.stdout.write("\n")
        for x in xrange(self.height):
            sys.stdout.write(str(x) + "\t")
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
            if character[0].isEnemy() == self.enemyTurn:
                character[0].resetActions()
        self.enemyTurn = 1 - self.enemyTurn

class gameSpace:
    def __init__(self, character, terrain):
        self.character = character
        self.terrain = terrain

    def getTerrainDisplay(self):
        if self.terrain == 0: 
            return "_"
        elif self.terrain == 1:
            return "X"
        elif self.terrain == 2:
            return "^|^"
        elif self.terrain == 3:
            return "/|"
        else:
            return "?"

    def getTerrain(self):
        return self.terrain

    def isValidTerrain(self, mounted):
        if mounted:
            return ( not(self.terrain == 1) ) and ( not(self.terrain == 2) )

        else:
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
        if self.character != None:
            return self.character.isLord()
        else:
            return False

    def hasEnemy(self):
        return self.character.isEnemy()

    def hasBoss(self):
        if self.character != None:
            return self.character.isBoss()
        else:
            return False
    
    def removeCharacter(self):
        self.character = None
