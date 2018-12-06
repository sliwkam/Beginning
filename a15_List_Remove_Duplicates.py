def duplicates(table):
        new = []
        for i in table:
            if i not in new:
                new.append(i)
        print(new)


def second(table):
        table = set(table)
        print(table)


name = [6, 4, 2, 7, 9, 7, 4, 5, 7]
second(name)
duplicates(name)
