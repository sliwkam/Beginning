# Program prints back to the user a string, except with the words in backwards order.
def inversion(table):
    result = table.split()
    new = []
    x = len(result)
    for i in range(x - 1, -1, -1):
        new.append(result[i])
    new = " ".join(new)
    print(new)


string = 'I am a student looking for a job'
inversion(string)
