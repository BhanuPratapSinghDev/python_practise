# def is_prime(num):
#     if num == 0 or num == 1:
#         print("Not prime")
#     else:
#         for i in range ( 2,num ):
#             if num % i == 0 :
#                 print("Not prime")
#
#         print("Prime number")
# num = int(input("enter number : "))
# is_prime(num)

# Output:
# enter number : 12
# Not prime
# Not prime
# Not prime
# Not prime
# Prime number

def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range ( 2,num ):
            if num % i == 0 :
                return False

        return True
num = int(input("enter number : "))
print(is_prime(num))

# enter number : 12
# output = False

# once return is called it won't go further in the function i.e. will terminate the function there