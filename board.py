from params import BOARD_WIDTH, BOARD_HEIGHT


class Cell():

	def __init__(self, x, y):
		self.x = x
		self.y = y


class Board():

	def __init__(self):
		self.width = BOARD_WIDTH
		self.height = BOARD_HEIGHT
		self.cells = []

		for x in range(0, self.width):
			for y in range(0, self.height):
				self.cells.append(Cell(x, y))

