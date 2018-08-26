li = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 0
li2 = []
number = int(input("Enter your chosen number:"))
quantity = int(len(li))
print(quantity)
# checking if the argument is greater than the number entered and adding to the new list
for i in li:
    if i < number:
        li2.append(i)
print(li2)
