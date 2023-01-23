import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
end_of_game = False

def dealcards(deal_to, amount=1):
    for nrOfCards in range(0, amount):
        deal_to.append(random.choice(cards))

def calculate_score():
    user_total = sum(user_cards)
    computer_total = sum(computer_cards)

    if computer_total == 21:
        end_of_game == True
        print("Computer has end_of_game!")
        return end_of_game
    elif user_total == 21:
        end_of_game = True
        print("Player has end_of_game!")
        return end_of_game
    
    if user_total > 21:
        if 11 in user_cards:
            for i in range(0, len(user_cards)):
                if user_cards[i] == 11:
                    user_cards[i] == 1
                    calculate_score()
        else:
            print("Computer wins")
            end_of_game = True
            return end_of_game

 

def main():
    dealcards(computer_cards, 2)
    dealcards(user_cards, 2)
    while end_of_game == False:
        print(f"You have: {user_cards}")
        print(f"Computer has: {computer_cards}")
        calculate_score()

        hit_stay = input("Hit or stay?: ").lower()
        if hit_stay == 'hit':
            dealcards(user_cards)
            hit_stay = ''
            continue
        else: break
        

main()

