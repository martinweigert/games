#kind of a milestone for me, built completely on my own.
#task source: http://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

import sys

def play_again():
    global player1_count
    global player2_count
    user_input = input("Do you want to play again? Type 'y' for yes or any key for no. ")
    if user_input.startswith("y"):
        for i in range(3):
            for n in range(3):
                game[i][n] = 0
        player1_count = 0
        player2_count = 0
    else:
        print("Ok thank you for playing.")
        sys.exit()

def field_occupied(player):
    global player1_count
    global player2_count
    print("This field is already occupied. Please choose another one.")
    if player == "Player 1":
        player1_count -= 1
    else:
        player2_count -= 1

def check_winner():
    winner = ""
    if game[0][0] == game[0][1] and game[0][0] == game[0][2]:
            winner = game[0][0]
    elif game[0][0] == game[1][0] and game[0][0] == game[2][0]:
            winner = game[0][0]
    elif game[2][0] == game[2][1] and game[2][0] == game[2][2]:
            winner = game[2][0]
    elif game[0][2] == game[1][2] and game[0][2] == game[2][2]:
            winner = game[0][2]
    elif game[1][0] == game[1][1] and game[1][0] == game[1][2]:
            winner = game[1][0]
    elif game[0][0] == game[1][1] and game[0][0] == game[2][2]:
            winner = game[0][0]
    if winner == "x":
        print_game()
        print("Player 1 won, congratulations.")
        play_again()
    elif winner == "o":
        print_game()
        print("Player 2 won, congratulations.")
        play_again()


def make_move(move_stripped, player_start):
    global player1_count
    global player2_count
    if player_start == "Player 1":
        player = "x"
    else:
        player = "o"
    i = int(move_stripped[0])-1
    m = int(move_stripped[1])-1
    if game[i][m] != 0:
        field_occupied(player_start)
    else:
        game[i][m] = player
    check_winner()
    if 0 not in game[0] and 0 not in game[1] and 0 not in game[2]:
        print_game()
        print("The game ended without a winner.")
        play_again()

def print_game():
    border = (3*[" ---"])
    row1 = ["| ",str(game[0][0]), " | ",str(game[0][1]), " | ",str(game[0][2]), " |"]
    row2 = ["| ",str(game[1][0]), " | ",str(game[1][1]), " | ",str(game[1][2]), " |"]
    row3 = ["| ",str(game[2][0]), " | ",str(game[2][1]), " | ",str(game[2][2]), " |"]
    a = [row1, row2, row3]
    print("".join(border))
    for i in range(3):
        print("".join(a[i]))
        print("".join(border))

game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
start = """

#########################################
             TIC TAC TOE
##########################################

"""
print(start)



player1_count = 0
player2_count = 0



while True:
    if player1_count == player2_count:
        player = "Player 1"
        player1_count += 1
    elif player1_count > player2_count:
        player = "Player 2"
        player2_count += 1
    print_game()
    while True:
        try:
            move = input("%s, type your move (format 'row, col', e.g. '1, 2'): " % player)
            move_splitted = move.split(",")
            move_stripped = [x.strip(' ') for x in move_splitted]
            if not (1 <= int(move_stripped[0]) <= 3):
                raise ValueError()
            if not (1 <= int(move_stripped[1]) <= 3):
                raise ValueError()
        except ValueError:
            print("Please choose two numbers between 1 and 3, seperated by a comma.")
        else:
            break
    make_move(move_stripped, player)






'''if int(move_stripped[0]) < 4 and int(move_stripped[1]) < 4:
        make_move(move_stripped, player)
    else:
        print("Please choose a number between 1 and 3")
        if player == "Player 1":
            player1_count -= 1
        else:
            player2_count -= 1'''
