# Hangman Game with Codesters

An interactive Hangman game built using the Codesters platform. Guess the letters of a randomly chosen word, and avoid losing all your guesses before the hangman is fully drawn!

---

## Features

- **Interactive Gameplay**: Guess letters through a wizard sprite with real-time feedback.
- **Dynamic Word Display**: Correct guesses reveal letters in the word.
- **Visual Hangman Drawing**: A turtle graphics-based hangman figure is drawn step-by-step as guesses are lost.
- **Random Word Selection**: Words are chosen at random from a predefined list.

---

## How to Play

1. The wizard will prompt you to guess a letter.
2. Input a single letter per guess.
3. Correct guesses will update the word display.
4. Incorrect guesses will draw a part of the hangman.
5. The game ends when:
   - You guess the entire word, or
   - The hangman figure is fully drawn after 6 incorrect guesses.

---

## Controls and Rules

- **Valid Inputs**: Only single alphabetic characters are allowed.
- **Case-Insensitive**: Inputs are converted to lowercase for consistency.
- **Repeat Prevention**: The same letter cannot be guessed twice.

---

## Code Overview

### Key Components

- **Game Logic**: 
  - Word selection from a predefined list.
  - Tracking correct guesses and remaining attempts.
- **Visual Updates**:
  - A list of text objects (`word_display`) represents the hidden word.
  - Turtle graphics draw the hangman figure incrementally.
- **Interactive Input**: 
  - The sprite (`gg`) provides prompts and feedback to the player.

### Functions

- **`drawhangman()`**: Draws each part of the hangman based on remaining guesses.
- **`update_display()`**: Updates the word display with correctly guessed letters.
- **`checkword()`**: Checks if the word is completely guessed.

---

## Example Game Playthrough

- Word: **holiday**
- Guesses:
  - Correct: `h`, `o`, `l`, `i`, `d`, `a`, `y`
  - Incorrect: `x`, `z`
- Outcome:
  - Victory: "Congratulations! You guessed the word!"
  - Loss: The hangman is fully drawn.

---

## Customization

- **Add More Words**: Update the `random_words` list with new words.
- **Difficulty Levels**: Adjust the number of allowed guesses (`no_guesses`).
- **Graphics**: Customize the hangman drawing in the `drawhangman()` function.

---

## Future Improvements

- Add a scoring system.
- Include word hints for challenging words.
- Support for multi-word phrases.

---

## License

This project is open-source and available for anyone to use and modify for educational purposes.

---

Enjoy playing the **Hangman Game** with Codesters!
