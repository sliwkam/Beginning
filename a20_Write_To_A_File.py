def form():
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    age = input('Enter your age: ')
    address = input('Enter your address: ')
    data = name + ' | ' + surname + ' | ' + age + ' | ' + address
    return data


if __name__ == "__main__":
    with open('save_file.txt', 'w') as open_file:
        open_file.write(form())
