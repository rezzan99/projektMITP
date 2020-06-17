<<<<<<< Updated upstream
from character import Character
import race
import exceptions

ted = Character('Ted', 'M', 'S', race.Elf())

try:
	ted.attach_atributes(hp=16)
except exceptions.TooManyAtributes:
	print('Invalid atributes...')

=======
from character import YourCharacter, Enemy
import race
import exceptions
from os import system, name
import board
from params import MOVES_AMOUNT, DIFFUCULTY
import random
import enemies
import time


def clear():
    if name  == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

Ted = YourCharacter('Ted', 'M', 'S', race.Elf())

try:
	Ted.attach_atributes(hp=15, defense=15, strength=10, agility=5, inteligence=5)
except exceptions.TooManyAtributes:
	print('Invalid atributes...')

while(1):
	Ber = Enemy(random.choice(enemies.ENEMY_NAMES), 'F', 'M', race.Dwarf())
	try:
		Ber.attach_atributes(hp=random.randint(0,DIFFUCULTY), defense=random.randint(0,DIFFUCULTY),
							 strength=random.randint(0,DIFFUCULTY), agility=random.randint(0,DIFFUCULTY),
							 inteligence=random.randint(0,DIFFUCULTY))
	except exceptions.TooManyAtributes:
		print('Invalid atributes...')



	TURN=1
	BOARD=board.Board()

	while(TURN):
		MOVES=MOVES_AMOUNT
		BOARD.fill(Ted, Ber)
		print(
			#'{0} is on position ({1}, {2}) and has {3} HP\n'.format(Ted.name, Ted.pos_x, Ted.pos_y, Ted.hp),
			#'{0} is on position ({1}, {2}) and has {3} HP\n'.format(Ber.name, Ber.pos_x, Ber.pos_y,Ber.hp),
			'The Distance between them is ',Ted.range(Ber),'\n',
			'1. ATTACK\n'
			'2. MOVE\n'
			'3. INVENTORY\n'
			'3. CAST A SPELL\n'
			'4. RUN\n'
			'5. SEE STATS\n')


		A=input()
		if A  == '1':
			TURN=Ted.attack(Ber)
			if TURN  == 0:
				print("THE FIGHT IS OVER")
				break
			time.sleep(2)
			TURN=Ber.attack(Ted)
			if TURN  == 0:
				print("YOU DIED!")
				sys.exit(-1)
		if A  == '2':
			print("You can move ",MOVES," tiles")
			try:
				distance = int(input('Distance: '))
				direction = input('Direction: ')

				Ted.move(distance, direction)

			except Exception as exc:
				print(exc)
				sys.exit(-1)
		if A  == '5':
			print(
				'1. YOUR STATS\n'
				'2. ENEMY STATS'
			)
			B=input()
			if B  == '1':
				Ted.__str__()
			if B  == '2':
				Ber.__str__()
	#loot()
	input("poza petla")












	

>>>>>>> Stashed changes

#print(ted.hp)