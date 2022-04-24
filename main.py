# tic tac toe game 

#  - 2 players should be able to play the game (both sitting at the same computer)
#  - the board should be printed out every time a player makes a move
#  - You should be able to accept input of the player position and then place a symbol on the board


# display board

def display_board(board):
    print('\n'*5)
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')




# get player_input
def player_input():
    X_or_O = ''

    # check if X or O is assigned
    while not (X_or_O == 'X' or X_or_O == 'O'):
    # start by asking player to choose X or O
        X_or_O = input("Player #1, Do you want to be 'X' or 'O'?: ").upper()

    if X_or_O == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


player_input()