import random
import time

cards = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def deal_card():
    return random.choice(list(cards.keys()))

def calc_point(hand):
    score = 0
    for card in hand:
        score += cards[card]
    if 'A' in hand and score > 21:
        score -= 10 # Ace will now contribute 1 instead of 11 points
    return score
    
def blackjack():
    print('''
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P" ''')

    # a list of flags for end-game results
    went_over = False
    user_blackjack = False
    computer_blackjack = False

    print("\nFor this version of BlackJack, Ace will count as 11\n")
    print("The dealer has served")
    
    # create the 2 players
    user = []
    computer = []

    # deal 2 cards for each player
    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    # calculate both of their scores
    user_point = calc_point(user)
    computer_point = calc_point(computer)

    # print the initial status of their cards
    print(f"\tYour cards: {user}, current score: {user_point}")
    print(f"\tComputer's first cards: {computer[0]}")

    # conditions for BlackJack, else, ask for more cards
    if 'A' in user and ('10' in user or 'J' in user or 'Q' in user or 'K' in user):
        user_blackjack = True
    elif 'A' in computer and ('10' in computer or 'J' in computer or 'Q' in computer or 'K' in computer):
        computer_blackjack = True
    else:
        # ask if the player wants to draw another card
        while user_point <= 21 and input("Type 'y' to get another cards, anything else to pass: ").lower() == 'y':
            user.append(deal_card())
            user_point = calc_point(user)
            
            print(f"\tYour cards now are: {user}, current score: {user_point}")
            print(f"\tComputer's first cards: {computer[0]}")

        # rule: if dealer < 17, must draw another card
        while computer_point < 17:
            computer.append(deal_card())
            computer_point = calc_point(computer)

    print("\nBoth players will now show their hands...\n")

    #print the final cards from both players
    print(f"\tYour final cards: {user}, FINAL score: {user_point}")
    print(f"\tComputer's final cards: {computer}, FINAL score: {computer_point}\n")
    
    if user_blackjack:
        print("BLACKJACK - You have WON! <3")
    elif computer_blackjack:
        print("Computer's got a BLACKJACK - You have LOST =(")
    elif user_point > 21:
        print("You went over. You LOSE =(")
    elif computer_point > 21:
        print("Computer went over - You've WON! <3")
    elif user_point > computer_point:
        print("Congratulations - You WIN! <3")
    else:
        print("You have less points - You LOSE =(")

while input("\nWould you like to play a game of BLACKJACK? 'Y' for YES | ANYTHING ELSE for NO: ").lower() == 'y':
    blackjack()
