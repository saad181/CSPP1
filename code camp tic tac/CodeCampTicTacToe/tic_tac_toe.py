'''Tic Tac Toe Game'''
def loop(set0):
    '''Checking the value '''
    if 'x' in set0:
        return 'x'
    return 'o'

def playgame(game):
    '''Checking winner of game '''
    set1, set2, set3, set4, set5 = set(), set(), set(), set(), set()
    length = len(game)
    for i in range(length):
        for j in range(len(game[i])):
            if i == j:
                set1.add(game[i][j])
            if i + j == (len(game)-1):
                set2.add(game[i][j])
            sett = set(game[i])
            if len(sett) == 1:
                if 'x' in sett:
                    return 'x'
                return 'o'
            if j == 0:
                set3.add(game[i][j])
            if j == 1:
                set4.add(game[i][j])
            if j == 2:
                set5.add(game[i][j])
    if len(set1) == 1:
        return loop(set1)
    if len(set2) == 1:
        return loop(set2)
    if len(set3) == 1:
        return loop(set3)
    if len(set4) == 1:
        return loop(set4)
    if len(set5) == 1:
        return loop(set5)
    return "draw"

def validity_check(game):
    '''Validating players'''
    x_element = 'x'
    o_element = 'o'
    count_x, count_o, count_t = 0, 0, 0
    for index in game:
        # print("Invalid")
        if len(index) != 3:
            return "invalid game"
        if x_element in index:
            count_x += index.count(x_element)
        if o_element in index:
            count_o += index.count(o_element)
        if '.' in index:
            count_t += index.count('.')
    if count_x + count_o + count_t != 9:
        return "invalid input"
    if abs(count_x - count_o) != 1:
        return "invalid game"
    return playgame(game)

def main():
    '''Main function '''
    row = []
    for _ in range(3):
        column = input()
        column = list(map(str, column.split(' ')))
        row.append(column)
    row = validity_check(row)
    print(row)

if __name__ == '__main__':
    main()