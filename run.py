from app.game import Deck, Hand, Chips
from app.database import(
    create_table, add_highscore, get_highscores, delete_highscores
    )

def main_menu():
    """
    Displays the main menu for the game. Handles user input for the options:
    1. New Game
    2. View High Scores
    3. Exit

    New Game: Starts a new game of Black Jack by calling the start_new_game
    function.

    View High Scores: Displays the high scores table with the top three scores
    by calling the display_high_scores_with_options function.

    Exit: Exits the game.

    If the user enters an invalid choice, the function will display an error
    message and prompt the user to enter a valid choice.

    Returns: none
    """
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
    """
    Initalizes a new game of black jack. The game will continue until the player runs out of chips or chooses to exit the game.
    The game will display the player's current chip balance and prompt the player to enter a bet.
    The player and dealer hands will be dealt two cards each. The player's hand will be displayed, with one of the dealer's cards hidden.
    If the player or dealer has a blackjack, the game will end and the appropriate win/loss message will be displayed.
    If neither the player or dealer has a blackjack, the player will be prompted to hit or stand.
    If the player busts, the player will lose the bet and the game will end.
    If the player stands, the dealer will play. If the dealer busts, the player wins.
    If the dealer wins, the player loses the bet.
    If the player wins, the player wins the bet.
    If the player and dealer tie, the player will push and the bet will be returned.
    If the player runs out of chips, the game will end.
    If the player chooses to play again, the game will continue.
    If the player has a high score, the player will be prompted to enter their name for the high score table.
    If the player does not have a high score, the player will be thanked for playing.

    Returns: none
    """
    create_table()
    deck = Deck()
    deck.shuffle()

    player_chips=Chips()
    player_chips.total=100

    print("You have", player_chips.total, "chips to start.")
    print("\nEach bet you make is taken from your total, each win added.")
    print("\nWhen you reach zero chips your game is over.")

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
                playing = hit_or_stand(deck, player_hand, dealer_hand)
                if player_hand.value > 21:
                    player_busts(player_chips)
                    break
            if player_hand.value <= 21:
                end_game(deck, player_hand, dealer_hand, player_chips)
        if player_chips.total <= 0:
            print("You have no more chips. Game Over")
            break

        play_again=input(
            "Do you want to play another round? Enter 'y' or 'n': "
            )
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

def end_game(deck,player_hand, dealer_hand, player_chips):
    """
    Handles the end of game logic which includes the dealer playing and determining the winner of the game and updating the player's chip balance.
    The fucntion performs the following actions:
    1. The dealer will play until their hand value is 17 or greater.
    2. The dealer's hand will be displayed.
    3. If the dealer busts, the player wins.
    4. If the dealer's hand value is greater than the player's hand value, the dealer wins.
    5. If the dealer's hand value is less than the player's hand value, the player wins.
    6. If the dealer's hand value is equal to the player's hand value, the player pushes.
    7. The player's chip balance will be updated based on the outcome of the game.
    8. The function will return to the start_new_game function if the player has chips remaining.
    

    Parameters:
    deck (Deck): The deck of cards used in the game.
    player_hand (Hand): The player's hand of cards.
    dealer_hand (Hand): The dealer's hand of cards.
    player_chips (Chips): The player's chip balance.

    Returns: none

    """
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
    """
    Displays the top three high scores from the high scores table.
    If there are no high scores, the function will display a message
    indicating that the player's score did not break the top three.

    Returns: none
    """
    highscores = get_highscores()
    if highscores:
        print('\nHigh Scores:')
        for rank, (name, score) in enumerate(highscores, start=1):
            print(f"{rank}. {name} - {score}")
    else:
        print("Your score did not break the top three.")


def display_high_scores_with_options():
    """
    Displays the high scores table with the top three scores and provides the
    player with the option to return to the main menu or delete high scores.
    If the player chooses to delete the high scores, the function will prompt
    the player to confirm the deletion.
    If the player confirms the deletion, the high scores table will be deleted.
    If the player chooses to return to the main menu, the function will return
    to the main menu.
    If there are no high scores, the function will display a message
    indicating that there are no high scores available.

    Returns: none
    """
    highscores = get_highscores()
    if highscores:
        print("\nHigh Scores:")
        for rank, (name, score) in enumerate(highscores, start=1):
            print(f"{rank}. {name} - {score}")

        print("\nType 'b' to return to the main menu or 'x'")
        print("to delete the high scores.")
        choice = input("Enter your choice: ")
        if choice.lower() =='x':
            delete_confirm=input ("Type 'delete' to confirm the deletion of all high scores:")
            if delete_confirm.lower()=='delete':
                delete_highscores()
                print("High scores have been deleted.")
                print("\nPress any enter to return to main menu")
                input()               
        elif choice.lower() =='b':
            return
    else:
        print("There are no high scores currently available.")
        print("\nPress any key to return to the main menu.")
        input()

def is_highscore(score):
    """
    Determines if the player's score is a high score by comparing the player's 
    score to the top three scores in the high scores table.
    If the player's score is greater than the lowest score in the high scores
    table, the function will return True.
    If the player's score is not greater than the lowest score in the high
    scores table, the function will return False.
    
    Parameters:
    score (int): The player's score to compare to the high scores table.

    Returns:
    bool: True if the player's score is a high score, False otherwise.
    """
    highscores=get_highscores()
    return len(highscores) < 3 or score > highscores[-1][1]

def take_bet(chips):
    """
    Prompts the player to enter a bet and validates the bet amount.
    If the player enters a bet greater than their chip balance, the function
    will display an error message and prompt the player to enter a valid bet.
    If the player enters a non-integer value, the function will display an
    error message and prompt the player to enter a valid bet.

    Parameters:
    chips (Chips): The player's chip balance.

    Returns: none
    """
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips!")
                print(f"\nYou have: {chips.total}")
            else:
                break
        except ValueError:
            print("Sorry, a bet must be an integer!")

def hit(deck, hand):
    """
    Adds a card to the player's or dealer's hand and adjusts the hand value
    for aces.
    
    Parameters:
    deck (Deck): The deck of cards used in the game.
    hand (Hand): The player's or dealer's hand of cards.

    Returns: none
    """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, player_hand, dealer_hand):
    """
    Prompts the player to hit or stand and validates the player's input.
    If the player enters an invalid input, the function will display an
    error message and prompt the player to enter a valid input.
    If the player chooses to hit, the player will be dealt another card
    and the player's hand will be displayed.
    If the player chooses to stand, the function will return False.
    
    Parameters:
    deck (Deck): The deck of cards used in the game.
    player_hand (Hand): The player's hand of cards.
    dealer_hand (Hand): The dealer's hand of cards.
    
    Returns:
    bool: True if the player chooses to hit, False if the player chooses
    to stand.
    """
    while True:
        try:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
            if x[0].lower() == 'h':
                hit(deck, player_hand)
                show_some(player_hand, dealer_hand)
                if player_hand.value > 21:
                    return False  # Player busts, end game
            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                return False  # Player stands, end game
            #else:
                #print("Sorry, please try again.")
        except(IndexError, ValueError):
            print("Invalid input, please enter either 'h' or 's'.")   
        return True

def show_some(player, dealer):
    """
    Displays the player's hand and one of the dealer's cards.

    Parameters:
    player (Hand): The player's hand of cards.
    dealer (Hand): The dealer's hand of cards.

    Returns: none
    """
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print(f"\nPlayer's Hand (value: {player.value}):", *player.cards, sep='\n ')

def show_all(player, dealer):
    """
    Displays the player's hand and the dealer's hand.
    
    Parameters:
    player (Hand): The player's hand of cards.
    dealer (Hand): The dealer's hand of cards.
    
    Returns: none
    """
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print(f"\nPlayer's Hand (value: {player.value}):", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(chips):
    """
    Displays a message indicating that the player has busted and updates the
    player's chip balance.
    
    Parameters:
    chips (Chips): The player's chip balance.
    
    Returns: none
    """
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    """
    Displays a message indicating that the player has won and updates the
    player's chip balance.
    
    Parameters:
    chips (Chips): The player's chip balance.
    
    Returns: none
    """
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    """
    Displays a message indicating that the dealer has busted and updates
    the player's chip balance.
    
    Parameters:
    chips (Chips): The player's chip balance.
    
    Returns: none
    """
    print("Dealer busts! Player wins!")
    chips.win_bet()

def dealer_wins(chips):
    """
    Displays a message indicating that the dealer has won and updates
    the player's chip balance.
    
    Parameters:
    chips (Chips): The player's chip balance.
    
    Returns: none
    """
    print("Dealer wins!")
    chips.lose_bet()

def push():
    """
    Displays a message indicating that the player and dealer have tied.
    
    Returns: none
    """
    print("Dealer and Player tie! It's a push.")

if __name__ == "__main__":
    main_menu()
