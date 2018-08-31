# use of the 'time' library
import time
n_end = 0
points_x = 0
points_y = 0
# operation of the program until the user stops
while n_end != 'STOP':
    player_1 = input("(Player 1) Enter your chosen sign: ")
    time.sleep(1)
    player_2 = input("(Player 2) Enter your chosen sign: ")
    x = player_1.upper()
    y = player_2.upper()
# checking terms
    if x == 'SCISSORS' and y == 'PAPER':
        print("Player 1 wins!")
        points_x = points_x + 1
        end = input("If you don't want to play again, please enter 'STOP'")
        n_end = end.upper()
    elif x == 'PAPER' and y == 'SCISSORS':
        print("Player 2 wins!")
        points_y = points_y + 1
        end = input("If you don't want to play again, please enter 'STOP'")
        n_end = end.upper()
    elif x == y:
        print("DRAW!")
        end = input("If you don't want to play again, please enter 'STOP'")
        n_end = end.upper()
    elif x == 'ROCK' and y == 'PAPER':
        print("Player 2 wins!")
        points_y = points_y + 1
        end = input("If you don't want to play again, please enter 'STOP'")
        n_end = end.upper()
    elif x == 'PAPER' and y == 'ROCK':
        print("Player 1 wins!")
        points_x = points_x + 1
        end = input("If you don't want to play again, please enter 'STOP'")
        n_end = end.upper()
    elif x == 'ROCK' and y == 'SCISSORS':
        print("Player 1 wins!")
        points_x = points_x + 1
        end = input("If you don't want to play again, please enter 'STOP'")
        n_end = end.upper()
    elif x == 'SCISSORS' and y == 'ROCK':
        print("Player 2 wins!")
        points_y = points_y + 1
        end = input("If you don't want to play again, please enter 'STOP'")
        n_end = end.upper()
# showing the final winner and total scores
if points_y > points_x:
    print("The game wins player 2! CONGRATULATIONS!!")
elif points_y < points_x:
    print("The game wins player 1! CONGRATULATIONS!!")
else:
    print("IT IS DRAW!")
print("(SCORE) Player 1: " + str(points_x) + "  Player 2: " + str(points_y))
