# tic tac toe game 

#  - 2 players should be able to play the game (both sitting at the same computer)
#  - the board should be printed out every time a player makes a move
#  - You should be able to accept input of the player position and then place a symbol on the board

import random

# test board for testing
test_board = ['#','X','O','X','O','X','O','X','O','X']

# game board outline and initial positions
game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# display board
def display_board(board):
    print('\n'*5)
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


# get player_input
def player_input():
    marker = ''

    # check if X or O is assigned
    while (marker != 'X' or marker != 'O'):
    # start by asking player #1 to choose X or O
        marker = input("Player #1, Do you want to be 'X' or 'O'?: ").upper()

    # assign that chosen marker to  p1
    p1 = marker

    # assign p2 the opposite of p1
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    # return tuple with (p1, p2)
    return(p1, p2)


# place marker in spot chosen by user
def place_marker(board, marker, position):
    board[position] = marker


# check if latest marker placed won the game
def check_for_winner(board, mark):
    
    return (
    (board[7] == mark and board[8] == mark and board[9] == mark) or # across top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # left side down
    (board[8] == mark and board[5] == mark and board[2] == mark) or # middle down
    (board[9] == mark and board[6] == mark and board[3] == mark) or # right side down
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)    # diagonal
    )


# randomly selecting which player makes the first move
def first_move():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# check if space is available to place marker
def space_open(board, position):

   return board[position] != ' '



# run the game
def play_game():
    display_board(game_board)
    player_input()

# play_game()


# ask if user wants to play again or not
def replay():
    new_game = input("Do you wish to play again ('Y' or 'N')? ").upper()

    if(new_game == 'Y'):
        play_game()
    else:
        print('Thanks for playing!')
