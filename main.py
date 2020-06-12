from character import Character
import race
import exceptions

ted = Character('Ted', 'M', 'S', race.Elf())

try:
	ted.attach_atributes(hp=16)
except exceptions.TooManyAtributes:
	print('Invalid atributes...')


print(ted.hp)