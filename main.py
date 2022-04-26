import random

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
    while not (marker == 'X' or marker == 'O'):
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
    return board[position] == ' '
    # addc check if spot taken by the other player


# check if all spaces are full of markers
def check_full_board(board):
    for i in range(1,10):
        if space_open(board, i):
            return False
    # board is full if returned True
    return True



# ask for player choice
def player_choice(game_board):
    position = 0

    while position not in range(1,10) or not space_open(game_board, position):
        position = int(input('Where would you like to place your next marker (1-9)?: '))
        if position in range(1,10):
            break
    
    return position



# ask if user wants to play again or not
def replay():
    return input("Do you wish to play again ('yes' or 'no')? ").lower().startswith('y')

# play the game
def start_game():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        game_board = [' '] * 10
        player1_marker, player2_marker = player_input()
        # randomly checking first move
        turn = first_move()
        print(f'{turn} will make the first move')
        
        # game start prompt
        play_game = input('Are you ready to play? Enter Yes or No.')
        
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.
                
                # show board
                display_board(game_board)
                # get player choice
                position = player_choice(game_board)
                # place marker where player chose 
                place_marker(game_board, player1_marker, position)

                # check if there is a winner based on last move
                if check_for_winner(game_board, player1_marker):
                    # display board
                    display_board(game_board)
                    # if player won - show message
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    # check if all spaces are filled
                    if check_full_board(game_board):
                        display_board(game_board)
                        # tie message
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.
                
                # show board
                display_board(game_board)
                # player choice
                position = player_choice(game_board)
                # place player choice 
                place_marker(game_board, player2_marker, position)

                # check for winner
                if check_for_winner(game_board, player2_marker):
                    # display board
                    display_board(game_board)
                    # winning message
                    print('Player 2 has won!')
                    game_on = False
                else:
                    # check if all spaces filled or not
                    if check_full_board(game_board):
                        display_board(game_board)
                        # draw message
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
        # replay message
        if not replay():
            break

start_game()