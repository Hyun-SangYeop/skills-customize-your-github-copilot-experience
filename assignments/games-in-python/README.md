# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple text-based game in Python using loops, conditionals, strings, and user input while practicing program flow and game logic.

## 📝 Tasks

### 🛠️ Hangman Game Setup

#### Description
Create a basic Hangman game where the player guesses letters to reveal a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Use a predefined list of words and randomly choose one for each round.
- Show the hidden word as underscores, such as `_ _ _ _ _`.
- Prompt the user to enter a single letter guess.
- Reveal correctly guessed letters in the correct positions.
- Example output:
  ```python
  Word: _ _ _ _ _
  Enter a letter: a
  Word: a _ _ a _
  ```

### 🛠️ Guess Tracking and Lives

#### Description
Add logic to track incorrect guesses and limit how many chances the player has before the game ends.

#### Requirements
Completed program should:

- Start with a fixed number of lives, such as 6.
- Decrease the remaining lives when the player guesses a wrong letter.
- Display the number of incorrect guesses or remaining attempts.
- Prevent repeated guesses from counting multiple times.
- Example output:
  ```python
  Incorrect guesses: 2
  Remaining attempts: 4
  ```

### 🛠️ Win and Lose Conditions

#### Description
Finish the game by checking whether the player won or lost and presenting a clear result.

#### Requirements
Completed program should:

- End the game when the player correctly guesses the full word.
- End the game when the player runs out of attempts.
- Print a final message indicating whether the player won or lost.
- Example output:
  ```python
  Congratulations! You guessed the word: python
  ```
  or
  ```python
  Game over! The word was: python
  ```
