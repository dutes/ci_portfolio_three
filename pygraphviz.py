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

dot.render('BlackJack_class_diagram', format='png',view=True)