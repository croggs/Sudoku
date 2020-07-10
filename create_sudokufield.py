from random import shuffle
from random import randint


# ------------------------------------Hauptfunktionen-------------------------------------------
def valid_board(board,num):
    for n in range(0, 81):
        row = n // 9
        column = n % 9
        if board[row][column] == 0:
            shuffle(num)
            for number in num:
                if check_row(number, board, n):
                    if check_column(number, board, n):
                        if check_3x3(number, board, n):
                            board[row][column] = number
                            #for t in range(0, 9):
                                #print(board[t])
                            if full_field(board):
                                return True
                            else:
                                if valid_board(board,num):
                                    return True
            break
    #for y in range(0, 9):
        #print(board[y])
    print("")
    board[row][column] = 0

# --------------------------------Hilfsfunktionen--------------------------------------
def check_row(number, board, n):
    if number in (board[n//9]):
        return False
    else:
        return True


def check_column(number, board, n):
    for i in range(9):

        #print(board[i][n%9],i,n%9)
        #print(number == board[i][column])
        if number == board[i][n%9]:
            return False
    return True


def check_3x3(number, board, n):
    quad = [board[i][(n%9 // 3) * 3:(n%9 // 3 + 1) * 3] for i in range(((n//9) // 3)*3, ((n//9) // 3 + 1) * 3)];
    if number in (quad[0]+quad[1]+quad[2]):
        return False
    else:
        return True


def full_field(board):
    for n in range(9):
        for m in range(9):
            if board[n][m] == 0:
                return False
    return True

def zero_board(board):
    while board[row][col]==0:
        row = randint(0,8)
        col = randint(0,8)
    saved_board = board[row][col]
    board[row][col]=0

    return board
# -----------------------------------Main----------------------------------------------
'''board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valid_board(board)
for n in range(0, 9):
    print(board[n])
print("")'''

