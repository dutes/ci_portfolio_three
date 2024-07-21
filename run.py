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
            display_high_scores()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def start_new_game():
    create_table()
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    if player_hand.value == 21:
        if dealer_hand.value == 21:
            push()
            return end_game(deck, player_hand, dealer_hand, player_chips)
        else:
            player_wins(player_chips)
            return end_game(deck, player_hand, dealer_hand, player_chips)

    playing = True
    while playing:
        playing = hit_or_stand(deck, player_hand, dealer_hand, player_chips)
        if player_hand.value > 21:
            player_busts(player_chips)
            return end_game(deck, player_hand, dealer_hand, player_chips)  # Pass deck instance

    if player_hand.value <= 21:
        return end_game(deck, player_hand, dealer_hand, player_chips)  # Pass deck instance

def end_game(deck, player_hand, dealer_hand, player_chips):  # Accept deck as a parameter
    if player_hand.value <=21:
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
    else:
        show_all(player_hand, dealer_hand)

    print("\nPlayer's winnings stand at", player_chips.total)
    if player_chips.total >= 100:
        name = input("Enter your name for the high score table: ")
        add_highscore(name, player_chips.total)

    print("High Scores:")
    display_high_scores()

    play_again = input("Do you want to play again? Enter 'y' or 'n': ")
    if play_again[0].lower() == 'y':
        start_new_game()
    else:
        print("Thanks for playing")
        return

def display_high_scores():
    highscores = get_highscores()
    if highscores:
        print("\nHigh Scores:")
        for rank, (name, score) in enumerate(highscores, start=1):
            print(f"{rank}. {name} - {score}")
    
        delete_option=input("Do you want to delete all the highscores? Type delete to confirm (Type anything to abort): ")
        if delete_option.lower()=='delete':
            delete_highscores()
            print('All highscores have been deleted.')
    
    else:
        print("No high scores available.")

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
    global playing
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
