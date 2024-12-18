# Tic-Tac-Toe Game

A simple two-player Tic-Tac-Toe game built with Codesters. Players alternate between placing "X" and "O" on a 3x3 grid. The game detects the winner after each move and ends when a player wins or all the boxes are filled.

---

## Features

- **Two Players**: Players alternate turns between placing "X" and "O".
- **Grid System**: A 3x3 grid is used to play the game.
- **Winner Detection**: The game checks for a winner after each move, either horizontally, vertically, or diagonally.
- **Game Over**: The game ends when there is a winner, and a message is displayed.

---

## How to Play

1. **Start the Game**:
   - The game starts with an empty 3x3 grid.
2. **Player Turns**:
   - Player 1 places an "X" in an empty square.
   - Player 2 places an "O" in an empty square.
   - Players alternate turns, and the game tracks whose turn it is.
3. **Winning the Game**:
   - A player wins by aligning three of their marks ("X" or "O") in a row, either horizontally, vertically, or diagonally.
   - Once a player wins, a message is displayed, and the game ends.
4. **Game Over**:
   - The game will end when a player wins, or if all squares are filled with no winner.

---

## Controls

- **Mouse Click**:
  - Click on an empty square in the grid to place your mark ("X" or "O").

---

## Code Overview

### Key Components

1. **Grid**:
   - The grid is created dynamically using `codesters.Square` objects. Each square is clickable and will hold either an "X" or "O".
   
2. **Turn Logic**:
   - The game alternates between Player 1 (X) and Player 2 (O). The `turn` variable tracks the current player's turn.
   
3. **Player Input**:
   - When a square is clicked, the game checks if the square is empty. If it is, the current player’s mark is placed in the square, and the turn alternates.
   
4. **Winner Detection**:
   - After every move, the game checks for a winning combination of three marks in a row (horizontally, vertically, or diagonally).
   - The `check_winner` function verifies all possible winning conditions.
   
5. **Game Over**:
   - If there is a winner, the game ends, and a message such as "X WINS!" or "O WINS!" is displayed.
   - No further moves are allowed after the game ends.

### Main Functions

- **`make_board()`**:
  - Creates a 3x3 grid of squares for the Tic-Tac-Toe game board.
  
- **`click(sprite)`**:
  - Handles player input, placing "X" or "O" in the clicked square and checks for a winner after each move.
  
- **`check_boxes(b1, b2, b3)`**:
  - Checks three squares for a winning combination. If all three squares contain the same mark, the game announces the winner.

- **`check_winner()`**:
  - Checks all possible winning combinations on the board.

---

## Future Enhancements

- **Draw Condition**:
  - Add logic to detect if the game ends in a draw (when all squares are filled without a winner).
  
- **Restart Option**:
  - Include a button or option to restart the game after it ends.
  
- **AI Player**:
  - Implement a basic AI to allow a single player to play against the computer.
  
- **Styling**:
  - Customize the game board with different colors or themes.

---

## License

This game is open-source and available for educational purposes and modifications.

---

Enjoy playing Tic-Tac-Toe!
