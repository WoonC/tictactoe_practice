import random
#Show Board Structure
def display_board(board):
    print(board[7] + "  |  " + board[8] + "  |  " + board[9])
    print(board[4] + "  |  " + board[5] + "  |  " + board[6])
    print(board[1] + "  |  " + board[2] + "  |  x" + board[3])

test_board = ['#','X','','X','O','X','O','X','O','X']

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

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ''

def full_board_check(board):
    for i in range(1,10):
        if board[i] == '':
            return False
    return True

def player_choice(board):
    position = []
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Please enter a number between 1-9: '))

    return position

def replay():
    response = input('Y to play again, N to stop playing: ').upper()
    return response == 'Y'

#### RUNNING THE GAME ####
while True:
    the_board = ['']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input('Ready to play the game? Y or N: ').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## During game play
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker, position)

            if win_check(the_board,player1_marker):
                print('Player 1 has won')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board,player2_marker):
                print('Player 2 has won')
                game_on = False

            else:
                if full_board_check(the_board):
                    print('Tie')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

