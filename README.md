# Code Institute Protfolio 3: BlackJack

## BlackJack
The aim of this project was to create a BlackJack game to equally satisfy the project requirements as well as offer the user a fun experience within the CLI limitations. The game was programmed in Python and utilizes the Code Institute Python template to deploy it on Heroku.

## Table of Contents
- [User Experience](#user-expeirience)
  - [The Strategy Plane](#the-strategy-plane)
  - [The Scope Plane](#the-scope-plane)
  - [The Structure Plane](#the-structure-plane)
  - [The Skeleton Plane](#the-skeleton-plane)
  - [The Surface Plane](#the-surface-plane)
- [Code Architecture](#code-architecture)
  - [File Structure](#file-structure)
  - [Reasons for Separation of Files](#reasons-for-separation-of-files)
- [Class Diagram](#class-diagram)
- [Flow Diagram](#flow-diagram)
- [Features](#features)
- [Testing](#testing)
- [Validation Testing](#validation-testing)
- [Libraries Used](#libraries-used)
- [Project Setup](#project-setup)
- [Deployment](#deployment)
- [Credits](#credits)
- [Thanks](#thanks)

## User Experience
### The Strategy Plane
The primary objective of this project is to create an engaging and user-friendly text-based BlackJack game that can be played interactively in a terminal window. The game aims to provide a seamless and enjoyable experience for users with clear instructions, intuitive and engaging gameplay, and prompt and accurate feedback on their actions.

#### User needs:
* Entertainment: Users seek an enjoyable and challenging card game that can be played in short sessions. 
* Clarity: Users need clear instructions and feedback to understand the out come of their actions.
* Progress Tracking: Users want to keep track of progress or successes, the highscores table is a means of doing this.

### The Scope Plane
#### Functional Specifications
* Gameplay Mechanics: Implement code BlackJack rules including dealing cards, player actions, win/loss conditions and high score tracking.
* Betting System: Allow the users to place bets and update their chip balance based on round outcomes.
* High Scores: Keep a record of top scores and display them when requested.
* User Prompts: Provide clear and timely feedback to the user's actions.

#### Content Requirements
* Game Instructions: Provide a brief overview of the game rules and how to play.
* Feedback Messages: Display messages for the outcomes of game actions as well as invalid inputs through out the game.
* High Scores Display: Keep track of and display on request the top three scores. Prompt the user to add their initials to the record

### The Structure Plane
#### Interaction Design 
* Main Menu: offers options to start new game, view high scores, exit.
* Game loop: Guide the users through the game round from placing bets to playing their hand, concluding the round and updating the players chip balance.
* User Input: Prompt the user for inputs and continously validate the users inputs.
* Feedback and Instructions: Provide real-time feedback and instructions based on the user's actions in game.

#### Information Architecture
* Main Menu: A central hub for accessing the program elements.
* Game Screen: Display game-related information such as the player's and dealer's hands, chip counts and betting options.
* High Scores Screen: Show the top scores and provide an option to return to the main menu.

### The Skeleton Plane
#### Interface Design
* Main Menu
  * Title: BlackJack
  * Options: 1. New Game, 2. View High Scores, 3. Exit
* Game Screen:
 * Player and dealer hands displayed, dealer has a card face down.
 * Current Chip balance and bet amount
 * Action prompts for hitting, standing and placing bets.
 * Clear feedback messaging on game outcomes.
* High Scores Screen
 * List of three highest scores.
 * Prompt to return to the main menu.

### The Surface Plane
#### Visual design
* Text Styling: Use colours and text styles to differentiate between different types of information.
* ASCII Art: Include an ASCCI art header for the main menu
* Colour Scheme: Use a colour scheme to make the information easier for the user to read and understand e.g. green for player actions, yellow for important messages.


## Code Architecture

### File Structure
The project is organised into several files to ensure modularity, maintainability and clarity. The files are as follows:
#### run.py
This is the main entry point of the application and handles the game flow and user interactions.
#### app/game/game.py
This is the file where the game logic and rules for BlackJack are held. The reason these rules are kept in a separate file is so that they can be reused or modified to create a new game variant.
#### app/database/database.py
This is the file that controls the database interactions and management. Having this file is best practice for DB related code.

### Reasons for separation of files
**Game File (game.py)**
-**Reusability:** Isolating the game logic allows for easy reuse in other card games or new varients of BlackJack.
_**Maintainability:** Keeping the game rules separate makes it easier to update and debug the game logic without affecting the application flow.
_**Clarity:** Makes the code easier to read and understand by distinguishing between the game rules and the functionality of the rest of the application

**Database File (database.py)**
-**Seperation of concerns:** Allows for the DB operations to be managed separately from the main game logic as is best practice for DB operations.
_**Scalability:** Keeping the game rules and logic segregated from the DB operations allows for expansion of the DB features without cluttering the main application logic.
_**Common Practice:** As outlined in the Model-View-Controller (MVC) architecture, separating the application into distinct components is a preferred principle.

## Class Diagram

This is a diagram of the strucutre of the classes in the BlackJack game:

![class Diagram](./readme%20assets/images/BlackJack_class_diagram.png)

The diagram was created with GraphViz and the following code:
```
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
```
## Flow Diagram

The flow diagram is a representation of the game logic flow for the BlackJack game:

![Flow Diagram](./readme%20assets/images/BlackJack_flow.png)

Diagram was created using draw.io

## Features
 Here is a gallery of the main interactions of the client.

 #### Main Menu
 ![Main Menu](./readme%20assets/images/main_menu.png)

 This is the main menu presented to the user on launch.


 #### High Scores
 ![High Scores](./readme%20assets/images/high_scores.png)

 This is the High Scores screen containing the highest three scores.

 #### Start New Game
 ![New Game Start](./readme%20assets/images/new_game_start.png)

 The screen that the user sees after starting a new game. This is where the user's input is taken and validated for the bet ammount for the round.

 #### First Deal
 ![First Deal](./readme%20assets/images/first_deal.png)

 This is the first deal. The dealer's cards a clearly deliniated from the players by different colours. The action is on the user to hit or stand. The input is validated.

 #### Player Busts
 ![Player busts](./readme%20assets/images/player_busts.png)

 This is what it looks like when the player busts.

 #### Player Wins
 ![Player wins](./readme%20assets/images/player_wins.png)

 In this instance, the player wins.

 #### Black Jack
 ![Player BlackJack](./readme%20assets/images/player_blackJack.png)

 This is a BlackJack for the user.

 #### Player not enough chips
 ![Player broke](./readme%20assets/images/player_not_enough_chips.png)

 This is what happens when the player attempts to bet more chips than they have.

 #### Player game over - No High Score
 ![Game over - no high score](./readme%20assets/images/player_game_over.png)

This is the game over screen when the player does not achieve a high score.

#### Player game over - High Score
![Game over - enter high score](./readme%20assets/images/player_enter_hiscore.png)

This is what the user sees if they end the game and have achieved a highscore. The user's input is validated.

#### Heroku Terminal Styling
![Heroku terminal](./readme%20assets/images/heroku_terminal.png)

I edited the Heroku terminal layout.html to center the terminal window and themed the colours to enhance the BlackJack theme.

## Testing

The testing for this project was conducted using an ad-hoc approach following the principles of rapid prototyping. Below is a detailed test script outlining some of the key tests that were performed:


### 1. Main Menu

| Test Case                   | Action                                           | Expected Result                                                               | Pass/Fail |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| Display Main Menu           | Run the application                              | The main menu is displayed with options: 1. New Game, 2. View High Scores, 3. Exit |  pass     |
| Invalid Main Menu Input     | Enter an invalid choice (e.g., '4' or 'abc')     | An error message is displayed: "Invalid choice. Please enter 1, 2, or 3."     |  pass     |

### 2. New Game

| Test Case                   | Action                                           | Expected Result                                                               | Pass/Fail |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| Start New Game              | Select option '1' at the main menu               | The screen clears, and the player is prompted to enter a bet.                 |  pass     |
| Place Valid Bet             | Enter a valid bet amount within the player's chip balance | The game starts, and the initial hands are dealt.                        |  pass     |
| Place Invalid Bet (Non-numeric) | Enter a non-numeric bet amount (e.g., 'abc')  | An error message is displayed: "Bet needs to be a positive number."           |    pass   |
| Place Invalid Bet (Exceeds Balance) | Enter a bet amount greater than the player's chip balance | An error message is displayed: "You do not have enough chips." |    pass   |

### 3. Game Play

| Test Case                   | Action                                           | Expected Result                                                               | Pass/Fail |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| Player Hit                  | Enter 'h' to hit                                 | A new card is dealt to the player, and the updated hand is displayed.         |  pass     |
| Player Stand                | Enter 's' to stand                               | The dealer's turn begins, and the dealer's hand is revealed.                  |  pass     |
| Player Bust                 | Continue hitting until the player's hand value exceeds 21 | A message is displayed: "Player busts!" and the game round ends.    |  pass     |
| Dealer Bust                 | Stand with a hand value that causes the dealer to bust | A message is displayed: "Dealer busts! Player wins!" and the player's chip balance is updated. | pass      |
| Dealer Wins                 | Stand with a hand value lower than the dealer's final hand value | A message is displayed: "Round Over - Dealer wins!" and the player's chip balance is updated. |   pass    |
| Player Wins                 | Stand with a hand value higher than the dealer's final hand value | A message is displayed: "Round Over - Player wins!" and the player's chip balance is updated. |  pass     |
| Push                        | Stand with a hand value equal to the dealer's final hand value | A message is displayed: "Dealer and Player tie! It's a push." and the player's bet is returned. |   pass    |

### 4. High Scores

| Test Case                   | Action                                           | Expected Result                                                               | Pass/Fail |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| View High Scores            | Select option '2' at the main menu               | The high scores table is displayed.                                           |  pass     |
| Enter High Score            | Achieve a high score and enter initials when prompted | The initials and score are recorded, and the high scores table is updated. |   pass    |
| Invalid Initials for High Score | Enter invalid initials (e.g., '123' or 'abcd') when prompted for high score initials | An error message is displayed: "Invalid input. Please enter 1-3 letters." |   pass    |

### 5. Exit

| Test Case                   | Action                                           | Expected Result                                                               | Pass/Fail |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| Exit Game                   | Select option '3' at the main menu               | The application exits with a message: "Thank you for playing!"                |   pass    |

### 6. Database Operations

| Test Case                   | Action                                           | Expected Result                                                               | Pass/Fail |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| High Scores Persist Between Sessions | Achieve a high score, exit the game, and restart the game | The high scores table retains the high score from the previous session. |   pass    |

### 7. Edge Cases

| Test Case                   | Action                                           | Expected Result                                                               | Pass/Fail |
|-----------------------------|--------------------------------------------------|-------------------------------------------------------------------------------|-----------|
| Both Player and Dealer Have Blackjack | Deal initial hands where both the player and dealer have blackjack | A message is displayed: "Both Blackjack! It's a push." |  pass      |
| Player with Two Aces        | Deal initial hands where the player receives two aces | One ace is counted as 11, and the other is counted as 1, resulting in a hand value of 12. |  pass      |

### Validation Testing
The code was validated using the Pylint (https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) plugin on Visual studio code. Errors found by the linter were white spaces & lines going past the 79th char limit. All of the issues reported by linter were resolved. 

## Libraries used
#### re
The Regular Expression library is used for character validation

#### os
The os library is used to make the game space easier to follow by calling the clearscreen() function when the need arose to have a screen refresh.

#### rich
The rich library allows for the colouring of text and easy display of ASCII art.

## Project Setup
To setup the project locally, follow these steps:
### 1. Clone Repository:
```
git clone https://github.com/dutes/ci_portfolio_three.git
cd ci_portfolio_three
```

### 2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependancies:
```
pip install -r requirements.txt
```

### 4. Run the application:
```
python run.py
```

## Deployment
The application was deployed on Heroku using the Code Institute template and instructions.
Once you created a Heroku account and linked it to your Github account you must follow these steps:
1. Open the Heroku dashboard and select click on the 'new' button in the top right corner, followed by create new
2. Give your app a name and chose the European region, then click 'create app' (app name must be unique)
3. Click on the settings tab.
4. Click on reveal config vars, enter PORT in the KEY input field and 8000 in the value, then click the add button.
5. scroll down to Buildpacks section.
6. Click 'Add buildpacks' and select Python form the list, click save changes. 
7. Click 'Add buildpacks' again and select node.js this time. click save changes.
8. Click on the deploy tab.
9. Click on the 'Connect to Github' button, then select the repository.
10. Tap to connect to confirm the repository.
11. Select the branch from which to deploy from.
12. Click on the enable Automatic deploys if desired other wise click 'deploy branch'
13. Heroku will attempt to deploy the application
14. Once successful, tap on the open app button to see your app running on Heroku.

The app is currently deployed here:
https://dutes-ci-portfolio3-a902468546c1.herokuapp.com/

## Credits
* Real Python -  https://realpython.com/ for general Python knowlege.
* FreeCodeCamp - https://www.freecodecamp.org/news/use-the-rich-library-in-python/ Rich tutorial 
* Automate the Boring stuff - Book (https://nostarch.com/automatestuff2)

## Thanks
Thanks to my mentor Matt Bodden for the guidance. 