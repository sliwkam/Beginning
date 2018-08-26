# importing the date
import datetime
time = datetime.datetime.now()

# query for name and age
print("Enter your name:")
name = input()
print("Enter your age:")
age = input()

# change of the data type
iage = int(age)
high = 100 - iage
print("Enter a number:")
n = input()

# the end of program
text = "You will be 100 years old in:" +" "+ str(int(str(time.strftime("%Y")))+high)

print(text*int(n))
