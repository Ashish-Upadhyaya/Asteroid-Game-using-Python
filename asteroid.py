import pygame, sys, os, random, math
from pygame.locals import *
import logging

# Initialize Pygame
pygame.mixer.pre_init()
pygame.init()

# Logging setup
logger = logging.getLogger('asteroids_game')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('asteroids_game.log')
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600
FPS = 60

# Canvas and Clock
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Asteroids')
fps_clock = pygame.time.Clock()

# Load Images
bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
debris = pygame.image.load(os.path.join('images', 'debris2_brown.png'))
ship = pygame.image.load(os.path.join('images', 'ship.png'))
ship_thrusted = pygame.image.load(os.path.join('images', 'ship_thrusted.png'))
asteroid_img = pygame.image.load(os.path.join('images', 'asteroid.png'))
shot = pygame.image.load(os.path.join('images', 'shot2.png'))
explosion = pygame.image.load(os.path.join('images', 'explosion_blue.png'))

# Load Sounds
missile_sound = pygame.mixer.Sound(os.path.join('sounds', 'missile.ogg'))
thruster_sound = pygame.mixer.Sound(os.path.join('sounds', 'thrust.ogg'))
explosion_sound = pygame.mixer.Sound(os.path.join('sounds', 'explosion.ogg'))
pygame.mixer.music.load(os.path.join('sounds', 'game.ogg'))
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)  # Loop the background music

# Game Variables
ship_x, ship_y = WIDTH / 2 - 50, HEIGHT / 2 - 50
ship_angle = 0
ship_is_rotating = False
ship_is_forward = False
ship_direction = 0
ship_speed = 0

asteroid_x = [random.randint(0, WIDTH) for _ in range(5)]
asteroid_y = [random.randint(0, HEIGHT) for _ in range(5)]
asteroid_angle = [random.randint(0, 360) for _ in range(5)]
asteroid_speed = 2

bullet_x, bullet_y, bullet_angle = [], [], []
score = 0
game_over = False

# Helper Functions
def rot_center(image, angle):
    """Rotate an image while keeping its center."""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def is_collision(obj1_x, obj1_y, obj2_x, obj2_y, dist):
    """Check if two objects collide based on distance."""
    distance = math.sqrt((obj1_x - obj2_x) ** 2 + (obj1_y - obj2_y) ** 2)
    return distance < dist

# Draw Function
def draw(canvas):
    global score, game_over
    canvas.fill(BLACK)
    canvas.blit(bg, (0, 0))
    canvas.blit(debris, (0, 0))

    for i in range(len(bullet_x)):
        canvas.blit(shot, (bullet_x[i], bullet_y[i]))

    for i in range(len(asteroid_x)):
        canvas.blit(rot_center(asteroid_img, asteroid_angle[i]), (asteroid_x[i], asteroid_y[i]))

    if ship_is_forward:
        canvas.blit(rot_center(ship_thrusted, ship_angle), (ship_x, ship_y))
    else:
        canvas.blit(rot_center(ship, ship_angle), (ship_x, ship_y))

    # Draw Score
    font = pygame.font.SysFont("Comic Sans MS", 40)
    score_label = font.render(f"Score: {score}", 1, (255, 255, 0))
    canvas.blit(score_label, (50, 20))

    if game_over:
        font = pygame.font.SysFont("Comic Sans MS", 80)
        game_over_label = font.render("GAME OVER", 1, WHITE)
        canvas.blit(game_over_label, (WIDTH / 2 - 150, HEIGHT / 2 - 40))

# Input Handling
def handle_input():
    global ship_angle, ship_is_rotating, ship_direction
    global ship_x, ship_y, ship_speed, ship_is_forward
    global bullet_x, bullet_y, bullet_angle
    global thruster_sound, missile_sound

    for event in pygame.event.get():
        if event.type == QUIT:
            logger.info('Game quit')
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                logger.debug('Right arrow key pressed')
                ship_is_rotating = True
                ship_direction = 0
            elif event.key == K_LEFT:
                logger.debug('Left arrow key pressed')
                ship_is_rotating = True
                ship_direction = 1
            elif event.key == K_UP:
                logger.debug('Up arrow key pressed')
                ship_is_forward = True
                ship_speed = 10
                thruster_sound.play()
            elif event.key == K_SPACE:
                logger.debug('Space bar pressed')
                bullet_x.append(ship_x + 50)
                bullet_y.append(ship_y + 50)
                bullet_angle.append(ship_angle)
                missile_sound.play()

        elif event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                logger.debug('Rotation stopped')
                ship_is_rotating = False
            elif event.key == K_UP:
                logger.debug('Forward motion stopped')
                ship_is_forward = False
                thruster_sound.stop()

    if ship_is_rotating:
        ship_angle += -10 if ship_direction == 0 else 10

    if ship_is_forward or ship_speed > 0:
        ship_x += math.cos(math.radians(ship_angle)) * ship_speed
        ship_y -= math.sin(math.radians(ship_angle)) * ship_speed
        ship_x %= WIDTH
        ship_y %= HEIGHT
        if not ship_is_forward:
            ship_speed = max(0, ship_speed - 0.2)

# Game Logic
def game_logic():
    global bullet_x, bullet_y, bullet_angle
    global asteroid_x, asteroid_y, asteroid_angle
    global score, game_over

    # Update Bullets
    for i in range(len(bullet_x) - 1, -1, -1):
        bullet_x[i] += math.cos(math.radians(bullet_angle[i])) * 10
        bullet_y[i] -= math.sin(math.radians(bullet_angle[i])) * 10
        if not (0 <= bullet_x[i] <= WIDTH and 0 <= bullet_y[i] <= HEIGHT):
            bullet_x.pop(i)
            bullet_y.pop(i)
            bullet_angle.pop(i)

    # Update Asteroids
    for i in range(len(asteroid_x)):
        asteroid_x[i] += math.cos(math.radians(asteroid_angle[i])) * asteroid_speed
        asteroid_y[i] -= math.sin(math.radians(asteroid_angle[i])) * asteroid_speed
        asteroid_x[i] %= WIDTH
        asteroid_y[i] %= HEIGHT

        if is_collision(ship_x, ship_y, asteroid_x[i], asteroid_y[i], 27):
            logger.error('Game over: collision with asteroid')
            game_over = True

    # Check Bullet-Asteroid Collisions
    for i in range(len(bullet_x) - 1, -1, -1):
        for j in range(len(asteroid_x) - 1, -1, -1):
            if is_collision(bullet_x[i], bullet_y[i], asteroid_x[j], asteroid_y[j], 50):
                asteroid_x[j] = random.randint(0, WIDTH)
                asteroid_y[j] = random.randint(0, HEIGHT)
                asteroid_angle[j] = random.randint(0, 360)
                explosion_sound.play()
                logger.info('Asteroid destroyed')
                score += 1
                bullet_x.pop(i)
                bullet_y.pop(i)
                bullet_angle.pop(i)
                break

# Main Game Loop
logger.info('Game started')
logger.debug('Game loop started')

while True:
    draw(window)
    handle_input()
    if not game_over:
        game_logic()
    pygame.display.update()
    fps_clock.tick(FPS)
