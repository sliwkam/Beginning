def search(numbers_list):
    # function checks (until the value is found) whether entered the number is included in the list.
    value = False
    while value is False:
        number = int(input('Enter your number: '))
        for i in numbers_list:
            if i == number:
                value = True
                break
        if value is True:
            print('Your number is in the list.')
        else:
            print("Your number isn't in the list.")


def binary_search(numbers_list, number):
    # function checks whether entered the number is included in the list in a binary way.
    # It works by repeatedly dividing in half the portion of the list that could contain the item, until you've
    # narrowed down the possible locations to just one
    start = 0
    end = len(numbers_list) - 1
    index = 0
    while index == 0:
        middle = int((end - start)/2)
        if middle < start or middle > end or middle < 0:
            print("Your number isn't in the list.")
            index = 1
        middle_value = numbers_list[middle]
        if middle_value == number:
            print("Your number is in the list.")
            index = 1
        elif middle_value > number:
            end = middle
        else:
            start = middle


if __name__ == '__main__':
    numbers_lis = [0, 1, 2, 3, 4, 5, 13, 24, 87, 134, 256]
    num = int(input('Enter your number: '))
    binary_search(numbers_lis, num)
    search(numbers_lis)
