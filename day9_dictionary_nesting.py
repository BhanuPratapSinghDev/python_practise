# Dictionary = { key : value} eg { "name" : "bhanu" , "age" : 19}
from fractions import Fraction

programming_dictionary= {
    "Bug":"defect in the program causing it to behave in an undesirable manner ", # to make it clear we write with 1 indent
    "Functions":"Piece of code that you can easily call over and over again",
    1234:"Integers"}
# What if we don't use " " around Bug ?
# NameError : name "Bug" is not defined . As it will think of it as an variable defined somewhere.

print(programming_dictionary["Bug"])
# print(programming_dictionary["Bite"])           # KeyError: 'Bite'
print(programming_dictionary[1234] )              # Integers

programming_dictionary["loop"] = "Action of doing something again  and again"
print(programming_dictionary)

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary )                   # output =  {}

# edit an item in dictionary
programming_dictionary["Bug"] = "Value changed"   # if it doesn't find the key then it will create a new key-value pair
print(programming_dictionary)                      # else it will rewrite the original value

# looping through a dictionary
for thing in programming_dictionary:
    print(thing)                                    # output = Bug
                                                    #          Functions
                                                    #          1234
                                                    #          loop
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])              # Bug
                                                    # Value changed
                                                    # Functions
                                                    # Piece of code that you can easily call over and over again
                                                    # 1234
                                                    # Integers
                                                    # loop
                                                    # Action of doing something again  and again
# Nesting Lists and Dictionaries
# eg : { key :[list], key2 :{dict} }
capitals = {
    "India" : "Delhi",
    "France": "Paris"
}
# travel_log = {
#     "France":"Paris","Lille","Dj"
# }                                                 # not possible as a key can have only one value
travel_log = {
    "France": ["Paris","Lille","Dj" ]

}
print( travel_log ["France"])                       # ['Paris', 'Lille', 'Dj']
print( travel_log ["France"] [1] )                  # Lille

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

travel_log2 = {
    "France": {"Paris":8,"Lille":7,"Dj" :[1,2,3,4]}
}
print(travel_log2["France"])                        # {'Paris': 8, 'Lille': 7, 'Dj': [1, 2, 3, 4]}
print(travel_log2["France"]["Dj"][1])               # 2

# project in the next
# file
