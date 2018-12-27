def validateSudoku(sudoku):
    list_t = []
    sublist = []
    if len(sudoku) == 81:
        for i in range(len(sudoku)):
            if i % 9 == 0 and i!=0:
                list_t.append(sublist)
                sublist = []
            sublist.append(sudoku[i])
        list_t.append(sublist)
    else:
        raise Exception("Invalid input")
    if (sudoku.count('.') == 0):
        raise Exception("Given sudoku is solved")
    possibleValues(list_t)
def eliminatedups(string):
    listt = list()
    for i in string:
        if i != ".":
            if i not in listt:
                listt.append(i)
            else:
                raise Exception("Invalid Sudoku:Duplicate values")
                return
def validRow(i, list_t):
    return list_t[i]
def validCol(i, list_t):
    column = []
    for row in list_t:
        column.append(row[i])
    return column
def validGrid(i, j, list_t):
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
                eliminatedups(validRow(i, list_t))
                eliminatedups(validCol(i, list_t))
                eliminatedups(validGrid(i, j, list_t))
                possibilities(i, j, list_t)
def possibilities(i , j, list_t):
    newstring = [1,2,3,4,5,6,7,8,9]
    newlist = []
    r = maptointegers(validRow(i, list_t))
    c = maptointegers(validCol(j, list_t))
    g = maptointegers(validGrid(i, j, list_t))
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