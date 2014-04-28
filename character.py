ALIVE = 1
DEAD = 0

from random import randrange

class character:
    def __init__(self, name, charClass, primWeapon, secWeapon, enemy, boss, stats, health, oweights, dweights, side):
        self.name = name
        self.charClass = charClass
        self.primWeapon = primWeapon
        self.secWeapon = secWeapon
        self.enemy = enemy
        self.boss = boss
        self.stats = stats
        self.maxhealth = health
        self.curhealth = health
        self.status = ALIVE
        self.moveAction =  True
        self.attackAction = True
        self.oweights = oweights
        self.dweights = dweights

    def isEnemy(self):
        return self.enemy

    def weapRange(self):
        return self.primWeapon.getRange()

    def isBoss(self):
        return self.boss

    def isLord(self):
        return self.charClass == "Lord"

    def isFlying(self):
        return self.charClass == "PegKnight"

    def isMounted(self):
        return self.charClass == "Cavalier"

    def getName(self):
        return self.name

    def getSide(self):
        return self.side

    def getOffensiveWeights(self):
        return self.oweights

    def getDefensiveWeights(self):
        return self.dweights

    def getCurrentHealth(self):
        return self.curhealth

    def getMaxHealth(self):
        return self.maxhealth

    def getSpeed(self):
        return self.stats.getSpeed()

    def getWeaponType(self):
        return self.primWeapon.getType()

    def getSecondaryWeaponType(self):
        if self.secWeapon != None:
            return self.secWeapon.getType()

    def getClass(self):
        return self.getClass

    def getRange(self):
        return self.stats.getRange()

    def isAlive(self):
        return self.status

    #Stuff necessary for limiting actions per turn
    def moveUsed(self):
        self.moveAction = False

    def attackUsed(self):
        self.attackAction = False
    
    def resetActions(self):
        self.moveAction = True
        self.attackAction = True

    def moveable(self):
        return self.moveAction

    def canAttack(self):
        return self.attackAction

    # Thus starts the Battle stats
    def attackSpeed(self):
        return self.stats.getCon() - self.primWeapon.getWeight()

    def hitRate(self):
        return self.primWeapon.getHit() + (self.stats.getSkill() * 2) + (self.stats.getLuck() / 2)

    def switchWeapons(self):
        temp = self.secWeapon
        self.secWeapon = self.primWeapon
        self.primWeapon = temp

    def evade(self, terrain):
        tbonus = 0
        if terrain == 2:
            tbonus = 20
        elif terrain == 3:
            tbonus = 30
        return (self.attackSpeed() * 2) + self.stats.getLuck() + tbonus

    def accuracy(self, enemyEvade, enemyWeap):
        bonus = self.weaponTriangle(enemyWeap)
        return self.hitRate() - enemyEvade + (bonus * .15)

    def weaponTriangle(self, enemyWeap):
        bonus = 0
        if self.getWeaponType() == "axe" and enemyWeap == "lance":
            bonus = 1
        elif self.getWeaponType() == "axe" and enemyWeap == "sword":
            bonus = -1
        elif self.getWeaponType() == "lance" and enemyWeap == "sword":
            bonus = 1
        elif self.getWeaponType() == "lance" and enemyWeap == "axe":
            bonus = -1
        elif self.getWeaponType() == "sword" and enemyWeap == "axe":
            bonus = 1
        elif self.getWeaponType() == "sword" and enemyWeap == "lance":
            bonus = -1

        return bonus

    def attackPower(self, enemyClass, enemyWeap):
        if self.getWeaponType() == "bow" and enemyClass == "pegKnight":
            modifier = 3
        else:
            modifier = 1
        bonus = self.weaponTriangle(enemyWeap)
        
        return ((self.stats.getStrength() + bonus + self.primWeapon.getMight()) * modifier)

    def defense(self, terrain):
        tbonus = 0
        if terrain == 2:
            tbonus = 1
        elif terrain == 3:
            tbonus = 2

        return self.stats.getDefense() + tbonus

    def damage(self, enemyClass, enemyWeap, enemyDefense):
        return self.attackPower(enemyClass, enemyWeap) - enemyDefense

    def critRate(self):
        return self.primWeapon.getCrit() + (self.stats.getSkill() / 2)

    def critEvade(self):
        return self.stats.getLuck()

    def critChance(self, enemyEvade):
        return self.critRate() - enemyEvade

    def isValidAttack(self, distance):
        #Check Ranges
        if self.getWeaponType() == "bow" and distance == 1:
            return False
        elif self.weapRange() < distance:
            return False
        else:
            return True

    #Resolve Attack performed on you
    def performAttack(self, accuracy, damage, critChance, mock = False):
        #Random generate a hit number, check vs crit and hit rates
        hit = randrange(1, 100)
        if mock:
            eDamage = (3*damage*critChance) + (damage*(accuracy-critChance))
            return eDamage
        elif hit <= accuracy:
            if hit <= critChance:

                self.curhealth -= damage * 3
                if self.curhealth <= 0:
                    self.status = DEAD
                return damage


            self.curhealth -= damage
            if self.curhealth <= 0:
                self.status = DEAD
            return damage
        else:
            print self.getName()
            print "miss"
            return 0      

    def fight(self, enemy, distance, aTerrain, dTerrain, mock = False):

        #Display purposes
        if not mock:
            print self.name + " attacking " + enemy.getName() 

        #Pull needed stats
        enemyWeap = enemy.getWeaponType()
        enemyClass = enemy.getClass()
        enemyDefense = enemy.defense(dTerrain)
        enemyEvade = enemy.evade(dTerrain)
        enemyCritEvade = enemy.critEvade()

        #Battle stats on attacker side
        accuracy = self.accuracy(enemyEvade, enemyWeap)
        damage = self.damage(enemyClass, enemyWeap, enemyDefense)
        critChance = self.critChance(enemyCritEvade)

        #Battle stats on defender side
        enemyAccuracy = enemy.accuracy(self.evade(aTerrain), self.getWeaponType())
        enemyDamage = enemy.damage(self.getClass(), self.getWeaponType(), 
                                   self.defense(aTerrain))
        enemyCritChance = enemy.critChance(self.critEvade())

        #Counters for display purposes
        damageInf = 0
        damageTak = 0

        #First Attack, Enemy Counter-attack, then checks for speed doubles
        damageInf += enemy.performAttack(accuracy, damage, critChance, mock)

        if enemy.isValidAttack(distance) and enemy.isAlive():
            damageTak += self.performAttack(enemyAccuracy, enemyDamage, 
                                            enemyCritChance, mock)

        if self.attackSpeed() >= (enemy.attackSpeed() + 4):
            damageInf += enemy.performAttack(accuracy, damage, critChance, mock)

        if enemy.attackSpeed() >= (self.attackSpeed() + 4):
            damageTak += self.performAttack(enemyAccuracy, enemyDamage, 
                                            enemyCritChance, mock)
        
        if mock:
            return (damageInf, damageTak)
        else:
            #Output Results
            print "Results: damage inflicted = " + str(damageInf) + " damage taken = " + str(damageTak) 
            print "Attacker health = " + str(self.curhealth) + ", Defender health =  " + str(enemy.curhealth) + "\n"
            return None

    #Overload equality operator
    def __eq__(self, other):
        if isinstance(other, character):
            return self.name == other.getName()
        return NotImplemented

class stats:
    def __init__(self, hp, strength, skill, spd, lck, defense, res, con, move):
        self.hp = hp
        self.strength = strength
        self.skill = skill
        self.spd = spd
        self.lck = lck
        self.defense = defense
        self.res = res
        self.con = con
        self.move = move

    def getSpeed(self):
        return self.speed

    def getDefense(self):
        return self.defense

    def getStrength(self):
        return self.strength

    def getSkill(self):
        return self.skill

    def getLuck(self):
        return self.lck

    def getCon(self):
        return self.con

    def getRange(self):
        return self.move


class weapon:
    def __init__(self, name, weaponType, might, hit, crit, rng, weight):
        self.name = name
        self.type = weaponType
        self.might = might
        self.hit = hit
        self.crit = crit
        self.rng = rng
        self.weight = weight

    def getCrit(self):
        return self.crit

    def getMight(self):
        return self.might

    def getType(self):
        return self.type

    def getHit(self):
        return self.hit

    def getWeight(self):
        return self.weight

    def getRange(self):
        return self.rng
