# Asteroids Game

Welcome to the **Asteroids Game**, a classic arcade-style game built using Python and the Pygame library. This project is designed to provide an engaging and nostalgic gaming experience while showcasing the capabilities of Pygame for game development.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Play](#how-to-play)
6. [Game Mechanics](#game-mechanics)
7. [Code Structure](#code-structure)
8. [Logging](#logging)
9. [Assets](#assets)
10. [Contributing](#contributing)
11. [License](#license)

---

## Overview

The Asteroids Game is a space-themed shooter where the player controls a spaceship navigating through a field of asteroids. The objective is to destroy as many asteroids as possible while avoiding collisions. The game features smooth animations, sound effects, and responsive controls to create an immersive experience.

This project also includes logging functionality to track game events, such as key presses, asteroid destruction, and game over conditions. This makes it easier to debug and analyze gameplay.

---

## Features

- **Dynamic Gameplay**: Navigate through a field of asteroids while shooting them down.
- **Responsive Controls**: Use arrow keys to rotate and thrust the spaceship, and the spacebar to fire bullets.
- **Collision Detection**: Accurate collision detection ensures fair gameplay.
- **Sound Effects**: Immersive sound effects for thrusters, missile firing, explosions, and background music.
- **Score Tracking**: Keep track of your score as you destroy asteroids.
- **Game Over State**: Automatically ends the game when the spaceship collides with an asteroid.
- **Logging**: Detailed logs for debugging and analyzing gameplay events.

---

## Requirements

To run this game, you need the following:

- **Python 3.7 or higher**
- **Pygame Library**: Install it using `pip install pygame`
- **Assets Folder**: Ensure the `images` and `sounds` directories are present in the root directory. These contain the required images and sound files.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/asteroids-game.git
   cd asteroids-game
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then, install Pygame:
   ```bash
   pip install pygame
   ```

3. **Verify Assets**:
   Ensure the `images` and `sounds` folders are present in the root directory. These folders should contain the following files:
   - `images/`: `bg.jpg`, `debris2_brown.png`, `ship.png`, `ship_thrusted.png`, `asteroid.png`, `shot2.png`, `explosion_blue.png`
   - `sounds/`: `missile.ogg`, `thrust.ogg`, `explosion.ogg`, `game.ogg`

4. **Run the Game**:
   Start the game by running:
   ```bash
   python main.py
   ```

---

## How to Play

1. **Controls**:
   - **Arrow Keys**:
     - `Left Arrow`: Rotate the spaceship counterclockwise.
     - `Right Arrow`: Rotate the spaceship clockwise.
     - `Up Arrow`: Thrust forward.
   - **Spacebar**: Fire bullets to destroy asteroids.

2. **Objective**:
   - Destroy as many asteroids as possible by shooting them.
   - Avoid collisions with asteroids to survive longer.

3. **Game Over**:
   - The game ends when the spaceship collides with an asteroid.
   - Restart the game by running the script again.

---

## Game Mechanics

### 1. Spaceship Movement
- The spaceship rotates around its center using the left and right arrow keys.
- The up arrow key activates the thruster, propelling the spaceship forward in the direction it is facing.
- The spaceship wraps around the screen edges, creating a continuous play area.

### 2. Shooting Bullets
- Pressing the spacebar fires a bullet in the current direction of the spaceship.
- Bullets travel in a straight line and are removed from the game when they go off-screen.

### 3. Asteroid Movement
- Asteroids move in random directions at a constant speed.
- When an asteroid reaches the edge of the screen, it wraps around to the opposite side.

### 4. Collision Detection
- Collisions between the spaceship and asteroids trigger a game-over state.
- Bullets that collide with asteroids destroy them, increasing the player's score.

---

## Code Structure

The code is organized into modular functions for clarity and maintainability:

1. **Initialization**:
   - Sets up Pygame, loads assets, and initializes game variables.

2. **Helper Functions**:
   - `rot_center(image, angle)`: Rotates an image while keeping its center.
   - `is_collision(obj1_x, obj1_y, obj2_x, obj2_y, dist)`: Checks if two objects collide based on distance.

3. **Game Logic**:
   - Handles movement of the spaceship, bullets, and asteroids.
   - Detects collisions and updates the game state accordingly.

4. **Input Handling**:
   - Processes user input for controlling the spaceship and firing bullets.

5. **Drawing**:
   - Renders the spaceship, bullets, asteroids, background, and score on the screen.

6. **Main Game Loop**:
   - Continuously updates the game state, processes input, and redraws the screen until the game ends.

---

## Logging

The game uses Python's `logging` module to record important events during gameplay. Logs are written to both a file (`asteroids_game.log`) and the console. This is useful for debugging and analyzing player behavior.

- **Log Levels**:
  - `INFO`: General game events (e.g., game start, asteroid destruction).
  - `DEBUG`: Detailed information about user input and game loop iterations.
  - `ERROR`: Critical events (e.g., game over due to collision).

Example log entry:
```
2023-10-01 12:34:56 - asteroids_game - INFO - Asteroid destroyed
```

---

## Assets

All assets used in the game are stored in the `images` and `sounds` directories. These include:

- **Images**:
  - Background (`bg.jpg`)
  - Debris (`debris2_brown.png`)
  - Spaceship (`ship.png`, `ship_thrusted.png`)
  - Asteroid (`asteroid.png`)
  - Bullet (`shot2.png`)
  - Explosion (`explosion_blue.png`)

- **Sounds**:
  - Missile firing (`missile.ogg`)
  - Thruster activation (`thrust.ogg`)
  - Explosion (`explosion.ogg`)
  - Background music (`game.ogg`)

Ensure these files are present in their respective directories for the game to function correctly.

---

## Contributing

We welcome contributions to improve the Asteroids Game! Here’s how you can contribute:

1. **Bug Reports**: Open an issue on GitHub if you encounter any bugs.
2. **Feature Requests**: Suggest new features or enhancements.
3. **Code Contributions**: Fork the repository, make your changes, and submit a pull request.

Please ensure your contributions follow the existing code style and include appropriate documentation.

---

## License

This project is licensed under the **APACHE 2.0 License**. See the `LICENSE` file for details.

---

Thank you for checking out the Asteroids Game! We hope you enjoy playing and exploring the code. If you have any questions or feedback, feel free to reach out via GitHub issues or email.

Happy gaming! 🚀
