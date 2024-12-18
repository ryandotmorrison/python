# Snake Game

A classic snake game with a modern twist using the Codesters platform! Navigate the snake to eat apples, grow longer, and avoid crashing into walls or itself.

---

## Features

- **Dynamic Snake Growth**: Eat apples to grow the snake and increase your score.
- **Score Tracking**: Real-time score updates displayed on the screen.
- **Responsive Controls**: Use arrow keys to change the snake's direction.
- **Collision Mechanics**: Game ends if the snake crashes into the walls or itself.

---

## How to Play

1. **Start the Game**:
   - The game begins with a small snake in the center of the stage.
   - A red apple appears at a random location.
2. **Control the Snake**:
   - Use the arrow keys to guide the snake towards the apple.
3. **Grow and Score**:
   - Eating an apple increases your score and grows the snake.
4. **Avoid Crashing**:
   - The game ends if the snake crashes into the walls or its own body.

---

## Controls

- **Arrow Keys**:
  - **Left**: Move left.
  - **Right**: Move right.
  - **Up**: Move up.
  - **Down**: Move down.

---

## Code Overview

### Core Components

- **Snake**:
  - Represented as a list of coordinates (`snake_xy`).
  - Grows by adding a segment when eating an apple.
- **Apple**:
  - Randomly spawns on the grid after being eaten.
  - Represented as a red circle (`a`).
- **Score**:
  - Tracks the number of apples eaten.
  - Displayed using a `Text` object (`score_text`).

### Functions

- **Movement**:
  - Direction controlled by global variables `dx` (horizontal) and `dy` (vertical).
  - Updated by arrow key events.
- **Apple Collision** (`chomp`):
  - Checks if the snake's head is at the same position as the apple.
  - Increases score, spawns a new apple, and triggers snake growth.
- **Crash Detection** (`crash`):
  - Ends the game if the snake collides with the walls or itself.
- **Main Loop** (`main`):
  - Continuously updates the snake's position.
  - Handles growth, collision detection, and rendering.

---

## Game Mechanics

1. **Movement**:
   - The snake moves in a grid-like pattern, updating its position based on `dx` and `dy`.
2. **Apple Eating**:
   - When the snake eats an apple, it grows by one segment, and the score increases.
3. **Collision**:
   - The game ends if:
     - The snake's head moves outside the grid boundary.
     - The snake's head collides with any part of its body.
4. **Score Display**:
   - The score is dynamically updated on the screen.

---

## Customization

- **Grid Size**:
  - Adjust the grid by changing the boundary values in the `crash` function.
- **Speed**:
  - Modify the game speed by adjusting the delay in `stage.wait()` inside the `main` loop.
- **Apple Appearance**:
  - Change the apple's color or size in the `chomp` function.
- **Snake Appearance**:
  - Customize the snake's color or size in the `main` function.

---

## Future Enhancements

- **Levels**:
  - Introduce levels with increasing speed or obstacles.
- **High Scores**:
  - Add a feature to save and display high scores.
- **Power-Ups**:
  - Include special apples with unique effects (e.g., double points, temporary speed boost).
- **Sound Effects**:
  - Add audio for eating apples or crashing.

---

## License

This project is open-source and free to use or modify for educational purposes.

---

Enjoy playing **Snake Game**, and see how long you can grow your snake!
