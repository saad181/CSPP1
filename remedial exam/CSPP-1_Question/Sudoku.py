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
def validateSudoku(sudoku):
    list_t = []
    sublist =[]
    if len(sudoku) == 81:
        for i in range(len(sudoku)):
            if i %9==0 and i!=0:
                list_t.append(sublist)
                sublist.append(sudoku)
                list_t.append(sublist)
            else:
                raise Exception("Invalid input")
            if (list_t.count(".")==0):
                raise Exception("Given sudoku is solved")
            possibleValues(list_t)



    #pass
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues(i,list_t):
    return list_t[i]
    
    #pass
"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(i,list_t):
    col=[]
    for row in list_t:
        col.append(row)
    return col    
    
    #pass

"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues(i,j,list_t):
    sub=list()
    if (i>=0 and i<3) and (j>=0 and j<3):
        for subrow in range(0,3):
            for subcolumn in range(0,3):
                sub.append(list_t[subrow][subcolumn])  # for 1 subgrid
    if (i>=0 and i<3) and (j>=3 and j<6):
        for subrow in range(0,3):
            for subcolumn in range(3,6):
                sub.append(list_t[subrow][subcolumn])  #for 2 subgrid
    if (i>=0 and i<3) and (j>=6 and j<9):
        for subrow in range(0,3):
            for subcolumn in range(6,9):
                sub.append(list_t[subrow][subcolumn])   #for 3 subgrid
    if (i>=3 and i<6) and (j>=0 and j<3):
        for subrow in range(3,6):
            for subcolumn in range(0,3):
                sub.append(list_t[subrow][subcolumn]) # for 4 subgrid
    if (i>=3 and i<6) and (j>=3 and j<6):
        for subrow in range(3,6):
            for subcolumn in range(3,6):
                sub.append(list_t[subrow][subcolumn])   #for 5 subgrid
    if (i>=3 and i<6) and (j>=6 and j<9):
        for subrow in range(3,6):
            for subcolumn in range(6,9):
                sub.append(list_t[subrow][subcolumn])   #for 6 subgrid                                                
    if (i>=6 and i<9) and (j>=0 and j<3):
        for subrow in range(6,9):
            for subcolumn in range(0,3):
                sub.append(list_t[subrow][subcolumn])  #for 7 subgrid
    if (i>=6 and i<9) and (j>=3 and j<6):
        for subrow in range(6,9):
            for subcolumn in range(3,6):
                sub.append(list_t[subrow][subcolumn])   #for 8 subgrid
    if (i>=6 and i<9) and (j>=6 and j<9):
        for subrow in range(6,9):
            for subcolumn in range(6,9):
                sub.append(list_t[subrow][subcolumn])  #for 9 subgrid
    return sub            


    #pass
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues(list_t):
    for i in range(len(list_t)):
        for j in range(len(list_t[0])):
            if list_t[i][j]=='.':
                duplicate( getRowValues(i,list_t))
                duplicate(getColumnValues(i,list_t))
                duplicate(getGridValues(i,j,list_t))
                value(i,j,list_t)
def value(i,j,list_t):
    num=[1,2,3,4,5,6,7,8,9]
    new=[]
    row_val = converttointegers(getRowValues(i,list_t))
    col_val = converttointegers(getColumnValues(i,list_t))
    grid_val = converttointegers(getGridValues(i,j,list_t))
    ans = ""
    for i in num:
        if i not in row_val and i not in col_val and i not in grid_val:
                    new.append(i)
    ans=list(map(str,new))
    ans=''.join(ans)                
                   
    print(ans)
    return ans                


def converttointegers(integer):
    row = row.replace(".","")
    row = list(row)
    mapped = list(map(int,row))
    return mapped



    #pass
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def duplicate(st):
    suduko1 = list()
    for i in st:
        if i != "." and  i != suduko1:
            suduko1.append(i)
        else:
            raise Exception("Invalid Sudoku:Duplicate found")
        return
          
def main():
    inp = input()
    try:
        check(inp)
    except Exception as e:
        print(e) 


    if __name__ == '__main__':
        main()
