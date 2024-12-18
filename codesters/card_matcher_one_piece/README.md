# Memory Matching Game

A simple memory matching game where players click on cards to reveal images. The goal is to find matching pairs of cards. The game has two rounds per turn, and players need to remember the images to match them correctly.

---

## Features

- **Card Matching**: Players click on cards to reveal their faces. The goal is to match pairs of identical cards.
- **Two-Round Turns**: Each player has two turns to click cards, and they must remember the images to match them.
- **Shuffling**: The deck is shuffled randomly to ensure a unique game every time.

---

## How to Play

1. **Start the Game**:
   - The game starts with a 4x4 grid of face-down cards.
   
2. **Player Turns**:
   - Players alternate turns to click on two cards. When a card is clicked, it reveals an image.
   - If the two revealed cards match, they remain visible. If they don't match, they are turned face-down again.
   
3. **Winning the Game**:
   - The game continues until all pairs of matching cards are found.

---

## Controls

- **Mouse Click**:
   - Click on a card to flip it over and reveal its image.
   - Click on a second card to try to match it with the first.
   
---

## Code Overview

### Key Components

1. **Deck of Cards**:
   - The game features a 4x4 grid of cards, each represented by a `codesters.Rectangle`. The cards are assigned unique IDs and will be flipped over when clicked.

2. **Card Faces**:
   - The faces of the cards are represented by sprites that correspond to different characters, such as "Bounceman", "Zoro", "Nami", etc.

3. **Game Logic**:
   - Players take turns flipping over two cards at a time. If the cards match, they remain face-up; otherwise, they are flipped back over.
   - The game keeps track of the current turn, alternating between players after each pair of cards is revealed.

4. **Shuffling**:
   - The deck of character images is shuffled randomly each time the game starts, ensuring a unique arrangement of cards for each game.

### Main Functions

- **`create_cards()`**:
   - Creates a 4x4 grid of cards on the game board. Each card is represented by a blue rectangle.
  
- **`deck()`**:
   - Populates the list of `sprites` with the images that will be used on the cards. These sprites represent various characters like "Bounceman", "Zoro", "Nami", etc.

- **`click(sprite)`**:
   - Handles the logic for revealing cards when clicked. If two cards are flipped over, it checks if they match. If they don't, the cards are hidden again.

- **`shuffle()`**:
   - Randomly shuffles the order of the sprites in the deck to ensure the game is different each time.

---

## Future Enhancements

- **Timer**:
   - Add a countdown timer to make the game more challenging.
   
- **Score System**:
   - Track and display the player's score based on the number of correct matches they make.

- **Game Restart**:
   - Include an option to restart the game after completing a round.

- **Sound Effects**:
   - Add sound effects for card flips, matches, and incorrect attempts.

---

## License

This game is open-source and available for educational purposes and modifications.

---

Enjoy playing the Memory Matching Game!
