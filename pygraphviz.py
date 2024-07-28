"""
This script creates a class diagram for the BlackJack game using the graphviz library.

The class diagram shows the relationships between the classes Deck, Card, Hand, Chips, and Database.
The Deck class contains Card objects, the Hand class contains Card objects, the Deck class deals to 
the Hand class,the Game class uses the Deck and Hand classes, the Game class manages the Chips
class, and the Game class records to the Database class.

The class diagram is saved as a png file named 'BlackJack_class_diagram.png'.
"""
from graphviz import Digraph

dot=Digraph(comment='BlackJack Class Diagram')

dot.node('Deck', 'Deck')
dot.node('Card', 'Card')
dot.node('Hand', 'Hand')
dot.node('Chips', 'Chips')
dot.node('Database', 'Database')
dot.edge('Deck', 'Card', label='contains')
dot.edge('Hand', 'Card', label='contains')
dot.edge('Deck', 'Hand', label='deals to')
dot.edge('Game', 'Deck', label='uses')
dot.edge('Game', 'Hand', label='uses')
dot.edge('Game', 'Chips', label='manages')
dot.edge('Game', 'Database', label='records')
dot.render('BlackJack_class_diagram', format='png', view=True)
