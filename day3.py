# IF ELSE

# Modulo operator (%): gives remainder eg : 10 % 2 == 0 , 15 % 2 == 1
number=int(input("Enter integer to check :"))
if number%2 == 0 :
    print("even integer")
else:
    print("odd integer")

# '=' used to assign value to a variable whereas' '==' used to check whether equals to or not

# Nested if else statements
print("Welcome to roller coaster")
height=int(input("Enter your height in cm ? "))
if height >=120 :

    print("You can ride")
    age=int(input("Enter your age :"))

    if age <= 12 :
        print(" Please pay 100 rupees ")

    elif age <= 18:
        print(" Please pay 120 rupees ")

    elif age <= 24 :
        print(" Please pay 140 rupees ")

    else:
        print(" Please pay 150 rupees ")

else:
    print("Sorry you can't ride")                                       # IndentationError



# Multiple if : all the conditions will be checked out and 3 executed if all 3 are true whereas in if-elif-else loop only 1 condition
print("Welcome to roller coaster")
height=int(input("Enter your height in cm ? "))
bill = 0
if height >=120 :

    print("You can ride")
    age=int(input("Enter your age :"))

    if age <= 12 :
        bill= 100
        print("Child tickets are  100 rupees ")
    elif age <= 20:
        bill = 120
        print("Teenager tickets are 120 rupees ")
    elif  45 <= age <=55 :
        print("You have a free ride on us")

    else:
        bill = 150
        print("Adult tickets are 150 rupees ")

    wants_photo=input("Do you want a photo ticket,type yes/ no")
    if wants_photo == "yes":
        bill += 50

    print(f"Your bill is : {bill} rupees ")

else:
    print("Sorry you can't ride")

# Logical operators : or and not
