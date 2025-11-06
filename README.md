# Animal Abstract Board Game

This is a Python-based, abstract, animal-themed board game that takes place on a 7x7 grid. Players control pieces (Chinchilla, Wombat, Emu, and Cuttlefish) with unique movement rules. The game ends when a Cuttlefish is captured by the opponent.

## Features
- Turn-based gameplay for two players (Amethyst and Tangerine)
- Piece-specific movement rules:
  - Chinchilla: slides 1 square in any direction
  - Wombat: jumps 4 squares orthogonally
  - Emu: slides 3 squares orthogonally
  - Cuttlefish: jumps 2 squares diagonally
- Win condition detection (game ends when a Cuttlefish is captured)
- Board represented as a 2D list
- Object-oriented design with inheritance and polymorphism

## Project Structure
```animal-abstract-board-game/
├─ game.py <- main game logic, including the board and piece classes
├─ tester.py <- test code demonstrating moves and validating rules
├─ README.md <- this file, explains the project and how to run it
```

## How to Run
1. Make sure you have Python 3 installed.
2. Run the game from the terminal:
```bash
python game.py
```

## Sample Usage
``` python
from game import AnimalGame

game = AnimalGame()
game.make_move('c2', 'c4')
print(game.get_game_state())
```