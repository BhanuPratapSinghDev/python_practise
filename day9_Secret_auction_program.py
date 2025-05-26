logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret bidding")
auction_dictionary = {}

continue_bidding = True

def bidding(auction_dictionary):
    highest_bid = 0
    winner = ""
    for key in auction_dictionary:
        bidding_amount = auction_dictionary[key]
        if bidding_amount > highest_bid :
            highest_bid = bidding_amount
            winner = key

    print(f"The winner is: {winner} with a bid of ${highest_bid}")


while continue_bidding:
    name = input("Enter your name please : ")
    bid = int(input("Enter your bid please : $"))
    auction_dictionary [name] = bid
    ask = input("Are there any other bidders ? Type 'yes' or 'no'.").lower()

    if ask == "yes":
        continue_bidding = True
        print("\n" * 100)                               # to clear out the screen
    else:
        continue_bidding = False
        bidding(auction_dictionary)
      
# max_value = max(auction_dictionary , key= auction_dictionary.get)