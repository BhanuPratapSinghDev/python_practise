# Local scope = variables declared inside function have local scope . They are seen only by the other code inside the
# same block of code
# Global scope = variables declared outside function have global scope . They are available outside and inside both
# These scopes are applicable to alll even functions too
# apples = 1

# def calculate():
#     def add_apples ():
#         apples = 2
#         print(f"Apples inside function are {apples}")
#
# add_apples()
# print(f"Apples outside function are {apples}")

# ANSWER = NameError: name 'add_apples' is not defined . As add_apples() now has a local scope within the calculate
# function hence when we call it from outside the function can't see inside the function . so to call add_apples() we
# need to be inside the walls of calculate function.

apples = 1
def calculate():
    def add_apples ():
        apples = 2
        print(f"Apples inside function are {apples}")

    add_apples()
calculate()
print(f"Apples outside function are {apples}")


# Block  scope = unlike other programming languages python does not have a block scope
# game_level = 3
# enemies = ["Zombie","Ghost"]
#
# if game_level < 5 :
#     new_enemy = enemies[0]
#
# print(new_enemy)                   # valid cose with output = Zombie
#                                    # as blocks like if , while , for with ':' colon and indentation they don't count as
#                                    # creating a local scope

#
# game_level = 3
#
# deenemies = ["Zombie","Ghost"]
# f create_enemy():
#     if game_level < 5 :
#         new_enemy = enemies[0]
#
# print(new_enemy)                   # within function local scope so new_enemy is available withing the function
                                     # as blocks like if , while , for with ':' colon and indentation they don't count as
                                     # creating a local scope . They are given function scope is they are within a
                                     # function or global scope if they aren't .
                                     # output = NameError: name 'new_enemy' is not defined

game_level = 3
enemies = ["Zombie","Ghost"]

def create_enemy():
    new_enemy = ""                   # to  get rid of warning it's just a warning that it might be an issue , as if
                                     # game_level not less than 5 then var new_enemy is not
                                     # created then we are printing nothing . So we can outside of if, while,for block
                                     # we can declare that variable and initialise it. S
    if game_level < 5 :
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()