
"""
problem description @ http://acm.uva.es/p/v101/10189.html
"""

def neighbours(i,j):
    yield i, j-1 #left side
    yield i-1, j-1 #top left diagonal
    yield i-1, j #top
    yield i-1, j+1 #top right diagonal
    yield i, j+1 #right
    yield i+1, j+1 #bottom right diagonal
    yield i+1, j #bottom
    yield i+1, j-1 #bottom left diagonal

def mine_sweeper(rows, columns, data):

    matrix = []

    #populate the matrix
    for i in range(rows):
        matrix.append(list(data[i]))

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '*':
                continue

            for neighbour_row, neighbour_col in neighbours(i,j):

                if (neighbour_row < 0 or neighbour_row > rows - 1 or \
                    neighbour_col < 0 or neighbour_col > columns - 1):
                    continue

                if matrix[neighbour_row][neighbour_col] == '*':
                    try:

                        matrix[i][j] += 1
                    except TypeError:
                        #first time
                        matrix[i][j] = 1

            if matrix[i][j] == '.':
                matrix[i][j] = 0

            matrix[i][j] = str(matrix[i][j])

    return [''.join(matrix[i]) for i in range(rows)]

if __name__ == '__main__':

    assert mine_sweeper(3, 5, ('**...', '.....', '.*...')) == ['**100', '33200', '1*100']
    assert mine_sweeper(4, 4, ('*...', '....', '.*..', '....')) == ['*100', '2210', '1*10', '1110']


    


