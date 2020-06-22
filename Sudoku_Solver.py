
"""
Title: Sudoku Solver
Author: Karl Duggan
Date: 17/06/2020

"""
import os

class Sudoku_Solver():
	def __init__(self):
		self.game = None
		self.resolved_game = None

	# Terminal menu
	def start(self):
		os.system('clear')
		print("--------- Sudoku Solver ---------\n")
		print("please select one of the following: \n")
		print(" 1 - Input a Sudoku puzzle.")
		print(" 2 - Test a Sudoku Puzzle.\n")

		select = input("Please make your selection: \n")
		if select == '1':
			self.run_puzzle()
		if select == '2':
			self.test_puzzle()

	# Print game in the terminal.
	def print_game(self):
	    for i in range(len(self.game)):
	        if i % 3 == 0 and i != 0:
	            print("- - - - - - - - - - - -")
	        for j in range(len(self.game[0])):
	            if j % 3 == 0 and j != 0:
	                print(" | ", end="")
	            if j == 8:
	                print(self.game[i][j])
	            else:
	                print(str(self.game[i][j]) + " ", end="")

	# The check has been broken down into smaller function and compiled into one.
	def check_valid(self, game, choice, pos):
		if self._check_row_valid(game, choice, pos):
			if self._check_col_valid(game, choice, pos):
				if self._check_square_valid(game, choice, pos):
					return True
		return False

	def input_game(self):
	    grid = []
	    print('Please type the numbers without spaces "xxxxxxxxx" \nIf blank eneter 0.')
	    for row in range(9):
	        number_line = input('Enter row {} numbers: '.format(row+1))
	        line = [int(i) for i in number_line ]
	        grid.append(line)
	    self.game = grid

	# Check if choice is valid in row.
	def _check_row_valid(self, game, choice, pos):
		for i in range(0,9):
			if game[pos[0]][i] == choice:
				return False
		return True
	# Check if choice is valid in colume. 
	def _check_col_valid(self, game, choice, pos):
		for i in range(0,9):
			if game[i][pos[1]] == choice:
				return False
		return True
	# Check if choice is valid in square. 
	def _check_square_valid(self, game, choice, pos):
		square_x = (pos[1] // 3) * 3
		square_y = (pos[0] // 3) * 3
		for i in range(0,3):
			for j in range(0,3):
				if game[square_y + i][square_x + j] == choice:
					return False
		return True

	def solver(self):
		# Start by finding an empty which is represented as a 0.
		for row in range(9):
			for col in range(9):
				if self.game[row][col] == 0:
					pos = (row,col)
					# Looping through a choice between 1 and 9.
					for choice in range(1,10):
						if self.check_valid(self.game, choice, pos):
							self.game[row][col] = choice
							# Once a choice has been confirmed we continue with the next with recursion by calling the solver function again.
							self.solver()
							# Backtracking, If the choice is incorrect we replace it with a 0 and go to the previous choice . 
							self.game[row][col] = 0 
					# If there are no longer any 0 and all is complete we will return.
					return
		# Print the final solution.
		self.print_game()
		input('Press Enter for More:')

	def test_puzzle(self):
		sudoku_game = [[0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,1,6,0],[0,6,7,0,3,5,0,0,4],
				 	   [6,0,8,1,2,0,9,0,0],[0,0,0,0,8,0,0,3,0],[0,0,2,0,7,9,8,0,6],
					   [8,0,0,6,9,0,3,5,0],[0,2,6,0,0,0,0,9,0],[0,0,0,0,0,0,0,0,0]]

		self.game = sudoku_game
		os.system('clear')
		print('Unresolved')
		self.print_game()
		print('>>>>>>>>>>>>>>>>>>>>>>>>')
		print('Resolved')
		self.solver()


	def run_puzzle(self):
		self.input_game()
		os.system('clear')
		print('Unresolved')
		self.print_game()
		print('>>>>>>>>>>>>>>>>>>>>>>>>')
		print('Resolved')
		self.solver()


if __name__ == '__main__':

	game = Sudoku_Solver()
	game.start()

	

	
