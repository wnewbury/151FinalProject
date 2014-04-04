ALIVE = 1
DEAD = 0

class character:
    def __init__(self, name, charClass, primWeapon, secWeapon, enemy, stats, health):
        self.name = name
        self.charClass = charClass
        self.primWeapon = primWeapon
        self.secWeapon = secWeapon
        self.enemy = enemy
        self.stats = stats
        self.maxhealth = health
        self.curhealth = health
        self.status = ALIVE

    def isEnemy(self):
        return self.enemy

    def isBoss(self):
        return self.name == "Migal"

    def isLord(self):
        return self.charClass == "Lord"

    def getName(self):
        return self.name

    def getRange(self):
        return self.stats.getRange()

    def isAlive(self):
        return self.status

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
