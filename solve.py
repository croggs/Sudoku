global solutions
from create_sudokufield import *
def solve(board,num):
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
                            if full_field():
                                solutions+=1
                                break
                            else :
                                if solve():
                                    return True
            break
    board[row][column] = 0

