"""
This module contains the main game logic for a text-based version of the game
Black Jack.
The game allows the player to play multiple rounds of Black Jack, place bets,
view high scores,
and exit the game. The game is played against a computer dealer.

The module includes the following functions:
- clear_screen(): Clears the terminal screen.
- main_menu(): Displays the main menu for the game and handles user input for
menu options.
- start_new_game(): Initializes a new game of Black Jack and handles the game
flow.
- end_game(deck, player_hand, dealer_hand, player_chips): Handles the end of
game logic and determines the winner.
- display_high_scores(): Displays the top three high scores from the high
scores table.
- is_highscore(score): Determines if the player's score is a high score.
- take_bet(chips): Prompts the player to enter a bet and validates the bet
amount.
- hit(deck, hand): Adds a card to the player's or dealer's hand and adjusts
the hand value for aces.
- hit_or_stand(deck, player_hand, dealer_hand): Prompts the player to hit or
stand and validates the player's input.
- show_some(player, dealer): Displays the player's hand and one of the
dealer's cards.  
- show_all(player, dealer): Displays the player's hand and the dealer's hand.
- player_busts(chips): Displays a message indicating that the player has
busted and updates the player's chip balance.
- player_wins(chips): Displays a message indicating that the player has won
and updates the player's chip balance.
- dealer_busts(chips): Displays a message indicating that the dealer has
busted and updates the player's chip balance.

The module also imports the following classes and functions:
- Deck: A class representing a deck of cards.
- Hand: A class representing a hand of cards.
- Chips: A class representing the player's chip balance.
- create_table(): A function to create the high scores table in the database.
- add_highscore(name, score): A function to add a high score to the database.
- get_highscores(): A function to retrieve the top three high scores from
the database.

The module is run as the main program to start the game by calling the
main_menu function.
"""

import re
import os
from app.game import Deck, Hand, Chips
from app.database import(create_table, add_highscore, get_highscores)

# Rest of the code...

#ASCII art for main menu
BLACKJACK_ART= r"""
______ _            _      ___            _    
| ___ \ |          | |    |_  |          | |   
| |_/ / | __ _  ___| | __   | | __ _  ___| | __
| ___ \ |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
| |_/ / | (_| | (__|   </\__/ / (_| | (__|   < 
\____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\
"""

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

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
        print(BLACKJACK_ART)
        print("\nBlack Jack Main Menu")
        print("1. New Game")
        print("2. View High Scores")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            start_new_game()
        elif choice == '2':
            display_high_scores()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            clear_screen()
            print("Invalid choice. Please enter 1, 2, or 3.")

def start_new_game():
    """
    Initalizes a new game of black jack. The game will continue until the
    player runs out of chips or chooses to exit the game.
    The game will display the player's current chip balance and prompt the
    player to enter a bet.
    The player and dealer hands will be dealt two cards each. 
    The player's hand will be displayed, with one of the dealer's cards hidden.

    Returns: none
    """
    create_table()
    deck = Deck()
    deck.shuffle()

    player_chips=Chips()
    player_chips.total=100
    clear_screen()
    print("You have", player_chips.total, "chips to start.")
    print("\nEach bet you make is taken from your total, each win added.")
    print("\nWhen you reach zero chips your game is over.")

    while player_chips.total > 0:
        print(f"your current chip balance is: {player_chips.total}")
        take_bet(player_chips)

        clear_screen()
        print(f"Game has started, player has bet {player_chips.bet} chips")

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

        while True:
            play_again=input(
            "Do you want to play another round? Enter 'y' or 'n': "
            ).strip().lower()
            if play_again in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        if play_again == 'n':
            print(f"Your score is: {player_chips.total}")
            break

    if player_chips.total > 0:
        if is_highscore(player_chips.total):
            while True:
                name = input(
                    "Enter your initials for the high score table: "
                    ).strip().upper()
                print("3 letters max, only letters allowed")
                if re.match("^[A-Z]{1,3}$", name):
                    add_highscore(name, player_chips.total)
                    display_high_scores()
                    break
                else:
                    print("Invalid input. Please enter 1-3 letters.")
        else:
            print("Thanks for playing")
            print(f"Your score is: {player_chips.total}")
            input("Press Enter to return to the main menu.")
    else:
        print("Thanks for playing")
        print(f"Your score is: {player_chips.total}")
        input("Press Enter to return to the main menu.")

    clear_screen()
    main_menu()

def end_game(deck,player_hand, dealer_hand, player_chips):
    """
    Handles the end of game logic which includes the dealer playing and
    determining the winner of the game and updating the player's chip balance.
        

    Parameters:
    deck (Deck): The deck of cards used in the game.
    player_hand (Hand): The player's hand of cards.
    dealer_hand (Hand): The dealer's hand of cards.
    player_chips (Chips): The player's chip balance.

    Returns: none

    """
    while dealer_hand.value < 17:
        hit(deck, dealer_hand)
    clear_screen()
    show_all(player_hand, dealer_hand)
    if dealer_hand.value > 21:
        dealer_busts(player_chips)
        print("Round Over - Dealer busts! Player wins!")
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_chips)
    elif dealer_hand.value < player_hand.value:
        player_wins(player_chips)
        print("Round Over - Player wins!")
    else:
        push()
        print("Round Over - its a push!")

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
        print("There are no high scores yet.")
    while True:
        print("\nType 'b' to return to the main menu.")
        user_input = input().strip()
        if user_input == 'b':
            break
        else:
            print("Invalid input. Type b to return to the main menu.")

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
            bet =input("How many chips would you like to bet? ").strip()
            if bet.isnumeric():
                bet=int(bet)
                if bet > 0:
                    if bet > chips.total:
                        print("You do not have enough chips")
                        print(f"you have {chips.total} chips")
                    else:
                        chips.bet=bet
                        break
                else:
                    print("bet needs to be a number greater than 0")
            else:
                print("bet needs to be a positive number")
        except ValueError:
            print("bet needs to be a number")

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
                clear_screen()
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
    print(f"\nPlayer's Hand (value: {player.value}):",*player.cards,sep='\n ')
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
    print("Round Over - Dealer wins!")
    chips.lose_bet()

def push():
    """
    Displays a message indicating that the player and dealer have tied.
    
    Returns: none
    """
    print("Dealer and Player tie! It's a push.")

if __name__ == "__main__":
    main_menu()
