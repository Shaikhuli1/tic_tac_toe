def display_board(board):

    '''
    Nought and crosses board
    '''
    
    print('\n'*25)    #Adds blank lines so you don't see the board history

    print('   |   |')
    print(' ' + board[7]+ ' | ' + board[8]+ ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4]+ ' | ' + board[5]+ ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1]+ ' | ' + board[2]+ ' | ' + board[3])
    print('   |   |')

############################################
def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)

##############################################
def place_marker(board,marker,position):

    '''
    Edits the board with the marker and position
    '''

    board[position] = marker
    
##############################################
def win_check(board,mark):

    '''
    Checks to see if any of the winning criteria are met
    i.e. Matching row, column or diagonal
    '''
    #rows
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    
    #Columns
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    
    #Diagonal
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))
    
##############################################
import random
def choose_first():

    '''
    Simple coin toos to determine who goes first
    '''

    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
##############################################
def space_check(board,position):

    '''
    Checks to see if a space is available on the board
    '''

    return board[position] == ' '

##############################################
def full_board_check(board):

    '''
    Check to see if board is full
    '''

    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True

##############################################
def player_choice(board):

    '''
    Function that asks for the players next position
    '''

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))

    return position
    
##############################################
def replay():

    '''
    Function that asks if they want to play again
    '''

    choice = input('Play again? Enter Y or N: ').upper()

    return choice == 'Yes'

##############################################
print('Welcome to Noughts & Crosses')

while True:
    # Resetting the board
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will be going first')

    play_game = input('Ready to play? Y or N? ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    #Game play

    while game_on:  #Player 1's turn

        if turn == 'Player 1':

            display_board(the_board)  #Display the board

            position = player_choice(the_board) #Choosing a position

            place_marker(the_board,player1_marker,position) #Placing a marker on the position

            if win_check(the_board,player1_marker): #Check to see if they've won
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:  #Player 2's turn
            display_board(the_board)  #Display the board

            position = player_choice(the_board) #Choosing a position

            place_marker(the_board,player2_marker,position) #Placing a marker on the position

            if win_check(the_board,player2_marker): #Check to see if they've won
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on = False
                else:
                    turn = 'Player 1'



    if not replay():    # Break out of the loop if they don't want to play
        break













    
