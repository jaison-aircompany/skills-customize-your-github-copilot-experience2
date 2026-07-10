# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a complete Hangman game in Python where the player guesses letters to reveal a hidden word. In this assignment, you will practice using strings, loops, conditionals, and user input to control game flow.

## 📝 Tasks

### 🛠️	Set Up the Game Data

#### Description
Create the basic game setup by defining a word list, selecting one random word, and preparing the variables needed to track progress.

#### Requirements
Completed program should:

- Store at least 5 possible words in a predefined list.
- Randomly choose one word at the start of each game.
- Create a progress display using underscores (for example: `_ _ _ _ _`).
- Set a fixed number of incorrect guesses allowed.


### 🛠️	Implement the Guessing Loop

#### Description
Build the main game loop that asks for letter guesses, updates progress, tracks incorrect attempts, and ends with a clear result message.

#### Requirements
Completed program should:

- Ask the player to enter one letter at a time.
- Reveal matching letters in all correct positions.
- Decrease remaining attempts only for incorrect guesses.
- End the game with a win message if the word is fully revealed.
- End the game with a lose message and show the correct word if attempts run out.
