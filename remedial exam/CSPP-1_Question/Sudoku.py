def check(sudoku):
    construct = []
    sublist = []
    if len(sudoku) == 81:
        for i in range(len(sudoku)):
            if i % 9 == 0 and i!=0:
                construct.append(sublist)
                sublist = []
            sublist.append(sudoku[i])
        construct.append(sublist)
    else:
        raise Exception("Invalid input")
    if (sudoku.count('.') == 0):
        raise Exception("Given sudoku is solved")
    possibleValues(construct)
def eliminatedups(string):
    listt = list()
    for i in string:
        if i != ".":
            if i not in listt:
                listt.append(i)
            else:
                raise Exception("Invalid Sudoku:Duplicate values")
                return
def validRow(i, construct):
    return construct[i]
def validCol(i, construct):
    column = []
    for row in construct:
        column.append(row[i])
    return column
def validGrid(i, j, construct):
    SubGrid = list()
    if (i >= 0 and i < 3) and (j >= 0 and j < 3):
        for subrow in range(0, 3):
            for subcol in range(0, 3):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 0 and i < 3) and (j >= 3 and j < 6):
        for subrow in range(0, 3):
            for subcol in range(3, 6):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 0 and i < 3) and (j >= 6 and j < 9):
        for subrow in range(0, 3):
            for subcol in range(6, 9):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 3 and i < 6) and (j >= 0 and j < 3):
        for subrow in range(3, 6):
            for subcol in range(0, 3):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 3 and i < 6) and (j >= 3 and j < 6):
        for subrow in range(3, 6):
            for subcol in range(3, 6):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 3 and i < 6) and (j >= 6 and j < 9):
        for subrow in range(3, 6):
            for subcol in range(6, 9):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 6 and i < 9) and (j >= 0 and j < 3):
        for subrow in range(6, 9):
            for subcol in range(0, 3):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 6 and i < 9) and (j >= 3 and j < 6):
        for subrow in range(6, 9):
            for subcol in range(3, 6):
                SubGrid.append(construct[subrow][subcol])
    if (i >= 6 and i < 9) and (j >= 6 and j < 9):
        for subrow in range(6, 9):
            for subcol in range(6, 9):
                SubGrid.append(construct[subrow][subcol])
    return SubGrid
def possibleValues(construct):
    for i in range(len(construct)):
        for j in range(len(construct[0])):
            if construct[i][j] == ".":
                eliminatedups(validRow(i, construct))
                eliminatedups(validCol(i, construct))
                eliminatedups(validGrid(i, j, construct))
                possibilities(i, j, construct)
def possibilities(i , j, construct):
    newstring = [1,2,3,4,5,6,7,8,9]
    newlist = []
    r = maptointegers(validRow(i, construct))
    c = maptointegers(validCol(j, construct))
    g = maptointegers(validGrid(i, j, construct))
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
    inputstring = str(input())
    try:
        check(inputstring)
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()