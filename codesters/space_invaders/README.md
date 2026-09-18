# Space Invader Shooter Game

Defend your rocket from waves of alien invaders in this interactive space-themed shooter game built using Codesters. Use your rocket to shoot down aliens while avoiding their bullets. Can you survive and eliminate all invaders before running out of lives?

---

## Features

- **Dynamic Alien Waves**: Aliens move left, right, and down the screen as they fire bullets at the player.
- **Player Controls**: Move the rocket left or right and fire lasers to destroy the aliens.
- **Collision Detection**: Detect hits on aliens or the player's rocket and update the game state accordingly.
- **Victory or Defeat**: Win by eliminating all aliens or lose when your lives reach zero.

---

## How to Play

1. Use the **left** and **right arrow keys** to move your rocket horizontally.
2. Press the **spacebar** to shoot lasers.
3. Avoid alien bullets while targeting alien invaders.
4. Win by eliminating all aliens before your lives (5) run out.

---

## Controls

- **Left Arrow Key**: Move the rocket left.
- **Right Arrow Key**: Move the rocket right.
- **Spacebar**: Fire lasers.

---

## Code Overview

### Core Components

- **Player Rocket**: Controlled by the player to navigate the stage and fire lasers.
- **Aliens**: A grid of invaders that move horizontally, descend over time, and fire bullets.
- **Lives**: The player starts with 5 lives, losing one for each hit from an alien bullet.
- **Game Over**: Triggered when all aliens are destroyed (win) or the player runs out of lives (loss).

### Functions

- **`createAliens()`**: Generates a grid of alien invaders.
- **`left_key()` / `right_key()`**: Move the player’s rocket left or right.
- **`space_bar()`**: Fires a laser from the player’s rocket.
- **`alienMove(steps)`**: Moves the aliens horizontally and down the screen, firing bullets randomly.
- **`alienCollision()`**: Handles collisions between lasers and aliens, removing hit aliens.
- **`playerCollision()`**: Handles collisions between alien bullets and the player, reducing lives.

---

## Game Mechanics

- **Alien Movement**:
  - Aliens move horizontally and descend incrementally.
  - They fire bullets randomly as they move.
- **Player Actions**:
  - The player can shoot lasers, which destroy aliens on collision.
- **Victory/Defeat**:
  - Victory: All aliens are eliminated.
  - Defeat: Lives reach zero.

---

## Customization

- **Difficulty Levels**:
  - Adjust `lives` to change player endurance.
  - Modify alien firing frequency in `alienShoot()`.
- **Graphics**:
  - Replace rocket or alien sprites for a personalized look.
- **Stage Background**:
  - Change the background to fit a new theme.

---

## Example Game Playthrough

1. Player starts with 5 lives.
2. Aliens move down the screen, firing bullets.
3. The player avoids bullets and shoots down all aliens to win.

---

## Future Improvements

- Add levels with increasing difficulty.
- Introduce power-ups for the player (e.g., multi-shot lasers).
- Implement a scoring system.
- Include sound effects for laser fire, collisions, and game-over events.

---

## License

This project is open-source and free to modify for educational and recreational purposes.

---

Enjoy playing **Space Invader Shooter**!
