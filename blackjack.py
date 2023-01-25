############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo
import os

def deal_card():
    """Deal a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card



#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []



#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
def calculate_score(cards):
    """Calculate the sum of cards, if one card is 11 and the sum of cards is >21 replace that card with 1"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    

def compare(user_score, computer_score):
    """This function compares the cards and returns a winner"""
    if user_score == computer_score:
        return print("It's a draw!")
    elif computer_score == 0:
        return print("Computer wins!")
    elif user_score == 0:
        return print("User wins!")
    elif user_score > 21:
        return print("User bust, computer wins!")
    elif computer_score > 21:
        return print("Computer bust, user wins!")
    elif computer_score > user_score:
        return print("Computer wins!")
    elif computer_score < user_score:
        return print("User wins!")

def play_blackjack():
    """Main function and entrypoint into the game"""
    user_cards = []
    computer_cards = []
    end_of_game = False
    #Initial dealing of cards
    print(logo)
    for _ in range(2):
        user_cards.append(deal_card())    
        computer_cards.append(deal_card())
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    while not end_of_game: #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User cards: {user_cards} score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")
        #Define end conditions of the loop at the top
        #check if the game has ended before stepping into the else block of drawing another card
        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_of_game = True
        else:
            user_deals = input("Draw another card? y/n ")
            if user_deals == 'y':
                user_cards.append(deal_card())
            else:
                end_of_game = True

        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.



    #After user draws, draw for computer until calculate_score() returns more than 17
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())
    
    print(f"User final hand: {user_cards} final score: {user_score}")
    print(f"Computer final cards: {computer_cards} final score: {computer_score}")
    compare(user_score, computer_score)
    

#Continously ask if we should play again
while input("Would you like to play a game of blackjack? y/n: ") == 'y':
    os.system('clear')
    play_blackjack()










#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

