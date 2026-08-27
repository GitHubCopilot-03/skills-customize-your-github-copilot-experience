# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python using strings, loops, and conditionals. By the end of this assignment, you will implement game logic that tracks guesses, updates progress, and handles win/loss outcomes.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Create the initial game setup in `starter-code.py`, including a word list, random word selection, and variables needed to track player progress.

#### Requirements
Completed program should:

- Store at least 5 possible words in a predefined list.
- Randomly choose one word as the secret word.
- Create a progress view that shows unknown letters as underscores (for example: `_ _ _ _`).
- Initialize a counter for remaining incorrect guesses.

### 🛠️ Implement the Guessing Loop

#### Description
Write the main game loop where the player enters one letter at a time, receives feedback, and continues until the game ends.

#### Requirements
Completed program should:

- Prompt the player to enter a single letter each turn.
- Update and display the current word progress after each guess.
- Decrease remaining attempts only for incorrect guesses.
- End the game with a clear win message when the word is fully guessed.
- End the game with a clear lose message when attempts reach zero and reveal the secret word.
