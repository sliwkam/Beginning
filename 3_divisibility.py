# entering data
number = float(input("Please enter your chosen 'num' number:"))
check = float(input("Please enter your chosen 'check' number:"))
# checking divisibility by 2
if number%2==0:
    print("The number is divided by 2 without rest.")
else:
    print("The number is divided by 2 with rest.")
# checking if the 'num' is a multiple of 4
if number%4==0:
    print("The number is a multiple of 4.")
# checking if the 'num' is divisible by 'check'
if number%check==0:
    print("The 'num' is divisible by 'check'.")
else:
    print("The 'num' isn't divisible by 'check'.")
