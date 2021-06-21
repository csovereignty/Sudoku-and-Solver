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