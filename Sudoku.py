import random

random.seed()

grid = [[0 for i in range(9)] for j in range(9)]



def check_row(self, grid, row, number):
    #check if row is valid
    if number in grid[row]:
        return True
    return False

def check_col(self, grid, col, number):
    #check if col is valid
    for i in range(9):
        if grid[i][col] == number:
            return True
    return False

def check_subgrid(self,grid,row,col,number):
		#check subgrid for valid numbers
		sub_row = (row // 3) * 3
		sub_col = (col // 3)  * 3
		for i in range(sub_row, (sub_row + 3)): 
			for j in range(sub_col, (sub_col + 3)): 
				if grid[i][j] == number: 
					return True
		return False


print(grid)
#finish working on making the grid and creating a proper sudoku puzzle then work on solving