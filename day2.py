# Primitive data types : Strings,integers,floats,booleans


# Subscripting : pulling out a particular element from a string
print("Hello"[0])
print("Hello"[-1])

# String
print("12"+"34")

# Integer =whole no + or -
print(12+34)

# Large Integer (instead of commas )
print(123_456_789)

# Float = Floating point no i.e. containing decimal
print(3.14)

# Boolean
print(True)
print(False)        # "False" is a string

# Len function used for sequence(string,bytes, tuple,list) or a collection ( dict,set , frozen set)

# Type function
print(type("hello"))
print(type(12345))
print(type(1234.5))
print(type(False))

# Type conversion , Type casting
print(int("1234")+int("4567"))
#print(int("abcd")+int("4567"))      #ValueError: invalid literal for int() with base 10: 'abcd'
#print(int("abcd"))                   # ValueError: invalid literal for int() with base 10: 'abcd'
print(bool(0))
print(bool(1))
#print("Number of letters in your name: "+str( len(input("Enter your name"))))

# Mathematical operators
print(12+34,12-34,1*2,2**4)

# Division always gives a float ( implicit typecasting)
print(2/2)
# Floor division gives an integer unless float used
print(25//2)
print(2.5//2)

# PEMDAS = Parentheses,Exponents,Multiplication/Division,Addition/Subtraction
# b/w multiplication and division the one to the left prioritised lly add and sub
print(2 * 2 + 2 / 2 - 2)
print(3 * 3 + 3 / 3 -3)
print(3 * (3 + 3 )/ 3 -3)  # add , mult, div,sub

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))

# Round function , syntax : round ( number, ndigits) , ndigits is the number of decimal places to round off to
print(round(bmi))
print(round(bmi,2))

# Flooring a number
print(int(3.14))

# Assignment operator ; to accumulate results of our calculations , +=, -= , *= , /=
score = 0
score += 1
print(score)

# F-strings : to insert a variable or an expression into a string ( converts into str itself)
print("Your score is", score)
print("Your score is " + str(score))

score = 10
height = 6.8
is_winning = True
print(f"Your score is = {score} . your height is = {height}. you are winning ={is_winning}")
