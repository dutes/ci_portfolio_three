import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    """
    Represents a playing card.

    Attributes:
        suit (str): The suit of the card.
        rank (str): The rank of the card.
    """

    def __init__(self, suit, rank):
        """
        Initializes a Card object with a suit and rank.
        
        Parameters:
            suit (str): The suit of the card.
            rank (str): The rank of the card.
        
        Returns:    
            None
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Returns a string representation of the card.
        
        Parameters:
        None
            
        Returns:    
        str: A string representation of the card.
                
        Example:    
        'Two of Hearts'
                    
        """
        return f'{self.rank} of {self.suit}'

class Deck:
    """
    Represents a deck of playing cards.
    
    Attributes:
        deck (list): A list of Card objects representing the deck of cards.
    
    Methods:
        shuffle: Shuffles the deck of cards.
        deal: Removes and returns a card from the deck.
    """

    def __init__(self):
        """
        Initializes a Deck object with a standard deck of 52 playing cards.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the deck of cards.
        
        This method shuffles the deck of cards using the random.shuffle function.
        
        Parameters:
        None
        
        Returns:
        None
        
        Example:
        deck.shuffle()
    """
        random.shuffle(self.deck)

    def deal(self):
        """
        Removes and returns a card from the deck.
        
        This method removes the last card from the deck and returns it.
        
        Parameters:
        None
        
        Returns:
        Card: A Card object representing the dealt card.
        """
        return self.deck.pop()

class Hand:
    """
    Represents a hand of playing cards.
    
    Attributes:
        cards (list): A list of Card objects representing the cards in the hand.
        value (int): The total value of the cards in the hand.
        aces (int): The number of aces in the hand.
    
    Methods:
        add_card: Adds a card to the hand.
        adjust_for_ace: Adjusts the value of the hand for aces.
    """
    def __init__(self):
        """
        Initializes a Hand object with an empty list of cards, a value of 0, and no aces.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Adds a card to the hand and adjusts the value of the hand.
        
        This method adds a card to the hand, updates the value of the hand based on the card's rank, and adjusts the value for aces if necessary.
        
        Parameters:
            card (Card): The Card object to add to the hand.
            
        Returns:
            None
        
        Example:    
            hand.add_card(card)
        """
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        """
        Adjusts the value of the hand for aces.
        
        This method adjusts the value of the hand for aces by subtracting 10 from the value if the total value is greater than 21 and there is at least one ace in the hand.
        
        Parameters:
        None
        
        Returns:
        None
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    """"
    Represents the chips used for betting in the game.
    
    Attributes:
        total (int): The total number of chips the player has.
        bet (int): The number of chips the player has bet.
        
        Methods:
        win_bet: Increases the total number of chips by the bet amount.
        lose_bet: Decreases the total number of chips by the bet amount.
    """
    def __init__(self):
        """
        Initializes a Chips object with a default total of 100 chips and no bet.
        
        Parameters:
        None
        
        Returns:
        None
        
        """
        self.total = 100  # default starting chips
        self.bet = 0

    def win_bet(self):
        """
        Increases the total number of chips by the bet amount.
        
        This method increases the total number of chips by the bet amount when the player wins a hand.
        
        Parameters:
        None
        
        Returns:
        None
        
        Example:    
        chips.win_bet()
        """
        self.total += self.bet

    def lose_bet(self):
        """
        Decreases the total number of chips by the bet amount.

        This method decreases the total number of chips by the bet amount when the player loses a hand.

        Parameters:
        None

        Returns:
        None

        Example:
        chips.lose_bet()
        """
        self.total -= self.bet
