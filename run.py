from app.game import Deck, Hand, Chips
from app.database import create_table, add_highscore, get_highscores, delete_highscores

def main_menu():
    while True:
        print("\nBlack Jack Main Menu")
        print("1. New Game")
        print("2. View High Scores")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_new_game()
        elif choice == '2':
            display_high_scores_with_options()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def start_new_game():
    create_table()
    deck = Deck()
    deck.shuffle()

    player_chips=Chips()
    player_chips.total=100

    print(f"You have {player_chips.total} chips to start. \nEach bet you make is taken from your total, each win added. \nWhen you reach zero chips your game is over")

    while player_chips.total > 0:
        print(f"your current chip balance is: {player_chips.total}")
        take_bet(player_chips)

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        show_some(player_hand, dealer_hand)

        if player_hand.value == 21 and dealer_hand.value == 21:
                show_all(player_hand, dealer_hand)
                push()
                
        elif player_hand.value == 21:
                show_all(player_hand,dealer_hand)
                player_wins(player_chips)
                
        elif dealer_hand.value == 21:
                show_all(player_hand, dealer_hand)
                dealer_wins(player_chips)
        
        else:
            playing = True
            while playing:
                playing = hit_or_stand(deck, player_hand, dealer_hand, player_chips)
                if player_hand.value > 21:
                    player_busts(player_chips)
                    break 
            if player_hand.value <= 21:
                    end_game(deck, player_hand, dealer_hand, player_chips)  # Pass deck instance
        
        if player_chips.total <= 0:
            print("You have no more chips. Game Over")
            break

        play_again=input("Do you want to play another round? Enter 'y' or 'n': ")
        if play_again[0].lower() !='y':
            break
    if player_chips.total > 0:
        if is_highscore(player_chips.total):
            name=input('Enter your name for the high score table: ')
            add_highscore(name, player_chips.total)
        else:
            print("Thanks for playing")
    else:
        print('Thanks for playing')
    
    main_menu()

def end_game(deck, player_hand, dealer_hand, player_chips): 
    while dealer_hand.value < 17:
        hit(deck, dealer_hand)
    show_all(player_hand, dealer_hand)
    if dealer_hand.value > 21:
         dealer_busts(player_chips)
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_chips)
    elif dealer_hand.value < player_hand.value:
        player_wins(player_chips)
    else:
        push()       

def display_high_scores():
    highscores = get_highscores()
    if highscores:
        print('\nHigh Scores:')
        for rank, (name, score) in enumerate(highscores, start=1):
            print(f"{rank}. {name} - {score}")
    else:
        print("Your score did not break the top three.")


def display_high_scores_with_options():
    highscores = get_highscores()
    if highscores:
        print("\nHigh Scores:")
        for rank, (name, score) in enumerate(highscores, start=1):
            print(f"{rank}. {name} - {score}")

        print("\nType 'b' to return to the main menu or 'x' to delete the high scores.")
        choice = input("Enter your choice: ")
        if choice.lower() =='x':
            delete_confirm=input("Type 'delete' to confirm the deleition of all high scores: ")
            if delete_confirm.lower()=='delete':
                delete_highscores()
                print("High scores have been deleted. \nPress any enter to return to main menu")
                input()             
        
        elif choice.lower() =='b':
            return
    else:
        print("There are no high scores currently available. Press any key to return to the main menu.")
        input()

def is_highscore(score):
    highscores=get_highscores
    return len(highscores) < 3 or score > highscores[-1][1]

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
            if chips.bet > chips.total:
                print(f"Sorry, you don't have enough chips! You have: {chips.total}")
            else:
                break
        except ValueError:
            print("Sorry, a bet must be an integer!")

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, player_hand, dealer_hand, player_chips):
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() == 'h':
            hit(deck, player_hand)
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                return False  # Player busts, end game
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            return False  # Player stands, end game
        else:
            print("Sorry, please try again.")
            continue
        return True

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print(f"\nPlayer's Hand (value: {player.value}):", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print(f"\nPlayer's Hand (value: {player.value}):", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts! Player wins!")
    chips.win_bet()

def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()

def push():
    print("Dealer and Player tie! It's a push.")

if __name__ == "__main__":
    main_menu()
