#This code is mainly for testing purposes, not ready to be included in final program, but helps keep ideas

from random import shuffle

def create_puzzle(self, grid):
    possible_numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(0,81):
        row=i//9
        col=i%9
		#find next empty cell
        if grid[row][col]==0:
            shuffle(possible_numbers)      
            for number in possible_numbers:
                if self.valid_location(grid,row,col,number):
                    self.path.append((number,row,col))
                    grid[row][col]=number
                    if not self.find_empty_square(grid):
                        return True
                    else:
                        if self.generate_solution(grid):
						#if the grid is full
                            return True
		    break
    grid[row][col]=0  
    return False

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