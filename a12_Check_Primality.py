number = int(input("Enter a number: "))


def prem(number):
    divisors = []
    for i in range(1, number, 1):
        if number == 1:
            print("Number is not prime.")
        elif number%i == 0:
            divisors.append(i)
    if len(divisors) == 1:
        print("Number is prime.")
    else:
        print("Number is not prime.")

'''
Program checks the divisors of entered number and adds them to the new table. 
When this table has only 2 elements, it means that the entered number is prime.
'''
prem(number)


