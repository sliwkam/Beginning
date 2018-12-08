import random


def password_generator(long1):
    # This function creates random password with using the Ascii Table.
        password = []
        for i in range(0, long1 - 1, 1):
            number = random.randint(32, 126)
            sign = chr(number)
            password.append(sign)
        password = "".join(password)
        return password


def password_chosen(long1):
    # Creates a password based on the entered words.
    words = ['afternoon', 'man', 'hesitant', 'quarrelsome', 'tent', 'bike', 'escape', 'kaput', 'cook', 'skinny', 'ang']
    password = ""
    while len(password) < long1:
        i = random.randint(0, len(words) - 1)
        password = password + words[i]
    password = "".join(password)
    return password


def password_change1(long1):
    # Gives the password a certain length, shortening it from the beginning.
    new_password = list(password_chosen(long1))
    while len(new_password) != long1:
        del new_password[0]
    return ''.join(new_password)


def password_change2(long1):
    # Gives the password a certain length, shortening it in random point.
    new_password = list(password_chosen(long1))
    while len(new_password) != long1:
        i = random.randint(0, long1 - 1)
        del new_password[i]
    return ''.join(new_password)


def password_upper(long1):
    # Changes to upper case.
    new_password = str(password_change2(long1))
    number = int(long1 * 0.4)
    i = 0
    while i != number:
        x = random.randint(0, long1 - 1)
        y = new_password[x]
        y = y.upper()
        new_password = new_password.replace(new_password[x], y)
        i += 1
    return new_password


def password_numbers(long1):
    # Turns letters into numbers.
    new_password = password_upper(long1)
    number = int(long1 * 0.4)
    i = 0
    while i != number:
        x = random.randint(0, long1 - 1)
        z = str(random.randint(0, 9))
        new_password = new_password.replace(new_password[x], z)
        i += 1
    return new_password


def main():
    # The main function that generates a password of the given type up to the moment of interruption.
    answer = 'YES'
    while answer != 'NO':
        strength = int(input("How strong a password should be?(1-5): "))
        long = int(input("How many signs password should contain?: "))
        if strength == 1:
            print('Your new password:  ' + str(password_change1(long)))
        elif strength == 2:
            print('Your new password:  ' + str(password_change2(long)))
        elif strength == 3:
            print('Your new password:  ' + str(password_upper(long)))
        elif strength == 4:
            print('Your new password:  ' + str(password_numbers(long)))
        elif strength == 5:
            print('Your new password:  ' + str(password_generator(long)))
        answer = input('Do you want another password?(YES/NO): ')
        answer = answer.upper()


main()
