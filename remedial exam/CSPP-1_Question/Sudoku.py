"""
In this method :
 * Check there are only 81 values
 * iterate through each row in the sudoku and if you find any duplicate values
    raise an exception
 * iterate through each column in the sudoku and if you find any duplicate values
    raise an exception
 * iterate through each subgrid(3x3) in the sudoku and if you find any duplicate values
    raise an exception
"""
def validateSudoku(sudoku,i=0,j=0):
    for i in range(i,9):
        for j in range(j,9):
            if sudoku[i][j]==0:
                return[i][j]
    

    pass
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues():
    num='123456789'
    for i in range(9):
        if num != row:
            return num
    pass
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues():
    num='123456789'
    for i in range(9):
        if num != column:
            return num
    pass

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues():
    pass
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues():
    pass
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
    inp = input()
    if "." not in inp:
        print("Given suduko is solved")
    else:
        suduko = []
        k = 0
        for i in range(9):
            row = []
            for j in range(9):
                row.append(inp[k])
                k = k + 1
            suduko.append(row)
            print("Given suduko is solved")

if __name__ == '__main__':
        main()
