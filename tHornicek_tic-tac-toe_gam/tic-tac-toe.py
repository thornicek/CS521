"""
Tic Tac Toe Simulation Starter Code
"""
#Tomas Hornicek, no collaborators, https://developer.mozilla.org/en-US/ ,Lecture Slides,https://www.w3schools.com/, no extension

import random


class TicTacToeSim:

	# Part 1
	def __init__(self):
		# Initialize the simulation
		# Set up board as a 2D list, turn to player 1, and ai to false
		# Required fields: board, turn, AI, AI_turn
		#board
		self.board = [[0,0,0],[0,0,0],[0,0,0]]
		self.turn = 1





	def change_turn(self):
		# Change turn to other player
		if self.turn == 1:
			self.turn = 2
			return 2
		else:
			self.turn = 1
			return 1




	def play_game(self):
		# This is the driver method for the simulation
		finished = False
		self.get_settings()
		while not finished:
			self.print_board()
			if self.AI and self.turn == self.AI_turn:
				print("AI making move...")
				move = self.smart_move()
				self.make_move(move,self.AI_turn)
			else:
				self.take_turn(self.turn)
			self.change_turn()
			result = self.check_winner()
			if result != 0:
				finished = True
				if result != -1:
					print(f"Game Over, Player{result} Won")
				else:
					print("Game Over, Draw")
				self.print_board()


	# Part 2
	def print_board(self):
		# Print the state of the board using X (player 1) and O (player 2)
		for i in range(len(self.board)):
			print(self.board[i])



	# Part 3
	def get_move(self):
		# Get input from user asking for their move as a tuple
		row = int(input("Enter row: "))
		col = int(input("Enter column: "))
		tupInput =(row,col)
		return tupInput
	# Part 4
	def take_turn(self, player):
		# This is the driver method for a players turn
		move =self.get_move()
		row = int(move[0])
		column = int(move[1])
		if (row >= 3 or column >= 3)or(self.board[row][column] != 0) :
			self.take_turn(player)
		else:
			self.make_move(move, player)


	def get_available_squares(self):
		# Get a list of available squares as tuples (row,col)
		availableSpots = []
		for row in range(len(self.board)):
			for col in range(len(self.board)):
				if (self.board[row][col] == 0):
					posTuple = (row,col)
					availableSpots.append(posTuple)
		return availableSpots

	def make_move(self, move, player):
		row = int(move[0])
		column = int(move[1])
		self.board[row][column] = player


	# Part 5
	def check_winner(self):
		# Check if a player has won, there are 8 ways to win.
		# Return the player who won 0 if nobody has won, and -1 if it is a draw
		if len(self.get_available_squares()) == 0:
			return -1
		previous = None
		# Checking all rows
		for row in range(len(self.board)):
			for col in range(len(self.board)):
				current = self.board[row][col]
				if current != previous and previous is not None:
					previous = None
					break
				if col == len(self.board) - 1 and current != 0:
					return current
				previous = current
		previous = None
		# Checking all columns
		for col in range(len(self.board)):
			for row in range(len(self.board)):
				current = self.board[row][col]
				if current != previous and previous is not None:
					previous = None
					break
				if row == len(self.board) - 1 and current != 0:
					return current
				previous = current
		previous = None
		# Checking first diagonal
		for i in range(len(self.board)):
			current = self.board[i][i]
			if current != previous and previous is not None:
				break
			if i == len(self.board) - 1 and current != 0:
				return current
			previous = current
		previous = None
		# Checking second diagonal
		for i in range(len(self.board)):
			current = self.board[len(self.board)-1-i][i]
			if current != previous and previous is not None:
				break
			if i == len(self.board) - 1 and current != 0:
				return current
			previous = current
		return 0

	# Part 6
	def random_move(self):
		"""Returns a random move from the list of available squares."""
		available_moves = self.get_available_squares()
		move = random.choice(available_moves)
		return move

	# Part 7
	def winning_move(self, player = None):
		# Find a winning move for a player
		available_moves = self.get_available_squares()
		for move in available_moves:
			if hasattr(self,"winning_row") and self.winning_row == move[0]:
				self.winning_row = None
				self.winning_col = None
				self.winning_diag = None
				return move
			elif hasattr(self,"winning_col") and self.winning_col == move[1]:
				self.winning_row = None
				self.winning_col = None
				self.winning_diag = None
				return move
			elif hasattr(self,"winning_diag") and self.winning_diag == "top left" and move[0] == move[1]:
				self.winning_row = None
				self.winning_col = None
				self.winning_diag = None
				return move
			elif hasattr(self,"winning_diag") and self.winning_diag == "top right" and move[0] + move[1] == len(self.board)-1:
				self.winning_row = None
				self.winning_col = None
				self.winning_diag = None
				return move


	def threat_to_lose(self):
		# Run winning_move from other perspective
		available_moves = self.get_available_squares()
		for move in available_moves:
			if hasattr(self,"losing_row") and self.losing_row == move[0]:
				self.losing_row = None
				self.losing_col = None
				self.losing_diag = None
				return move
			elif hasattr(self,"losing_col") and self.losing_col == move[1]:
				self.losing_row = None
				self.losing_col = None
				self.losing_diag = None
				return move
			elif hasattr(self,"losing_diag") and self.losing_diag == "top left" and move[0] == move[1]:
				self.losing_row = None
				self.losing_col = None
				self.losing_diag = None
				return move
			elif hasattr(self,"losing_diag") and self.losing_diag == "top right" and move[0] + move[1] == len(self.board)-1:
				self.losing_row = None
				self.losing_col = None
				self.losing_diag = None
				return move

	def smart_move(self):
		# If there is a winning move, win
		# If there is a threat to lose, block
		# Make random move
		length = len(self.board) - 1
		p1Count = 0
		p2Count = 0
		winnable = False
		losable = False
		zeroCount = 0
		#Row smart_move
		for row in range(len(self.board)):
			for col in range(len(self.board)):
				if self.board[row][col] == 1:
					p1Count += 1
				elif self.board[row][col] == 2:
					p2Count += 1
				elif self.board[row][col] == 0:
					zeroCount += 1
			if p1Count == length and self.AI_turn == 1 and zeroCount == 1:
				winnable = True
				self.winning_row = row
			elif p1Count == length and self.AI_turn == 2 and zeroCount == 1:
				losable = True
				self.losing_row = row
			elif p2Count == length and self.AI_turn == 2 and zeroCount == 1:
				winnable = True
				self.winning_row = row
			elif p2Count == length and self.AI_turn == 1 and zeroCount == 1:
				losable = True
				self.losing_row = row
			p1Count = 0
			p2Count = 0
			zeroCount = 0
		p1Count = 0
		p2Count = 0
		zeroCount = 0
		#Column smart_move 
		for col in range(len(self.board)):
			for row in range(len(self.board)):
				if self.board[row][col] == 1:
					p1Count += 1
				elif self.board[row][col] == 2:
					p2Count += 1
				elif self.board[row][col] == 0:
					zeroCount += 1
			if p1Count == length and self.AI_turn == 1 and zeroCount == 1:
				winnable = True
				self.winning_col = col
			elif p1Count == length and self.AI_turn == 2 and zeroCount == 1:
				losable = True
				self.losing_col = col
			elif p2Count == length and self.AI_turn == 2 and zeroCount == 1:
				winnable = True
				self.winning_col = col
			elif p2Count == length and self.AI_turn == 1 and zeroCount == 1:
				losable = True
				self.losing_col = col
			p1Count = 0
			p2Count = 0
			zeroCount = 0
		p1Count = 0
		p2Count = 0
		zeroCount = 0
		#Top left diagonal smart_move
		for i in range(len(self.board)):
			if self.board[i][i] == 1:
				p1Count += 1
			elif self.board[i][i] == 2:
				p2Count += 1
			elif self.board[i][i] == 0:
				zeroCount += 1
		if p1Count == length and self.AI_turn == 1 and zeroCount == 1:
			winnable = True
			self.winning_diag = "top left"
		elif p1Count == length and self.AI_turn == 2 and zeroCount == 1:
			losable = True
			self.losing_diag = "top left"
		elif p2Count == length and self.AI_turn == 2 and zeroCount == 1:
			winnable = True
			self.winning_diag = "top left"
		elif p2Count == length and self.AI_turn == 1 and zeroCount == 1:
			losable = True
			self.losing_diag = "top left"
		p1Count = 0
		p2Count = 0
		zeroCount = 0
		#Top Right diagonal smart_move
		for i in range(len(self.board)):
			current = self.board[len(self.board)-1-i][i]
			if self.board[len(self.board)-1-i][i] == 1:
				p1Count += 1
			elif self.board[len(self.board)-1-i][i] == 2:
				p2Count += 1
			elif self.board[len(self.board)-1-i][i] == 0:
				zeroCount += 1
		if p1Count == length and self.AI_turn == 1 and zeroCount == 1:
			winnable = True
			self.winning_diag = "top right"
		elif p1Count == length and self.AI_turn == 2 and zeroCount == 1:
			losable = True
			self.losing_diag = "top right"
		elif p2Count == length and self.AI_turn == 2 and zeroCount == 1:
			winnable = True
			self.winning_diag = "top right"
		elif p2Count == length and self.AI_turn == 1 and zeroCount == 1:
			losable = True
			self.losing_diag = "top right"
		if winnable:
			return self.winning_move()
		if losable:
			return self.threat_to_lose()
		return self.random_move()
	# Part 8
	def get_settings(self):
		# At the start of the simulation, get settings from the user
		# Decide whether to play vs AI and if so whether the user is first or second
		self.turn = 1
		playerAIInput = input("Do you want to play against AI? Answer True or False: ")
		if playerAIInput == "True":
			self.AI = True
			playerOrderInput = input("Would you like to be Player1 or Player2? Type \"1\" or \"2\": ")
			if playerOrderInput == "1":
				self.AI_turn = 2
			elif playerOrderInput == "2":
				self.AI_turn = 1
			else:
				self.get_settings()
		elif playerAIInput == "False":
			self.AI = False

		else:
			self.get_settings()

#### ONLY FOR TESTING #####
#### DO NOT PUT TESTING CODE OUTSIDE OF HERE ####
if __name__ == '__main__':
	sim = TicTacToeSim()
	sim.play_game()


