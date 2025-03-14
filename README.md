# Asteroids Game

## Overview
The Asteroids Game is a classic space shooter game inspired by the original arcade game. In this version, you control a spaceship navigating through an asteroid field while trying to shoot down as many asteroids as possible. The game is developed using the Pygame library in Python and includes rich multimedia elements such as images, sounds, and background music to provide an engaging user experience.

## Table of Contents
1. [Features](#features)
2. [How to Play](#how-to-play)
3. [Controls](#controls)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [Game Logic and Functionality](#game-logic-and-functionality)
7. [Logging](#logging)
8. [Credits](#credits)
9. [License](#license)
10. [Contributing](#contributing)
11. [Contact](#contact)

## Features
- **Spaceship Control**: Rotate your spaceship left and right, thrust forward, and shoot missiles.
- **Asteroid Field**: Navigate through dynamically moving asteroids that wrap around screen edges.
- **Collision Detection**: Realistic collision detection between the spaceship, bullets, and asteroids.
- **Scoring System**: Earn points for each asteroid destroyed.
- **Sound Effects**: Immersive sound effects for missile firing, thrusting, explosions, and background music.
- **Game Over Condition**: The game ends if the spaceship collides with an asteroid.

## How to Play
1. Launch the game and use the arrow keys to rotate and thrust your spaceship.
2. Press the spacebar to fire missiles at approaching asteroids.
3. Destroy as many asteroids as possible to increase your score.
4. Avoid collisions with asteroids to keep the game going.

## Controls
- **Left Arrow Key**: Rotate the spaceship counterclockwise.
- **Right Arrow Key**: Rotate the spaceship clockwise.
- **Up Arrow Key**: Thrust the spaceship forward.
- **Spacebar**: Fire missiles at asteroids.

## Installation
To run this game, ensure you have Python and Pygame installed on your system. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/asteroids-game.git
   ```

2. **Install Pygame**:
   ```bash
   pip install pygame
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd asteroids-game
   ```

4. **Run the Game**:
   ```bash
   python main.py
   ```

## Project Structure
### Images Directory
Contains all the image assets used in the game:
- `asteroid.png`: Image of the asteroid.
- `bg.jpg`: Background image.
- `debris2_brown.png`: Debris image.
- `explosion_blue.png`: Explosion animation image.
- `nebula_brown.png`: Nebula background image.
- `ship_thrusted.png`: Image of the spaceship with thrusters active.
- `ship.png`: Image of the spaceship.
- `shot2.png`: Image of the missile shot.

### Sounds Directory
Contains all the sound effects and background music:
- `explosion.ogg`: Sound effect for asteroid explosions.
- `game.mp3`: Background music (alternative format).
- `game.ogg`: Background music.
- `missile.ogg`: Sound effect for firing missiles.
- `thrust.ogg`: Sound effect for spaceship thrust.

### Main File
- `main.py`: The main game file containing the game logic, event handling, and rendering functions.

## Game Logic and Functionality
### Initialization
- The game initializes Pygame, sets up the display window, loads images and sounds, and configures global variables.
  
### Drawing and Rendering
- The `draw` function handles rendering the spaceship, asteroids, bullets, background, debris, and score display on the screen.

### Input Handling
- The `handle_input` function processes keyboard events to control the spaceship's rotation, thrust, and missile firing. It also manages sound playback for thrusting and missile firing.

### Game Logic
- The `game_logic` function updates the positions of bullets and asteroids, checks for collisions, wraps objects around screen edges, and updates the score when asteroids are destroyed.

### Screen Update
- The `update_screen` function refreshes the display at a consistent frame rate of 60 FPS.

### Collision Detection
- The `isCollision` function calculates the distance between two points to determine if a collision has occurred.

### Logging
- Comprehensive logging is implemented to track game events such as key presses, game start, game over conditions, and asteroid destructions. Logs are written to both the console and a file named `asteroids_game.log`.

## Logging
The game uses Python's `logging` module to record various events during gameplay. This includes:
- **Info Level**: Game start, asteroid destruction.
- **Debug Level**: Game loop iterations, key presses, and specific game actions.
- **Error Level**: Game over conditions due to collisions.

Logs are output to both the console and a log file (`asteroids_game.log`) for later review.

## Credits
- **Images**: All images are sourced from various free-to-use resources.
- **Sounds**: All sounds are sourced from various free-to-use resources.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.

## Contact
For any questions or feedback, feel free to contact me at [ashishofficial231@gmail.com].

---

Enjoy the game and happy coding!
