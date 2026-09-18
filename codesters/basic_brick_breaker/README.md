# Brick Breaker Game

A classic brick-breaking game created with the Codesters platform! Control the paddle, bounce the ball, and clear all the bricks to win.

---

## Features

- **Interactive Paddle**: Move the paddle left or right to keep the ball in play.
- **Dynamic Ball Movement**: The ball bounces off the paddle and bricks with randomized angles.
- **Brick Destruction**: Break bricks by hitting them with the ball to score.
- **Game Over Condition**: The game ends if the ball touches the bottom of the screen.

---

## How to Play

1. **Start the Game**:
   - The game begins with a ball bouncing on the screen and a paddle at the bottom.
   - Rows of bricks are arranged at the top of the screen.
2. **Control the Paddle**:
   - Use arrow keys to move the paddle left or right.
3. **Break the Bricks**:
   - Use the ball to hit and remove bricks from the screen.
4. **Avoid Missing the Ball**:
   - If the ball falls below the paddle, the game ends.

---

## Controls

- **Arrow Keys**:
  - **Left**: Move paddle left.
  - **Right**: Move paddle right.

---

## Code Overview

### Core Components

- **Paddle**:
  - Represented as a red rectangle (`player`).
  - Controlled by the player using arrow keys.
- **Ball**:
  - Represented as a blue circle (`b`).
  - Moves continuously, bouncing off surfaces.
- **Bricks**:
  - Represented as green rectangles (`brick_list`).
  - Arranged in rows at the top of the screen.

### Functions

- **Build Bricks** (`build_bricks`):
  - Dynamically creates a grid of bricks at the start of the game.
- **Paddle Movement**:
  - Controlled by the `left_key` and `right_key` functions.
- **Ball Collision** (`collision`):
  - Handles ball interaction with the paddle and bricks.
  - Adjusts ball speed and direction upon collision.
  - Removes bricks when hit.
- **Floor Collision** (`floor_collision`):
  - Detects when the ball falls below the paddle to end the game.
- **Main Game Loop** (`main`):
  - Continuously updates the game until all bricks are destroyed or the ball hits the bottom.

---

## Game Mechanics

1. **Ball Movement**:
   - The ball starts with randomized x and y speeds.
   - Bounces off the paddle, walls, and bricks.
2. **Brick Destruction**:
   - Each brick hit is removed from the stage and the `brick_list`.
3. **Win Condition**:
   - All bricks are cleared from the screen.
4. **Lose Condition**:
   - The ball falls below the paddle and touches the bottom of the screen.

---

## Customization

- **Brick Layout**:
  - Modify the `build_bricks` function to change the number of rows or columns of bricks.
- **Ball Speed**:
  - Adjust the initial values of `y_speed` and `x_speed` for difficulty.
- **Paddle Size**:
  - Change the dimensions of the `player` rectangle to increase or decrease the paddle's size.
- **Ball Appearance**:
  - Customize the ball's size or color in its declaration (`b`).

---

## Future Enhancements

- **Levels**:
  - Add multiple levels with different brick layouts and increased ball speeds.
- **Power-Ups**:
  - Introduce special bricks that drop power-ups when hit (e.g., paddle size increase, multiple balls).
- **Scoring System**:
  - Add a score counter to track points for breaking bricks.
- **Sound Effects**:
  - Include audio feedback for collisions and brick destruction.
- **Game Over Screen**:
  - Display a message when the player wins or loses.

---

## License

This project is open-source and available for educational use and modifications.

---

Enjoy playing **Brick Breaker Game**, and see how many bricks you can smash!
