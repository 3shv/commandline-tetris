## Program by Rajesh Veeranki, B.Tech, IIT Bombay CSE

from random import choice

class Tetramino:
	shape = [
			   [' ', ' ', ' ', ' '], 
			   [' ', ' ', ' ', ' '], 
			   [' ', ' ', ' ', ' '], 
			   [' ', ' ', ' ', ' ']
			]
	pos_x = 0
	pos_y = 0

	def __init__(self, shape, pos_x, pos_y):
		self.shape = shape
		self.pos_x = pos_x
		self.pos_y = pos_y

	def is_within_bounds(self, board):
		piece_start_x = self.pos_x
		piece_start_y = self.pos_y
		piece_end_x = self.pos_x + len(self.shape)
		piece_end_y = self.pos_y + len(self.shape)

		for i in range(piece_start_x, piece_end_x):
			for j in range(piece_start_y, piece_end_y):
				if self.shape[i-piece_start_x][j-piece_start_y] == '*' and board[i][j] == '*':
					return False
		return True

	def has_moves(self, board):
		piece_start_x = self.pos_x
		piece_start_y = self.pos_y
		piece_end_x = self.pos_x + len(self.shape)
		piece_end_y = self.pos_y + len(self.shape)

		for i in range(piece_start_x, piece_end_x):
			for j in range(piece_start_y, piece_end_y):
				if board[i+1][j] == '*' and self.shape[i - piece_start_x][j - piece_start_y] == '*':
					print piece_end_x, piece_start_y
					return False
		return True

	def move_left(self):
		self.pos_x += 1
		self.pos_y -= 1

	def move_right(self):
		self.pos_x += 1
		self.pos_y += 1

	def rotate_clockwise(self):
		size = len(self.shape)
		result = [[' ' for i in range(size)] for j in range(size)]

		for i in range(size):
			for j in range(size):
				result[j][size-i-1] = self.shape[i][j]
		self.shape = result
		self.pos_x += 1

	def rotate_anticlockwise(self):
		size = len(self.shape)
		result = [[' ' for i in range(size)] for j in range(size)]

		for i in range(size):
			for j in range(size):
				result[size-j-1][i] = self.shape[i][j]
		self.shape = result
		self.pos_x += 1

	def draw(self):
		for row in self.shape:
			for col in row:
				print col,
			print '\n'

	def copy(self, board):
		piece_start_x = self.pos_x
		piece_start_y = self.pos_y
		piece_end_x = self.pos_x + len(self.shape)
		piece_end_y = self.pos_y + len(self.shape)

		for i in range(piece_start_x, piece_end_x):
			for j in range(piece_start_y, piece_end_y):
				if self.shape[i - piece_start_x][j - piece_start_y] == '*':
					board[i][j] = '*'


class Game:
	SHAPES = (
		 	[ 
			   [' ', ' ', ' ', ' '], 
			   ['*', '*', '*', '*'], 
			   [' ', ' ', ' ', ' '], 
			   [' ', ' ', ' ', ' ']
			],
			[ 
			   [' ', '*', ' '], 
			   [' ', '*', ' '], 
			   [' ', '*', '*'], 
			],
			[ 
			   [' ', '*', ' '], 
			   [' ', '*', ' '], 
			   ['*', '*', ' '], 
			],
			[ 
			   ['*', '*',], 
			   ['*', '*',], 
			],
		)

	BOARD = [[' ' for i in range(22)] for j in range(21)]

	for i in range(21):
		BOARD[i][0] = '*'
		BOARD[i][21] = '*'

	for i in range(22):
		BOARD[20][i] = '*'

	def draw(self, board, piece):
		piece_start_x = piece.pos_x
		piece_start_y = piece.pos_y
		piece_end_x = piece.pos_x + len(piece.shape)
		piece_end_y = piece.pos_y + len(piece.shape)
		for i in range(21):
			for j in range(22):
				if i >= piece_start_x and i < piece_end_x and j >= piece_start_y and j < piece_end_y:
					brick = piece.shape[i-piece_start_x][j-piece_start_y]
					if brick != ' ':
						print brick,
					else:
						print board[i][j],
				else:
					print board[i][j],
			print '\n'

	def __init__(self):

		# Padding board
		for i in range(21):
			self.BOARD[i][0] = '*'
			self.BOARD[i][21] = '*'

		for i in range(22):
			self.BOARD[20][i] = '*'

		while True:
			start_piece = Tetramino(choice(self.SHAPES), 0, choice(range(1,16)))
			self.draw(self.BOARD, start_piece)

			if not start_piece.has_moves(self.BOARD):
				print "Game finished"
				return

			while True:
				if start_piece.has_moves(self.BOARD):			
					command = raw_input("""					
								Move the piece.
								Available commands are:
								. a (return): move piece left
								. d (return): move piece right
								. w (return): rotate piece counter clockwise
								. s (return): rotate piece clockwise
							 """)

					prev_x = start_piece.pos_x
					prev_y = start_piece.pos_y
					prev_shape = start_piece.shape

					if command == 'a':
						# move left
						start_piece.move_left()
					if command == 'd':
						# move right
						start_piece.move_right()
					if command == 'w':
						# rotate counter clockwise
						start_piece.rotate_anticlockwise()
					if command == 's':
						# rotate clockwise
						start_piece.rotate_clockwise()

					if not start_piece.is_within_bounds(self.BOARD):
						print "Invalid move. Try again"
						# Rolling back
						start_piece = Tetramino(prev_shape, prev_x, prev_y)
					else:
						self.draw(self.BOARD, start_piece)
				else:
					# Add the piece to the board
					start_piece.copy(self.BOARD)
					break



if __name__ == '__main__':
	print "Running Tetris game."
	Game()
















