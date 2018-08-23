import copy
'''Addition and multiplication of matrices'''
def mult_matrix(m_1, m_2, temp_1, temp_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if temp_1 != temp_2:
        print("Error: Matrix shapes invalid for mult")
        return None
    mul = []
    for itemp in range(0, len(m_1), 1):
        temp = []
        for jtemp in range(len(m_2[0])):
            res = 0
            for ktemp in range(0, len(m_2), 1):
                res += int(m_1[itemp][ktemp]) * int(m_2[ktemp][jtemp])
            temp.append(res)
        mul.append(temp)
    return mul


def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    len_1 = len(m_1)
    len_2 = len(m_2)
    if len_1 != len_2:
        print("Error: Matrix shapes invalid for addition ")
        return None
    add = copy.deepcopy(m_1)
    for itemp in range(0, len_2, 1):
        for jtemp in range(0, len(m_2[itemp]), 1):
            add[itemp][jtemp] = int(add[itemp][jtemp])
            add[itemp][jtemp] += int(m_2[itemp][jtemp])
    return add


def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    total = 0
    matrix = []
    val1 = int(size[0])
    for _ in range(0, val1, 1):
        row = input().split()
        matrix.append(row)
        total += len(row)
    return matrix, total
def main():
    '''main function for addition and multiplication'''
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    size1 = input().split(',')
    m_1, total1 = read_matrix(size1)
    size2 = input().split(',')
    m_2, total2 = read_matrix(size2)
    if total1 != total2:
        print("Error: Invalid input for the matrix")
    else:
        print(add_matrix(m_1, m_2))
        print(mult_matrix(m_1, m_2, size1[1], size2[0]))


if __name__ == '__main__':
    main()
