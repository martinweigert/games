

a = """

#########################################
                GAME TIME
##########################################

"""

print(a)


while True:
    print("Which game do you want to play?")
    game_choice = input("Type 't' for Tic Tac To and 'c' for Connect Four. ")
    if game_choice == "t":
        import tictactoe.py
    if game_choice == "c":
        import connect_four.py
    else:
        print("That's not an option.")
