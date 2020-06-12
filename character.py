from exceptions import TooManyAtributes
from race import Human, Elf

AVAILABLE_POINTS = 15


class Character():

	def __init__(self, name, sex, physique, race):
		self.name = name
		self.sex = sex
		self.physique = physique
		self.race = race

		self.hp = self.race.HP 
		self.defense = self.race.DEFENSE 
		self.strength = self.race.STRENGTH 
		self.agility = self.race.AGILITY 
		self.inteligence = self.race.INTELIGENCE 



	def attach_atributes(self, hp=0, defense=0, strength=0, agility=0, inteligence=0):
		if (hp + defense + strength + agility + inteligence) > AVAILABLE_POINTS:
			raise TooManyAtributes

		self.hp += hp
		self.defense += defense
		self.strength += strength
		self.agility += agility
		self.inteligence += inteligence

	



