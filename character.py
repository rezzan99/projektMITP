from exceptions import TooManyAtributes
from race import Human, Elf
<<<<<<< Updated upstream
=======
from params import AVAILABLE_POINTS, AVAILABLE_ITEMS_AMOUNT, BOARD_HEIGHT, BOARD_WIDTH
from params import N, NE, E, SE, S, SW, W, NW
from math import sqrt

import random

>>>>>>> Stashed changes

AVAILABLE_POINTS = 15


class Character():

	def __init__(self, name, sex, physique, race):
		self.name = name
		self.sex = sex
		self.physique = physique
		self.race = race
<<<<<<< Updated upstream
		self.exuipment = []
=======

		self.equipment = []
		self.bag = []
		self.items_amount = 0
>>>>>>> Stashed changes

		self.hp = self.race.HP 
		self.defense = self.race.DEFENSE 
		self.strength = self.race.STRENGTH 
		self.agility = self.race.AGILITY 
		self.inteligence = self.race.INTELIGENCE 


	def __str__(self):
		print('name: ',self.name,'\nsex: ',self.sex,'\nphysique: ',self.physique,'\nrace: ',type(self.race).__name__,\
			'\nHP: ',self.hp,'\ndefense: ',self.defense,'\nstrength: ',self.strength,'\nagility: ',self.agility,'\ninteligence: ',self.inteligence,'\n')
	def attach_atributes(self, hp=0, defense=0, strength=0, agility=0, inteligence=0):
		if (hp + defense + strength + agility + inteligence) > AVAILABLE_POINTS:
			raise TooManyAtributes

		self.hp += hp
		self.defense += defense
		self.strength += strength
		self.agility += agility
		self.inteligence += inteligence

<<<<<<< Updated upstream
=======

	def add_item(self, item):
		if(self.items_amount >= AVAILABLE_ITEMS_AMOUNT):
			raise TooManyItems

		self.bag.append(item)
		self.items_amount += 1




	'''def equip_item(self, item):
		self.equipment.append(item)
		self.items_amount += 1'''


	def move(self, amount, direction):
		start_pos_x = self.pos_x
		start_pos_y = self.pos_y
		
		if direction in (N, E, S, W):
			if direction == N:
				self.pos_y += amount
			if direction == E:
				self.pos_x += amount 
			if direction == S:
				self.pos_y -= amount 
			if direction == W:
				self.pos_x -= amount
		elif direction in (NE, SE, SW, NW):
			distance = int(sqrt(amount))
			if direction == NE:
				self.pos_y += distance
				self.pos_x += distance
			if direction == SE:
				self.pos_x += distance 
				self.pos_y -= distance
			if direction == SW:
				self.pos_x -= distance 
				self.pos_y -= distance
			if direction == NW:
				self.pos_x -= distance
				self.pos_y += distance
		else: 
			raise UnknownMoveDirection
			
		if self.pos_x >= BOARD_WIDTH or self.pos_x < 0 or self.pos_y >= BOARD_HEIGHT or self.pos_y < 0:
			self.pos_x = start_pos_x
			self.pos_y = start_pos_y
			raise PositionOutOfBounds("Out of bounds")


	def attack (self, target):
		ATK=self.strength
		if(self.range(target)<=4):
			print(self.name," attacks ", target.name, " for ", ATK,".\n")
			FIGHT=target.defend(ATK)
			return FIGHT
		else:
			print(self.name,' is  too far away')
			return 1
	def defend (self, ATK):
		FIGHT = 1
		DEF=abs(ATK-self.defense)
		self.hp-=ATK-DEF
		print(self.name," Defends ", DEF, " from ", ATK, "points of demage and has ", self.hp, " HP left.\n")
		if self.hp<=0:
			print(self.name, "Dies ;)")
			FIGHT=0
		return FIGHT
	def range(self, target):
		range=round(sqrt((target.pos_x-self.pos_x)**2+(target.pos_y-self.pos_y)**2))
		#range+=self.equipment.weapon.range
		return range
class YourCharacter(Character):

	def __init__(self, name, sex, physique, race):
		super().__init__(name, sex, physique, race)
		self.pos_x = 2
		self.pos_y = 1

class Enemy(Character):
	def __init__(self, name, sex, physique, race):
		super().__init__( name, sex, physique, race)
		self.pos_x = random.randint(1, BOARD_WIDTH-1)
		self.pos_y = random.randint(0, BOARD_HEIGHT)




>>>>>>> Stashed changes
	



