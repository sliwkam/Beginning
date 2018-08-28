# library use
import random
# creating random list
a = random.sample(range(100), 15)
b = random.sample(range(100), 10)
c = []
# checking common words
for i in b:
    if i in a:
        c.append(i)
print(c)
