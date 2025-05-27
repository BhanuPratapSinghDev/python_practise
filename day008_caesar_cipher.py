logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
# Method 1
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caiser (text, shift , direction):
    output_code = ""
    if direction =="decode":
         shift *=-1
    for letter in text :
        if letter not in alphabet :
            output_code += letter
        else:
            index = alphabet.index(letter) + shift
            index = index % len(alphabet)
            output_code += alphabet[index]
    print(f"{direction}d code is {output_code}")

should_continue = True
while should_continue :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caiser ( text , shift , direction)
    restart=input("Type 'yes' to continue else 'no' \n").lower()
    if restart == 'no':
        should_continue= False
        print("Goodbye")




# **********************************************************************************************************************
#                                             Method 2 (lenthy code)
# print(logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def encrypt ( text ,shift ):
#     encrypt_code = ""
#     for letter in text:
#         index = alphabet.index(letter) + shift
#         index = index % len(alphabet) # what if tried to shift z by 8 ? That will go beyond hence need to use
#         # index %= len(alphabet)      # modulo to get remainder eg . 4 % 25 = 4 , 34 % 25 = 9
#                                       # for eg z shift by 8. index = 26 + 8= 34 . 34 % 26 = 8
#                                       # when divided firstly 1 loop around alphabets doe now 8 more to cover
#
#
#
#         encrypt_code += alphabet[index]
#     print(f"Encrypted code is {encrypt_code}")
#
# def decrypt( text , shift) :
#     decrypt_code=""
#     for letter in text:
#         index =  alphabet.index(letter) - shift
#         index = index % len(alphabet)                           # so to remain in the range of 26 alphabets
#         decrypt_code += alphabet[index]
#
#     print(f"Decrypted code is {decrypt_code}")
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# if direction == "encode" :
#     encrypt(text,shift)
# if direction == "decode" :
#     decrypt( text , shift )
