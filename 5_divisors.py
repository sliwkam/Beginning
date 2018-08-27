# entering the number by the user
number = int(input("Enter your chosen number:"))
divisors = []
# determining the divisors of the number
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

    print(str(divisors) + " are a divisors of your number.")
