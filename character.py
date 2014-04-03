class character:
    def __init__(self, name, charClass, primWeapon, secWeapon, enemy, stats, health):
        self.name = name
        self.charClass = charClass
        self.primWeapon = primWeapon
        self.secWeapon = secWeapon
        self.enemy = enemy
        self.stats = stats
        self.health = health

    def isEnemy():
        return self.enemy

    def isBoss():
        return self.name == "Migal"

    def isLord():
        return self.charClass == "Lord"


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

class weapon:
    def __init__(self, name, weaponType, might, hit, crit, rng, weight):
        self.name = name
        self.type = weaponType
        self.might = might
        self.hit = hit
        self.crit = crit
        self.rng = rng
        self.weight
