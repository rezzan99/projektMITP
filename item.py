
class Item():
	pass

class Equipment(Item)
    def __init__(self,):


        ARMOR= {
            'head': 0,
            'chest': 1,
            'legs': 2,
            'feet': 3,
            'weapon': 4
        }




class Weapon(Item):
	pass

class Armor(Item):
	pass
class Head(Armor):
    pass
class Chest(Armor):
    pass
class Legs(Armor):
    pass
class Feet(Armor):
    pass

#WEAPONS & SHIELDS
class ShortSword(Weapon):
    STRENGTH = 3
    RANGE = 2
class LongSword(Weapon):
    STRENGTH = 5
    RANGE = 3
class ShortBow(Weapon):
    AGILITY = 3
    RANGE = 8
class LongBow(Weapon):
    AGILITY = 4
    RANGE = 9
class ShortWand(Weapon):
    INTELLIGENCE = 4
class LongWand(Weapon):
    INTELLIGENCE = 6
class SmallShield(Weapon):
    DEFENCE = 5
class BigShield(Weapon):
    DEFENCE = 7
    
#ARMOR & CLOTHING   
#HEAD
class ArcherCowl(Head):
    AGILITY = 2
class MageHat(Head):
    INTELLIGENCE = 3
class WarriorHelm(Head):
    STRENGTH = 3
#CHEST
class ArcherVest(Chest):
    AGILITY = 4
    DEFENCE = 2
class MageRobes(Chest):
    INTELLIGENCE = 5
    DEFENCE = 1
class WarriorBreastplate(Chest)
    STRENGTH = 5
    DEFENCE = 4
#LEGS
class ArcherLeggins(Legs)
    AGILITY = 3
    DEFENCE = 1
class MageUnderwear(Legs):
    INTELLIGENCE = 4
    DEFENCE = 1
class WarriorLegplates(Legs):
    STRENGTH = 3
    DEFENCE = 3
#FEET
class ArcherSlippers(Feet):
    AGILITY = 4
    DEFENCE = 1
class MageSandals(Feet):
    INTELLIGENCE = 2
    AGILITY = 2
    DEFENCE = 1
class WarriorGraves(Feet):
    STRENGTH = 2
    DEFENCE = 5
    AGILITY = 1
