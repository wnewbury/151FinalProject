ALIVE = 1
DEAD = 0

from random import randrange

class character:
    def __init__(self, name, charClass, primWeapon, secWeapon, enemy, boss, stats, health):
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

    def isEnemy(self):
        return self.enemy

    def weapRange(self):
        #FIXME MAKE IT ALWAYS HAVE A WEAPON, EVEN IF NONE
        if self.secWeapon != None:
            return max(self.primWeapon.getRange(), self.secWeapon.getRange())
        else:
            return self.primWeapon.getRange()

    def isBoss():
        return self.boss

    def isLord(self):
        return self.charClass == "Lord"

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.stats.getSpeed()

    def getWeaponType(self):
        return self.primWeapon.getType()

    def getClass(self):
        return self.getClass

    def getRange(self):
        return self.stats.getRange()

    def isAlive(self):
        return self.status

    def attackSpeed(self):
        return self.stats.getCon() - self.primWeapon.getWeight()

    def hitRate(self):
        return self.primWeapon.getHit() + (self.stats.getSkill() * 2) + (self.stats.getLuck() / 2)

    def evade(self):
        #Need terrain at some point
        return (self.attackSpeed() * 2) + self.stats.getLuck()

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

    def defense(self):
        #need terrain
        return self.stats.getDefense()

    def damage(self, enemyClass, enemyWeap, enemyDefense):
        return self.attackPower(enemyClass, enemyWeap) - enemyDefense

    def isValidAttack(self, distance):
        if self.getWeaponType() == "bow" and distance == 1:
            return False
        elif self.weapRange() < distance:
            return False
        else:
            return True

    def performAttack(self, accuracy, damage):
        hit = randrange(1, 100)
        if hit <= (accuracy * 100):
            self.curhealth -= damage

            if self.curhealth <= 0:
                self.status = DEAD

            return damage
        else:
            print "miss"

            return 0


        

    def fight(self, enemy, distance):
        print self.name + " attacking " + enemy.getName() 

        enemyWeap = enemy.getWeaponType()
        enemyClass = enemy.getClass()
        enemyDefense = enemy.defense()
        enemyEvade = enemy.evade()

        accuracy = self.accuracy(enemyEvade, enemyWeap)
        damage = self.damage(enemyClass, enemyWeap, enemyDefense)

        enemyAccuracy = enemy.accuracy(self.evade(), self.getWeaponType())
        enemyDamage = enemy.damage(self.getClass(), self.getWeaponType(), 
                                   self.defense())


        damageInf = 0
        damageTak = 0

        damageInf += enemy.performAttack(accuracy, damage)

        if enemy.isValidAttack(distance) and enemy.isAlive():
            damageTak += self.performAttack(enemyAccuracy, enemyDamage)

        if self.attackSpeed() >= (enemy.attackSpeed() + 4):
            damageInf += enemy.performAttack(accuracy, damage)

        if enemy.attackSpeed() >= (self.attackSpeed() + 4):
            damageTak += enemy.performAttack(accuracy, damage)

        print "Results: damage inflicted = " + str(damageInf) + " damage taken = " + str(damageTak) 
        print "Attacker health = " + str(self.curhealth) + ", Defender health =  " + str(enemy.curhealth) + "\n"

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
