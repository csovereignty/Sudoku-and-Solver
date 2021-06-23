import random

random.seed()

#Generates and returns a random num from 1-9
def random_sudoku_num():
    return random.randrange(1,9,1)

#Returns true if the num exists in the row
def row_validation(grid, row, num):
    if num in grid[row]:
        return True
    return False

#Returns true if the num exists in the col
def col_validation(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False

#Return true if the num exists in the sub-section
def sub_validation(grid, row, col, num):
    sub_row = (row // 3) * 3
    sub_col = (col // 3) * 3
    for i in range(sub_row, (sub_row + 3)): 
        for j in range(sub_col, (sub_col + 3)):
            if grid[i][j] == num:
                return True
    return False

def validation_check(grid, row, col, num):
    if row_validation(grid, row, num):
        return False
    if col_validation(grid, col, num):
        return False
    if sub_validation(grid, row, col, num):
        return False
    return True

#need to make a function to create a valid board state (Backtracking)

#creates our grid which is basically a set of lists inside of a list
grid = [[0 for i in range(9)] for j in range(9)]

#prints our grid in a legible format! Yay!
for s in grid:
    print(*s)
print('')

#randomly assigns values to our grid
for i in range(0,81):
    row=i//9 #first time = 0 2nd = 0 3rd = 0 
    col=i%9 #first time = 0 2nd = 1 
    if grid[row][col] == 0:
        grid[row][col] = random_sudoku_num()


for s in grid:
    print(*s)


    