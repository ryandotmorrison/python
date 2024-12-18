# Pokémon Quiz Game

Test your Pokémon knowledge with this interactive multiple-choice quiz game! Answer fun questions about Pokémon regions, numbers, types, and more. See how many questions you can get right out of 5!

---

## Features

- **Interactive Questions**: Five Pokémon-themed multiple-choice questions to challenge your knowledge.
- **Real-Time Feedback**: Displays "Correct!" or "Wrong!" for each answer.
- **Score Tracking**: Keeps track of correct answers and shows your total score at the end.
- **Colorful UI**: Dynamic text updates with a visually engaging background.

---

## How to Play

1. Each question appears with four answer choices labeled A, B, C, and D.
2. Click on the correct answer using your mouse.
3. Receive instant feedback on whether your choice was correct or not.
4. At the end of the quiz, see your final score out of 5.

---

## Controls

- **Mouse Click**: Select an answer by clicking on it.

---

## Code Overview

### Core Components

- **Questions and Answers**:
  - Questions (`q`) and their answer options (`a`) are stored in lists.
  - Correct answers are linked to specific text objects (`ca`).
- **Dynamic UI**:
  - The question text (`qText`) and answer options (`aText`, `bText`, `cText`, `dText`) update dynamically for each question.
- **Feedback Display**:
  - The `display` object shows messages like "Correct!" or "Wrong!" and the final score.

### Functions

- **`createQ()`**: Creates the questions, answer options, and correct answers.
- **`showQ()`**: Displays the current question and its options.
- **`nextQ()`**: Advances to the next question or ends the game.
- **`click(choice)`**: Handles user clicks, checks answers, updates the score, and moves to the next question.

---

## Game Mechanics

- **Question Flow**:
  - The quiz starts with the first question and proceeds sequentially.
  - Questions and answer options are displayed dynamically.
- **Scoring**:
  - Correct answers increment the score.
  - The final score is displayed after all questions are answered.

---

## Example Quiz Questions

1. **Question**: How many regions are in Pokémon?  
   **Options**: 1, 5, 10, 18  
   **Answer**: 10

2. **Question**: How many different Pokémon are there?  
   **Options**: 500, 750, 1,025, 1,000  
   **Answer**: 1,025

---

## Customization

- **Add More Questions**:
  - Update the `createQ()` function with new questions and answers.
- **Change Appearance**:
  - Modify text colors, fonts, or the stage background to match a specific theme.
- **Scoring System**:
  - Add bonus points for faster responses or introduce difficulty levels.

---

## Future Improvements

- Add a timer to make the quiz more challenging.
- Include animations or sound effects for correct and incorrect answers.
- Introduce levels with progressively harder questions.

---

## License

This project is open-source and free to use or modify for educational purposes.

---

Enjoy playing the **Pokémon Quiz Game** and test your knowledge of the Pokémon universe!
