### My own attempt at creating the blackjack game from scratch, without looking at other code/solutions ###

from art import logo
import os
import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    """Returns the sum of the list of cards. If blackjack on first two cards, return zero. If 11/ace is hit and score exceeds 21 - remove 21 and insert 1 instead"""
    if sum(cards) == 21 and len(cards) == 2: #If blackjack is hit return 0 and immedietly end the game
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the cards after dealing has finished"""
    if computer_score == 0:
        return "Computer has blackjack!"
    elif user_score == 0:
        return "User has blackjack!"
    elif user_score == computer_score:
        return "Draw!"
    elif user_score > 21:
        return "User bust, computer wins!"
    elif computer_score > 21:
        return "Computer bust, user wins!"
    elif user_score > computer_score:
        return "User wins!"
    elif computer_score > user_score:
        return "Computer wins!"

def play_game():
    """The main entrypoint for the game"""
    user_cards = []
    computer_cards = []
    game_over = False

    print(logo)

    for _ in range(2): #begin with 2 cards
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over: #This handles the logic of cards dealt to user, whenever game_over hits True (if blackjack, loss or)
        #start off by dealing 2 cards
       
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User hand: {user_cards}, score: {user_score}")
        print(f"Computer hand: {computer_cards[0]}")

        #Set basecase to exit the rule, in this case all win conditions
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            if input("Do you want to hit another card? y/n ") == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score < 17: #We need to continously call the calculate score so that computer_score is dynamically updated. Other than that it doesnt matter in what loop we place it
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    
while input("Do you want to play a game of blackjack? y/n ").lower() == 'y':
    os.system('clear')
    play_game()








