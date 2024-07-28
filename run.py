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
from rich.console import Console
from rich.text import Text
from app.game import Deck, Hand, Chips
from app.database import(create_table, add_highscore, get_highscores)

# Rest of the code...
console=Console()
#ASCII art for main menu
BLACKJACK_ART = r"""
 ____  _        _    ____ _  __   _   _    ____ _  __
| __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /
|  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' / 
| |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \ 
|____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\
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
        clear_screen()
        blackjack_art=Text(BLACKJACK_ART,style="bold green")
        console.print(blackjack_art)
        console.print("\nBlack Jack Main Menu",style="red")
        console.print("=====================",style="bold yellow")
        console.print("1. New Game",style="bright_green")
        console.print("2. View High Scores", style="bright_yellow")
        console.print("3. Exit", style="bright_red")

        console.print("Enter your choice: ", style="bold yellow")
        choice = input().strip()

        if choice == '1':
            start_new_game()
        elif choice == '2':
            display_high_scores()
        elif choice == '3':
            console.print("Thank you for playing!",style="bold yellow")
            break
        else:
            clear_screen()
            console.print("Invalid choice. Please enter 1, 2, or 3.",
                          style="bold red")

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
    console.print(f"You have [bold cyan]{player_chips.total}[/bold cyan]chips to start."
                  ,style="bold yellow")
    console.print("\nEach bet you make is taken from your total, each win added.",
        style="bold green")
    console.print("\nWhen you reach zero chips your game is over.\n"
                  ,style="bold red")

    while player_chips.total > 0:
        console.print(f"your current chip balance is: [bold cyan]{player_chips.total}[/bold cyan]"
                      ,style="bold green")
        take_bet(player_chips)

        clear_screen()
        console.print(
            f"Game has started, player has bet [bold cyan]{player_chips.total}[/bold cyan] chips",
                      style="bold green")

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
            print("You have no more chips. Game Over",style="bold red")
            break

        while True:
            console.print("Do you want to play another round? Enter 'y' or 'n': "
                          ,style="bold yellow")
            play_again=input().strip().lower()
            if play_again in ['y', 'n']:
                break
            else:
                console.print("Invalid input. Please enter 'y' or 'n'."
                              ,style="bold red")
        if play_again == 'n':
            console.print(f"Your score is: {player_chips.total}",
                          style="bold green")
            break

    if player_chips.total > 0:
        if is_highscore(player_chips.total):
            while True:
                console.print("Enter your initials for the high score table: "
                              ,style="bright_magenta")
                name = input().strip().upper()
                console.print("3 letters max, only letters allowed"
                              ,style="bold yellow")
                if re.match("^[A-Z]{1,3}$", name):
                    add_highscore(name, player_chips.total)
                    display_high_scores()
                    break
                else:
                    print("Invalid input. Please enter 1-3 letters."
                          ,style="bold red")
        else:
            console.print("Thanks for playing",style="bold yellow")
            console.print(f"Your score is: {player_chips.total}"
                          ,style="bold green")
            input("Press Enter to return to the main menu.")
    else:
        console.print("Thanks for playing",style="bold yellow")
        console.print(f"Your score is: {player_chips.total}"
                      ,style="bold green")
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
        console.print("Round Over - Dealer busts! Player wins!"
                      ,style="bold green")
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_chips)
    elif dealer_hand.value < player_hand.value:
        player_wins(player_chips)
        console.print("Round Over - Player wins!",
                      style="bold green")
    else:
        push()
        console.print("Round Over - its a push!",
                      style="bold yellow")

def display_high_scores():
    """
    Displays the top three high scores from the high scores table.
    If there are no high scores, the function will display a message
    indicating that the player's score did not break the top three.

    Returns: none
    """
    clear_screen()
    highscores = get_highscores()
    if highscores:
        console.print('\nHigh Scores:',style="bold green")
        for rank, (name, score) in enumerate(highscores, start=1):
            console.print(f"{rank}. {name} - {score}")
    else:
        console.print("There are no high scores yet.",style="bold red")
    while True:
        console.print("\nType 'b' to return to the main menu.",
                      style="bold yellow")
        user_input = input().strip()
        if user_input == 'b':
            break
        else:
            console.print("Invalid input. Type b to return to the main menu.",
                          style="bold red")

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
            console.print("How many chips would you like to bet? ",
                          style="bold yellow")
            bet =input().strip()
            if bet.isnumeric():
                bet=int(bet)
                if bet > 0:
                    if bet > chips.total:
                        console.print("You do not have enough chips",
                                      style="bold red")
                        console.print(f"you have {chips.total} chips")
                    else:
                        chips.bet=bet
                        break
                else:
                    console.print("bet needs to be a number greater than 0",
                                  style="bold red")
            else:
                console.print("bet needs to be a positive number",
                              style="bold red")
        except ValueError:
            console.print("bet needs to be a number", style="bold red")

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
            console.print("Would you like to Hit or Stand? Enter 'h' or 's' ",
                          style="bold yellow")
            x = input().strip()
            if x[0].lower() == 'h':
                hit(deck, player_hand)
                clear_screen()
                show_some(player_hand, dealer_hand)
                if player_hand.value > 21:
                    return False  # Player busts, end game
            elif x[0].lower() == 's':
                console.print("Player stands. Dealer is playing.",
                              style="bold green")
                return False  # Player stands, end game
            #else:
                #print("Sorry, please try again.")
        except(IndexError, ValueError):
            console.print("Invalid input, please enter either 'h' or 's'.",
                          style="bold red")
            return True

def show_some(player, dealer):
    """
    Displays the player's hand and one of the dealer's cards.

    Parameters:
    player (Hand): The player's hand of cards.
    dealer (Hand): The dealer's hand of cards.

    Returns: none
    """
    console.print("\nDealer's Hand:",style="magenta")
    console.print(" ::card hidden::",style="magenta")
    console.print(f" {dealer.cards[1]}" ,style="magenta")
    console.print(f"\nPlayer's Hand (value: {player.value}):",
                  style="bright_blue")
    for card in player.cards:
        console.print(f" {card}",style="bright_blue")

def show_all(player, dealer):
    """
    Displays the player's hand and the dealer's hand.
    
    Parameters:
    player (Hand): The player's hand of cards.
    dealer (Hand): The dealer's hand of cards.
    
    Returns: none
    """
    console.print("\nDealer's Hand:",style="magenta")
    for card in dealer.cards:
        console.print(f" {card}",style="magenta")
    console.print(f"Dealer's Hand = {dealer.value}",style="magenta")
    console.print(f"\nPlayer's Hand (value: {player.value}):",
                  style="bright_blue")
    for card in player.cards:
        console.print(f" {card}",style="bright_blue")
    console.print(f"Player's Hand = {player.value}",style="bright_blue")

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
