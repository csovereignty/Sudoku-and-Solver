import random

random.seed()

#creates our grid which is basically a set of lists inside of a list
grid = [[0 for i in range(9)] for j in range(9)]

#prints our grid in a legible format! Yay!
for s in grid:
    print(*s)
print('')

for i in range(9):
    if grid[0][i] == 0:
        grid[0][i] = random.randrange(1,9,1)
    for j in grid[0]:
        if grid[0][j] == grid[0][i]:
            continue #holdover here


for s in grid:
    print(*s)