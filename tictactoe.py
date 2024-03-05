
#Show Board Structure
def display_board(board):
    print(board[7] + " | " + board[8] + " | " + board[9])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[1] + " | " + board[2] + " | " + board[3])

test_board = ['#','1','2','3','4','5','6','7','8','9']

#Take in player input
def player_input():
    marker = []
    while marker != 'X' or marker != 'O':
        marker = input('Please enter X or O: ').upper()

        if marker == 'X':
            return 'X','O'
        if marker == 'O':
            return 'O','X'
        else:
            print('X or O only')

#Changing board markers to X or O
def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

print(win_check(test_board, 'X'))
print(test_board)
