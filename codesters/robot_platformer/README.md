# Underwater Adventure Platformer

Welcome to **Underwater Adventure**, an interactive platformer game built with Codesters. Guide your robot character through an underwater world filled with platforms, walls, and collectible coins while avoiding obstacles. Reach the end to win!

---

## Features

- **Dynamic Gameplay**: Control a robot character with smooth movement and jumping mechanics.
- **Interactive Physics**: Realistic gravity and collision detection with platforms and walls.
- **Collectibles**: Gather coins to complete the level.
- **Win Condition**: Collect all coins to win the game.

---

## How to Play

### Controls
- **Arrow Keys**:
  - **Right**: Move the robot to the right.
  - **Left**: Move the robot to the left.
  - **Up**: Jump upward.
- **Space Bar**: Perform a jump if not already in the air.

### Objective
1. Move across platforms and walls to collect all the coins.
2. Avoid falling off platforms.
3. Collect every coin to win and display the victory message.

---

## Code Overview

### Core Components
- **Robot Sprite**: Main character controlled by the player.
- **Platforms**: Various static obstacles and platforms to jump onto.
- **Coins**: Collectibles scattered throughout the level.
- **Gravity**: Enables realistic jumping and falling mechanics.

### Functions
- **`createPlats()`**: Generates platforms and walls.
- **`addCollectables()`**: Places coins in specific locations.
- **`lvl1()`**: Creates the ground platform.
- **`collision()`**: Handles sprite collisions with platforms, walls, and coins.
- **`interval()`**: Continuously monitors player movement and applies gravity when necessary.

### Events
- **Key Events**:
  - Right Arrow: Move right.
  - Left Arrow: Move left.
  - Up Arrow: Jump.
- **Collision Events**:
  - Handles landing on platforms and collecting coins.

---

## Installation

1. Install Codesters or access the online Codesters platform.
2. Copy the game script into a new project.
3. Run the project to start playing!

---

## Game Mechanics

- **Gravity**: Activates when the robot falls off a platform or during a jump.
- **Collisions**:
  - Landing on platforms resets gravity.
  - Collecting coins removes them from the stage.
- **Win Condition**: Removes the robot sprite and displays "You Win!" when all coins are collected.

---

## Customization

- Change platform and coin positions by editing the `createPlats()` and `addCollectables()` functions.
- Modify colors and sizes of objects for a personalized experience.
- Add additional levels by defining new functions and extending the current game loop.

---

## License

This project is open-source and available for anyone to modify or expand upon for educational purposes.

---

Enjoy playing **Underwater Adventure**!
