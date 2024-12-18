# Castle Battle Game

Engage in a thrilling magical duel in a castle setting! Take control of a powerful wizard, cast spells, and defend yourself against the evil wizard and witch. Can you outlast their attacks and emerge victorious?

---

## Features

- **Playable Wizard Character**: Control a wizard with unique spells and abilities.
- **Enemy Opponents**: Battle against the evil wizard and witch, each with distinct health and attacks.
- **Spell Casting**: Choose between offensive and defensive spells to defeat your enemies.
- **Dynamic Gameplay**: Real-time enemy attacks and spell collisions.

---

## How to Play

1. Control the wizard using spellcasting keys.
2. Cast offensive or defensive spells to damage enemies or shield yourself.
3. Survive and eliminate the evil wizard and witch to win the game.
4. Avoid losing all your health, or it’s game over.

---

## Controls

- **Spacebar**: Cast an offensive spell (electric bolt).
- **F Key**: Deploy a temporary shield to block enemy attacks.

---

## Code Overview

### Core Components

- **Sprites**:
  - `w` (Wizard): The player character with 5 HP.
  - `ew` (Evil Wizard) and `ewit` (Evil Witch): Enemies, each starting with 10 HP.
- **Spell System**:
  - Offensive spells (electric bolts, ice, and doom) to attack enemies.
  - Defensive shield to block enemy projectiles.
- **Health System**:
  - Each sprite has an HP attribute that decreases upon taking damage.
  - Enemies are removed when their HP reaches zero.

### Functions

- **Player Actions**:
  - `space_bar()`: Casts an electric bolt at enemies.
  - `shield()`: Activates a temporary shield to block attacks.
- **Enemy Actions**:
  - `ice()`: The witch casts an ice attack targeting the player.
  - `doom()`: The wizard casts a doom spell targeting the player.
  - `interval()`: Alternates enemy attacks at regular intervals.
- **Collision Handling**:
  - `w_hit(sprite, hit_sprite)`: Handles the collision of player spells with enemies.
  - `e_ew_hit(sprite, hit_sprite)`: Handles collisions involving enemy attacks and the player or shield.

---

## Game Mechanics

- **Offensive Spells**:
  - Cast by the player to reduce enemy HP.
  - Automatically removed after hitting an enemy or traveling a certain distance.
- **Defensive Shield**:
  - Blocks enemy attacks for a limited duration.
- **Enemy Attacks**:
  - Regular intervals trigger attacks like ice and doom spells aimed at the player.
- **Victory/Defeat**:
  - Win by reducing both enemies’ HP to zero.
  - Lose when the player’s HP reaches zero.

---

## Example Playthrough

1. The player begins with 5 HP.
2. The evil wizard and witch alternate between casting attacks.
3. The player casts electric bolts to damage enemies and uses shields to block attacks.
4. The game ends when the player wins by defeating the enemies or loses all HP.

---

## Customization

- **Adjust Difficulty**:
  - Modify the `hp` values for the player or enemies.
  - Adjust the frequency of enemy attacks in `interval()`.
- **Add More Spells**:
  - Introduce new spell types with unique effects.
- **Enhanced Graphics**:
  - Replace sprites or background with custom visuals.
- **Scoring System**:
  - Implement a score for tracking performance based on time or efficiency.

---

## Future Improvements

- Add a health bar display for all characters.
- Introduce more enemy types or levels.
- Implement sound effects for spells and collisions.
- Allow players to choose from multiple spell types dynamically.

---

## License

This project is open-source and free to use or modify for educational purposes.

---

Enjoy the **Castle Battle Game** and master your magical skills!
