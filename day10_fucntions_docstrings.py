# functions with outputs:
def my_function () :
    result = 3 * 2
    return result                                 #  after return everything is going to replace where the function
                                                  # was called

output = my_function()
print( output )

def format_name (f_name , l_name):
    if f_name == "" or l_name == "":
        return None                                # return tells computer that it is the end of the function and now return
                                              #  from the function ( hence used to terminate the function)
                                              # output = None

    first = f_name.title()                            # Bhanu Pratap
    last = l_name.title()
    # print(f"{first} {last}")
    return f"{first} {last}"

formatted_string = format_name( input ("enter first name: "), input ("enter last name : "))
print(formatted_string)

def function1 (text):
    return text + text
def function2 (text):
    return text.title()
output = function2( function1("hello") )
print(output)                                  # Hellohello

def function3 (text):
    return text + text
    # print("Bye")                            # print will not work as return tells computer that it is the end of the
                                              # function and now return from the function

print (function3("hello"))

# Docstrings : it tells us about the function and goes as the first line after the declaration in b/w 3 quotation marks

def function4( num1,num2):
     """ Takes 2 numbers and adds them
      afterward returning via return"""
     result = num1+num2
     return result
print(function4(4,4))

# to store a function in a variable don't use parenthesis
fav_function = function4
print(fav_function(5,5))