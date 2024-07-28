# Code Institute Protfolio 3: BlackJack

## BlackJack
The aim of this project was to create a BlacJack game to equally satisfy the
project requirements as well as offer the user a fun experience within the CLI 
limiations.
The game was programmed in Pyhton and utilises the Code Institute python
template to deploy it on Heroku.

## Table of Contents




## User Expeirience
### The Strategy Plane
The primary objective of this project is to create an engaging and user-feiendly text-based BlackJack game that can be played interactively in a terminal window. The game aims to provide a seemless and enjoyable experience for users with clear instructionsm intuitive and engagine gameplay and promt and accurate feedback on their actions.

#### User needs:
* Entertianment: Users seek an enjoyable and challenging card game that can be played in short sessions. 
* Clarity: Users need clear instructions and feedback to understand the out come of their actions.
* Progress Tracking: Users want to keep track of progress or successess, the highscores table is a means of doing this.

### The Scope Plane
#### Functional Specifications
* Gameplay Mechanics: Implement code BlackJack rules including dealing cards, player actions, win/loss conditions and high score tracking.
* Betting System: Allow the users to place bets and update their chip blance based on round outcomes.
* High Scores: Keep a record of top scores and display them when requested.
* User Prompts: Provide clear and timely feedback to the user's actions.

#### Content Requirements
* Game Instructions: Provide a brief overview of the game rules and how to play.
* Feedback Messages: Display messages for the outcomes of game actions as well as invalid inputs through out the game.
* High Scores Display: Keep track and display on request the top three scores. Prompt the user to add thier initals to the record
git 
### The Structure Plane
#### Interaction Design 
* Main Menu: offers options to start new game, view high scores, exit.
* Game loop: Guide the users through the game round from placing bets to playing their hand, concluding the round and updating the players chip balance.
* User Input: Promt the user for inputs and continously validate the users inputs.
* Feedback and Instructions: Provide real-time feedback and instuctions based on the user's actions in game.

#### Infomation Architecture
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
 * Current Chip balance and bet ammount
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
