logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add (num1 , num2):
    return num1 + num2
def subtract (num1 , num2):
    return num1-num2
def multiply (num1, num2):
    return num1*num2
def divide (num1,num2) :
    return num1 / num2

# define functions before using them on top
operation_dictionary = {"+" : add, "-" : subtract , "*" : multiply , "/" : divide}

def calculator():
    print(logo)

    should_accumulate = True

    num1 = float (input("enter first number : "))     # so that it doesnt overwrite the if choice block ccode value for num1
    while should_accumulate :

        for key in operation_dictionary:
            print(key)
        operator = input("enter operator : ")
        num2 = float (input("enter second number : "))
        answer = operation_dictionary[operator](num1,num2)
        print(f"{num1} {operator} {num2} = { answer } " )

        choice = (input(f"enter 'y' to continue to calculating with {answer} or type 'n' to start a new calculation :").
                  lower())
        if choice == "y":
            num1 = answer

        else :
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
