def validateSudoku(sudoku):
    list_t = []
    sub = []
    if len(sudoku) == 81:
        for i in range(len(sudoku)):
            if i % 9 == 0 and i!=0:
                list_t.append(sub)
                sub = []
            sub.append(sudoku[i])
        list_t.append(sub)
    else:
        raise Exception("Invalid input")
    if (sudoku.count('.') == 0):
        raise Exception("Given sudoku is solved")
    possibleValues(list_t)

def duplicate(st):
    suduko1 = list()
    for i in st:
        if i != ".":
            if i not in suduko1:
                suduko1.append(i)
            else:
                raise Exception("Invalid Sudoku:Duplicate values")
                return

def getRowValues(i, list_t):
    return list_t[i]

def getColumnValues(i, list_t):
    column = []
    for row in list_t:
        column.append(row[i])
    return column
def getGridValues(i, j, list_t):
    SubGrid = list()
    if (i >= 0 and i < 3) and (j >= 0 and j < 3):
        for subrow in range(0, 3):
            for subcol in range(0, 3):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 0 and i < 3) and (j >= 3 and j < 6):
        for subrow in range(0, 3):
            for subcol in range(3, 6):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 0 and i < 3) and (j >= 6 and j < 9):
        for subrow in range(0, 3):
            for subcol in range(6, 9):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 3 and i < 6) and (j >= 0 and j < 3):
        for subrow in range(3, 6):
            for subcol in range(0, 3):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 3 and i < 6) and (j >= 3 and j < 6):
        for subrow in range(3, 6):
            for subcol in range(3, 6):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 3 and i < 6) and (j >= 6 and j < 9):
        for subrow in range(3, 6):
            for subcol in range(6, 9):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 6 and i < 9) and (j >= 0 and j < 3):
        for subrow in range(6, 9):
            for subcol in range(0, 3):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 6 and i < 9) and (j >= 3 and j < 6):
        for subrow in range(6, 9):
            for subcol in range(3, 6):
                SubGrid.append(list_t[subrow][subcol])
    if (i >= 6 and i < 9) and (j >= 6 and j < 9):
        for subrow in range(6, 9):
            for subcol in range(6, 9):
                SubGrid.append(list_t[subrow][subcol])
    return SubGrid
def possibleValues(list_t):
    for i in range(len(list_t)):
        for j in range(len(list_t[0])):
            if list_t[i][j] == ".":
                duplicate(getRowValues(i, list_t))
                duplicate(getColumnValues(i, list_t))
                duplicate(getGridValues(i, j, list_t))
                possibilities(i, j, list_t)
def possibilities(i , j, list_t):
    newstring = [1,2,3,4,5,6,7,8,9]
    newlist = []
    r = maptointegers(getRowValues(i, list_t))
    c = maptointegers(getColumnValues(j, list_t))
    g = maptointegers(getGridValues(i, j, list_t))
    finalanswer = ""
    for each in newstring:
        if each not in r:
            if each not in c:
                if each not in g:
                    newlist.append(each)
    finalanswer = list(map(str, newlist))
    finalanswer = ''.join(finalanswer)
    print(finalanswer)
    return finalanswer
def maptointegers(integerlist):
    row = ''.join(integerlist)
    row = row.replace(".", "")
    row = list(row)
    finalmappedint = list(map(int, row))
    return finalmappedint

def main():
    inp = str(input())
    try:
        validateSudoku(inp)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()