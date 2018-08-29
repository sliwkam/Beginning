# entering a sentence
string = input("Enter your chosen sentence: ")
n_string = string[::-1]
print(n_string.lower())
# change the size of the letter
sy = n_string.lower()
sx = string.lower()
# removing the space
x = sx.replace(" ", "")
y = sy.replace(" ", "")
if x == y:
    print("Entered sentence is a palindrome.")
else:
    print("Entered sentence isn't a palindrome.")
