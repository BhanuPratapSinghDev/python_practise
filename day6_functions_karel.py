# Practise on Reeborg's world ( similar to karel which has a robot in a grid based world)

######################   Functions : just a wrapper name for a block of code helps to save time   #########

# Defining a function (parenthesis differentiate variable from function )
# for indentation , 4 spaces generally or a tab
#    print("Hello")
#    print("Bye")
# my_function()       # calling a function

# While loop (more dangerous than for loop)
# 1) while something_is_true :
# 2)   do somthing repeatedly           1 -> 2-> 1-> 2-> 1 ........so on

# functions that allows for inputs :

def greet(name):
    print("Good morning. ", end = "   ") # by default end is \n
    print(f"How are you {name} ?", end ="")
    print("Have you done your breakfast? ")
greet("Bhanu")

# name is Parameter and Bhanu is Argument

###########################    Function with more than one inputs     ########################################

# NAME , LOCATION ARE POSITIONAL ARGUMENTS :
def greetings(name,location):
    print(f"Hello {name}\nHow is the whether there in {location}")
greetings("Bhanu",1234)

# KEYWORD ARGUMENTS :
def greetings(name,location):
    print(f"Hello {name}\nHow is the whether there in {location}")
greetings(name="Bhanu",location=1234)
greetings(location=1234,name="Bhanu",)    # now order doesn't matter
