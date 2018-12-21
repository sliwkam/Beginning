def reading_and_saving(filename):
    list_ = []
    with open(filename) as text:
        line = text.readline()
        while line:
            list_.append(int(line))
            line = text.readline()
    return list_


if __name__ == '__main__':
    table1 = reading_and_saving('one.txt')
    table2 = reading_and_saving('two.txt')
    table3 = [i for i in table1 if i in table2]
    print(table3)


# The program reads file, converts values into int type
# and adds to list. Then compares two lists and creates
# new list with repeated values.
