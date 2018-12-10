import random


def cows_and_bulls(number, rand_number):
    # counts number of 'cows'
    count = 0
    for i in range(0, 4):
        if number[i] == rand_number[i]:
            count += 1
    return count


if __name__ == "__main__":
    rand_num = str(random.randint(1000, 9999))
    su = 1
    attempts = 0
    # explanation
    print("Let's play a game of Cowbull!")
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")
    while su != 0:
        num = input("Enter your guess: ")
        if num == "exit":
            break
        cou = cows_and_bulls(num, rand_num)
        su = 4 - cou
        print('You have:     ' + str(su)+' cows     '+str(cou) + ' bulls.')
        # counts movements
        attempts += 1
    if num == 'exit':
        print('Game was terminated.')
    else:
        print('You win in ' + str(attempts) + ' moves.')
