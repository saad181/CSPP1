'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    def findNextCellToFill(grid, i, j):
            for x in range(i,9):
                    for y in range(j,9):
                            if grid[x][y] == 0:
                                    return x,y
            for x in range(0,9):
                    for y in range(0,9):
                            if grid[x][y] == 0:
                                    return x,y
            return -1,-1

    def isValid(grid, i, j, e):
            rowOk = all([e != grid[i][x] for x in range(9)])
            if rowOk:
                    columnOk = all([e != grid[x][j] for x in range(9)])
                    if columnOk:
                            # finding the top left x,y co-ordinates of the section containing the i,j cell
                            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                            for x in range(secTopX, secTopX+3):
                                    for y in range(secTopY, secTopY+3):
                                            if grid[x][y] == e:
                                                    return False
                            return True
            return False

    def solveSudoku(grid, i=0, j=0):
            i,j = findNextCellToFill(grid, i, j)
            if i == -1:
                    return True
            for e in range(1,10):
                    if isValid(grid,i,j,e):
                            grid[i][j] = e
                            if solveSudoku(grid, i, j):
                                    return True
                            # Undo the current cell for backtracking
                            grid[i][j] = 0
            return False


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()