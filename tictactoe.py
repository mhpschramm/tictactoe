__author__ = 'mhp'

import random # for AI's choice of fields

# initiate and fill the board


def print_pretty(board): # add pretty boarders
    print(" ")
    for row in range(0,3):
        print(board[row][0], "|", board[row][1], "|", board[row][2])
        if row < 2:
            print("-", "-", "-", "-", "-")
    print(" ")

def line_check(board):  # check if somebody has won, return True if so and winner1
    if board[0][0] == board[1][1] == board[2][2] or board[0][1] == board[1][1] == board[2][1] or board[0][2] == board[1][1] == board[2][0] or board[1][0] == board[1][1] == board[1][2]:  # check winning combinations of field 5
        return True
    elif board[0][0] == board[0][1] == board[0][2] or board[0][0] == board[1][0] == board[2][0]:  # check non-diagonals of field 1
        return True
    elif board[0][2] == board[1][2] == board[2][2] or board[2][0] == board[2][1] == board[2][2]:  # check non-diagonals of field 9
        return True
    else:
        return False

def choose_starter():  #Let the user decide who starts
    input_ok = False
    while input_ok is False:
        first = input("Do you want to start (else the computer will begin)? Choose 'y' or 'n'")
        if first not in ("y", "n"):
            print("Please enter only 'y' or 'n'")
        elif first == "y":
            first_flag = True
            input_ok = True
        else:
            first_flag = False
            input_ok = True
    return first_flag



def play():
    lets_play = True
    wins = 0
    losses = 0
    draws = 0
    while lets_play is True:
        fields = ["1","2","3","4","5","6","7","8","9"]
        board = [["1","2","3"],["4","5","6"],["7","8","9"]]
        intfields = list(range(1,10))
        first_flag = choose_starter()
        ct = 1
        print("Let's play Tic Tac Toe!")
        print_pretty(board)
        while ct < 10:
            if ct % 2 == 1 and first_flag is True or ct % 2 == 0 and first_flag is False:  # human plays if choice was yes and odd move or if choice was no and even move
                selection = input("Choose a field where you want to place an 'X'!")
                if selection not in fields:
                    print("Please only enter values from 1 to 9")
                else:
                    selection = int(selection)
                    row = (selection-1)//3
                    if board[row][selection-(row*3+1)] not in ("X", "O"):
                        board[row][selection-(row*3+1)] = "X"  # place your "X"
                        print("You placed an 'X' on field %s" % selection)
                        print_pretty(board)
                        ct += 1
                        intfields.remove(selection)
                    else:
                        print("Field %s is already occupied, choose another one" %selection)
            else:  # computer plays
                selection = random.choice(intfields)  # pure RNG, no AI
                intfields.remove(selection)  # remove choices already selected (so there are no trial and errors)
                row = (selection-1)//3
                board[row][selection-(row*3+1)] = "O"  # place computer's "O"
                print("Computer placed an 'O' on field %s" % selection)
                print_pretty(board)
                ct += 1
            won = line_check(board)
            if won is True or ct == 10 and won is False: # check if anybody has won already
                if won is True:
                    if ct % 2 == 1 and first_flag is True or ct % 2 == 0 and first_flag is False:
                        print("Too bad! The computer has won the game!")
                        losses += 1
                    else:
                        print("Congratulations! You have won the game!")
                        wins += 1
                    print("Your stats are: Wins: %d, Draws: %d, Losses: %d" % (wins, draws, losses))
                    input_ok = False
                    while input_ok is False:
                        again = input("Do you want to play once again?")
                        if again in ("y","n"):
                            input_ok = True
                            if again == "n":
                                lets_play = False
                                print("Okay, bye!")
                        else:
                            print("Come on! Only 'y' or 'n'!")
                    break
                else:
                    print("The game is drawn!")
                    draws += 1
                    print("Your stats are: Wins: %d, Draws: %d, Losses: %d" % (wins, draws, losses))
                    input_ok = False
                    while input_ok is False:
                        again = input("Do you want to play once again?")
                        if again in ("y","n"):
                            input_ok = True
                            if again == "n":
                                lets_play = False
                                print("Okay, bye!")
                        else:
                            print("Come on! Only 'y' or 'n'!")

play()
