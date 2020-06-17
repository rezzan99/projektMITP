from params import BOARD_WIDTH, BOARD_HEIGHT

class Cell():

	def __init__(self, x, y,fill=0):
		self.x = x
		self.y = y
		self.fill=''

class Board():
	def __init__(self):
		self.heigth = BOARD_HEIGHT
		self.width = BOARD_WIDTH
		self.cells = []
		for y in range(0, self.heigth):
			for x in range(0, self.width):
				self.cells.append(Cell(x, y))
	def fill (self,Ted,Ber):
		i=0
		for y in range(0, self.heigth):
			for x in range(0, self.width):
				if x==Ted.pos_x and y== Ted.pos_y:
					self.cells[i].fill=' H '
					print(self.cells[i].fill,end='')
					i+=1
					x+=1
					continue
				if x==Ber.pos_x and y== Ber.pos_y:
					self.cells[i].fill = ' E '
					print(self.cells[i].fill, end='')
					i+=1
					x+=1
					continue
				#print(self.cells[i])
				if self.cells[i].x%12==0 or self.cells[i].x%12==11:
					self.cells[i].fill = '|'
				else:
					self.cells[i].fill = ' _ '
				print(self.cells[i].fill,end='')
				i += 1
			print()


		# for i in range(0,119):
		# 	if self.cells[i] % 12 == 1 or self.cells[i] % 12 == 11:
		# 		self.cells[i] = '|'
		# 	else:
		# 		self.cells[i] = '_'
		# 	print(self.cells[i])
		# 	i += 1