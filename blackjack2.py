import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
end_of_game = False

def dealcards(deal_to, amount=1):
    for nrOfCards in range(0, amount):
        deal_to.append(random.choice(cards))

def show_cards():
    user_total = sum(user_cards)
    computer_total = sum(computer_cards)
    return user_total, computer_total

def calculate_score():

    user_total = show_cards()[0]
    computer_total = show_cards()[1]

    global end_of_game

    if computer_total == 21:
        end_of_game = True
        print("Computer blackjack!")
        return end_of_game
    elif user_total == 21:
        end_of_game = True
        print("Player has blackjack!")
        return end_of_game
    
    if user_total > 21:
        end_of_game = True
        print("Player bust, computer wins!")
        return end_of_game

    elif computer_total > 21:
        end_of_game = True
        print("Computer bust, player wins!")
        return end_of_game
    
    return user_total, computer_total

        # if 11 in user_cards:
        #     for i in range(0, len(user_cards)):
        #         if user_cards[i] == 11:
        #             user_cards[i] == 1
        #             calculate_score()
        # else:
        #     print("Computer wins")
        #     end_of_game = True
        #     return end_of_game

def compare():
    results = calculate_score()
    try: 
        user = results[0]
        computer = results[1]
    except: return

    if user < 21 and computer < 21:
        if user > computer:
            end_of_game = True
            return print("User wins!"), end_of_game
        else:
            end_of_game = True
            return print("Computer wins!"), end_of_game
    if user == computer:
        end_of_game = True
        return print("Draw!"), end_of_game

    
    

def main():
    dealcards(computer_cards, 2)
    dealcards(user_cards, 2)
    while end_of_game == False:
        print(f"You have: {user_cards}")
        print(f"Computer has: {computer_cards}")
        if calculate_score() == True:
            continue
        

        hit_stay = input("Hit or stay?: ").lower()
        if hit_stay == 'hit':
            dealcards(user_cards)
            calculate_score()         
        elif hit_stay == 'stay': #computers turn to get cards
            while calculate_score()[1] < 17:
                dealcards(computer_cards)
                compare()

        


main()
play_again = input("Play again? y/n ").lower()
if play_again == 'y':
    main()
else: exit()

