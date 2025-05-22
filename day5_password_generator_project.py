import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome o password generator")
nb_letters= int( input("Enter total letters  you need?"))
nb_numbers= int(input("Enter total numbers  you need?"))
nb_symbols= int( input("Enter total symbols  you need?"))

# print(random.sample(letters,nb_letters))
# print(random.sample(numbers,nb_numbers))
# print( random.sample(symbols,nb_symbols))
letters_selected = random.sample(letters,nb_letters)
numbers_selected = random.sample(numbers,nb_numbers)
symbols_selected = random.sample(symbols,nb_symbols)

selected= letters_selected + numbers_selected + symbols_selected
print(selected)
random.shuffle(selected)                      #mutable sequence ,just shuffles in place not returns itself
print(selected)
print("Your password is : ",end='')
for elements in selected:
      print(elements,end="")

# Method 2
# password=""
# for element in selected:
#     password += element
# print(password)
