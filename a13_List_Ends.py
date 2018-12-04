lis = [5, 10, 15, 25]
numbers = [3, 5, 6, 7, 8, 9, 1000]


def first_last(tab):

    # Program adds the first and last number of the used table to the new table

    new = []
    z = len(tab) - 1
    y = tab[0]
    x = tab[z]
    new.append(y)
    new.append(x)
    print(new)


first_last(numbers)
