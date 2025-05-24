# using flow chart programming
import random

from day7_hangman_art import stages         # no need for hangman_art.stages simply use stages

lives = 6
lst = ["apple","bamboo","camel","dance"]
random_word = random.choice(lst)

placeholder= ""
for i in range(len(random_word)):
    placeholder += "_"
print(placeholder)

# TODO-1 : using while loop to allow user to guess again .

game_over = False
correct_letters=[]

while not game_over:                                   # NOT FALSE = TRUE
    guess= input("Guess a letter :").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

     # TODO-2: CHANGE THE FOR LOOP SO TO KEEP PREVIOUS CORRECT LETTERS IN DISPLAY.
     # if lives becomes zero then gameover

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

# LIST OUTSIDE SO THAT EVERYTIME THE WHILE LOOP REPEATS IT DOES NOT BECOME EMPTY AS GIVEN IN CONDITION
    print(display)

    if guess not in random_word:
        lives-=1
        print(f"You guessed {guess} , that's not in the word. You lose a life. {lives} Lives remaining.")
        if lives == 0 :
            game_over= True
            print(f"***************************** You lose ! . Correct word was {random_word}*********************************")

    if "_" not in display:
        game_over= True
        print("*********************************** You win ! **************************************")

    print(stages[-lives])   # or in variable stages add hangman images in opp order





#space = len(random_word)                 # integer already
# placeholder= "_"*space
# print(placeholder)