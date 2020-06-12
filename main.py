from character import YourCharacter
import race
import exceptions
import params
import sys

ted = YourCharacter('Ted', 'M', 'S', race.Elf())

try:
	ted.attach_atributes(hp=15)
except exceptions.TooManyAtributes:
	print('Invalid atributes...')

while True:
	try:
		distance = int(input('Distance: '))
		direction = input('Direction: ')

		ted.move(distance, direction)
		print('{0} on position ({1}, {2})'.format(ted.name, ted.pos_x, ted.pos_y))
	except Exception as exc:
		print(exc)
		sys.exit(-1)
	


print(ted.hp)