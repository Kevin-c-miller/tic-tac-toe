# tic tac toe game 

#  - 2 players should be able to play the game (both sitting at the same computer)
#  - the board should be printed out every time a player makes a move
#  - You should be able to accept input of the player position and then place a symbol on the board


# game board outline and initial positions
game_board = ['#','1','2','3','4','5','6','7','8','9']

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
    X_or_O = ''

    # check if X or O is assigned
    while not (X_or_O == 'X' or X_or_O == 'O'):
    # start by asking player #1 to choose X or O
        X_or_O = input("Player #1, Do you want to be 'X' or 'O'?: ").upper()

    # print(X_or_O)

    if X_or_O == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# place marker in spot chosen by user
def place_marker(board, marker, position):
    board[position] = marker


place_marker(game_board, '$', 8)
display_board(game_board)

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
