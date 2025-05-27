#python is case:sensitive remember else SyntaxError    , generally hyphen : is used just a typo


#print("hello world .." )                                               # used to comment

#STRING MANIPULATION


#print("hello world!\nhello world?\n hello world with space")    #\n = new line character


# string concatenation

#print("hello"+"bhanu")
#print("hello" + "bhanu")
#print("hello"+" "+"bhanu")
#or use print("hello "+"bhanu")

# IndentaionError: unexpected indent if space before print

# pep gives us hint here for code betterment




#print("hello"+input("What is your name?")+"!")
# once input given and enter clicked what's entered is going to replace input function

#Variable

#a = 12345
#name = input("what is your name?")
#print("hello",    name,a)
#print(len(name))
#print(len(a))       TypeError : object of type 'int' has no len()

# don't use spaces between words instead user_name
# don't start with numbers
# don't use special words like print or input
# to make program readable use  better variable name




# if wrong variable name used in program then NameError: name 'nama' not defined


#DAY 1 PROJECT BAND NAME GENERATOR

print("Welcome to the Band Name Generator ")
city_name= input("What's your city name?\n")
pet_name=input("What's your pet name?\n")
print("Your band name could be :",city_name,pet_name)
