# this program guesses the number chosen by the user


def binary_looking(table):
    left = 0
    count = 0
    right = len(table) - 1
    while left <= right:
        m = int((left + right)/2)
        count += 1
        print('Is ' + str(table[m]) + ' your number?: ')
        result = input()
        result = result.upper()
        while result != 'EXIT' and result != 'YES' and result != 'NO':
            print("Only 'yes', 'no' or 'exit'. ")
            result = input()
            result = result.upper()
        if result == 'EXIT':
            print('Goodbye. Thanks for the game!')
            break
        elif result == 'YES':
            print('Your number was found in ' + str(count) + ' moves.')
            break
        elif result == 'NO':
            print('My choice it too small or to big?')
            sign = input()
            sign = sign.upper()
            if sign == 'SMALL':
                left = m + 1
            elif sign == 'BIG':
                right = m - 1


if __name__ == '__main__':
    tab = []
    print('This program guesses the number you chose from 1 to 100.')
    print('Please, choose your number. When you will be ready please, write "START". If you want to terminate this game')
    print('please write "EXIT". You can end this game in every moment by writing this comment. ')
    comment = input()
    comment = comment.upper()
    for i in range(0, 100):
        tab.append(i + 1)
    while comment != 'EXIT' or comment != 'START':
        if comment == 'START':
            binary_looking(tab)
            break
        elif comment == 'EXIT':
            print('Goodbye. Thanks for the game!')
            break
        print('You want to start or exit game?:')
        comment = input()
        comment = comment.upper()
