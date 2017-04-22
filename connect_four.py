import sys
import re

def play_again():
    global player1_count
    global player2_count
    user_input = input("Do you want to play again? Type 'y' for yes or any key for no. ")
    if user_input.startswith("y"):
        for i in range(6):
            for n in range(7):
                game[i][n] = 0
        player1_count = 0
        player2_count = 0
    else:
        print("Ok thank you for playing.")
        sys.exit()


def print_game():
    border = (7*[" ---"])
    row1 = ["| ",str(game[0][0]), " | ",str(game[0][1]), " | ",str(game[0][2]), " | ",str(game[0][3]), " | ",str(game[0][4]), " | ",str(game[0][5]), " | ",str(game[0][6]), " | "]
    row2 = ["| ",str(game[1][0]), " | ",str(game[1][1]), " | ",str(game[1][2]), " | ",str(game[1][3]), " | ",str(game[1][4]), " | ",str(game[1][5]), " | ",str(game[1][6]), " | "]
    row3 = ["| ",str(game[2][0]), " | ",str(game[2][1]), " | ",str(game[2][2]), " | ",str(game[2][3]), " | ",str(game[2][4]), " | ",str(game[2][5]), " | ",str(game[2][6]), " | "]
    row4 = ["| ",str(game[3][0]), " | ",str(game[3][1]), " | ",str(game[3][2]), " | ",str(game[3][3]), " | ",str(game[3][4]), " | ",str(game[3][5]), " | ",str(game[3][6]), " | "]
    row5 = ["| ",str(game[4][0]), " | ",str(game[4][1]), " | ",str(game[4][2]), " | ",str(game[4][3]), " | ",str(game[4][4]), " | ",str(game[4][5]), " | ",str(game[4][6]), " | "]
    row6 = ["| ",str(game[5][0]), " | ",str(game[5][1]), " | ",str(game[5][2]), " | ",str(game[5][3]), " | ",str(game[5][4]), " | ",str(game[5][5]), " | ",str(game[5][6]), " | "]
    a = [row1, row2, row3, row4, row5, row6]
    print("".join(border))
    for i in range(6):
        print("".join(a[i]))
        print("".join(border))


def check_winner():
    winner = ""
    for row in range(6):
        for column in range(7):
            if game[row][column] == "R":
                if game[row][column+1] == "R" and game[row][column+2] == "R" and game[row][column+3] == "R":
                    winner = "R"
                elif game[row+1][column] == "R" and game[row+2][column] == "R" and game[row+3][column] == "R":
                    winner = "R"
                elif game[row-1][column+1] == "R" and game[row-2][column+2] == "R" and game[row-3][column+3] == "R":
                    winner = "R"
                elif game[row-1][column-1] == "R" and game[row-2][column-2] == "R" and game[row-3][column-3] == "R":
                    winner = "R"
            if game[row][column] == "B":
                if game[row][column+1] == "B" and game[row][column+2] == "B" and game[row][column+3] == "B":
                    winner = "B"
                elif game[row+1][column] == "B" and game[row+2][column] == "B" and game[row+3][column] == "B":
                    winner = "B"
                elif game[row-1][column+1] == "B" and game[row-2][column+2] == "B" and game[row-3][column+3] == "B":
                    winner = "B"
                elif game[row-1][column-1] == "B" and game[row-2][column-2] == "B" and game[row-3][column-3] == "B":
                    winner = "B"
    if winner == "R":
        print_game()
        print("Player 1 won, congratulations.")
        play_again()
    elif winner == "B":
        print_game()
        print("Player 2 won, congratulations.")
        play_again()


def column_full(player):
    global player1_count
    global player2_count
    print("All fields in this column are occupied. Please choose another columm.")
    if player == "Player 1":
        player1_count -= 1
    else:
        player2_count -= 1



def make_move(column, player_start):
    global player1_count
    global player2_count
    if player_start == "Player 1":
        player = "R"
    else:
        player = "B"
    column -= 1
    if game[0][column] != 0:
        column_full(player_start)
    for i in range(5, -1, -1):
        if game[i][column] == 0:
            game[i][column] = player
            break
    check_winner()
    if 0 not in game[0] and 0 not in game[1] and 0 not in game[2] and 0 not in game[3] and 0 not in game[4] and 0 not in game[5]:
        print_game()
        print("The game ended without a winner.")
        play_again()


game = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
###10 instead of 7 values per list so that the check_winner function won't throw an error because list out of range


start = """

#########################################
             CONNECT FOUR
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
            column = int(input("%s, choose a column for your checker (1-7): " % player))
            if not (1 <= int(column) <= 7):
                raise ValueError()
        except ValueError:
            print("Please choose a number between 1 and 7.")
        else:
            break
    make_move(column, player)
