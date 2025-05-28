import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_cards():
    """ returns a random card from the deck """
    cards =  [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score( cards):
    """takes a list of cards and returns the total """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21 :   # 11 i.e. Ace can work as 1 and 11 both as per need . if greater than 21 then
        cards.remove(11)                   # it becomes 1 and if less han 21 then becomes 11
        cards.append(1)
    return sum(cards)                      # cards need to be an iterable to work inside sum

def compare (u_score, c_score):   # Shadows name 'computer_score' from outer scope : warning
    if u_score == c_score :      # so need to use different name inside
        return "Draw"
    elif c_score == 0 :
        return "user lost . computer has a blackjack "
    elif u_score == 0 :
        return "computer lost . user has a blakjack "
    elif u_score > 21 :
        return "user lost as you went over "
    elif c_score > 21 :
        return "computer lost as it went over"
    elif u_score > c_score :
        return "user win"
    elif c_score > u_score:
        return "computer win"
    else :
        return " You lose"

def play_games():
    print(logo)
    user_cards = []
    computer_cards = []

    user_score = -1                            # so that if no values gets assigned it doesnt become undefined creating a
    computer_score = -1                        # issue . Also assigning a value will help in debugging
    game_over = False

    for i in range(2):
        user_cards.append(deal_cards())          # += used in strings not in lists as it works as extend hence needs iterable
        computer_cards.append(deal_cards())      # whereas we are adding single element

    while not game_over :
        user_score = calculate_score( user_cards )
        computer_score = calculate_score( computer_cards )

        print(f"your cards are {user_cards} , current score = {user_score}")
        print(f"computer's card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
             game_over = True
        else:
            choice = input("enter 'y' to get another card , type 'n'  to pass : ")
            if choice == "y" :
                user_cards.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score( computer_cards )

    print(f"Your final hand is {user_cards},final score = {user_score}")
    print(f"Computer final hand is {computer_score} , final score = {computer_score}")
    print(compare(user_score,computer_score))
print("\n"*20)
while input("Do you want to play blackjack ? Type 'y' for yes or 'n' for no: ").lower() == "y" :
    play_games()