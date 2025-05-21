my_country = "India"
my_DOB = 23_03_2006       # ZeroDivisionError: division by zero

# head and tail game
import random
lst=["head","tail"]
print(random.choice(lst))

#method 2
number=random.randint(0,1)
if number==0:
    print("head")
else:
    print("tail")

#method 3
lst=["head","tail"]
random_index=random.randint(0,1)
print(lst[random_index])


