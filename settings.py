TITLE = "Jumpy!"
WIDTH = 1000
HEIGHT = 700
FPS = 60
# movement
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 2.1
JUMP_POWER = -25
WALL_FRICTION = 0.05

# lista platform

PLATFORM_LIST = [(500, 180, 100, 20),
                 (310, 160, 100, 20),
                 (80, 120, 80, 20),
                 (530, HEIGHT - 120, 100, 20),
                 (290, HEIGHT - 160, 100, 20),
                 (110, HEIGHT - 100, 80, 20),
                 (WIDTH - 280, 200, 100, 20),
                 (0, HEIGHT - 20, 90, 20),
                 (WIDTH - 260, HEIGHT - 20, 240, 20),
                 (WIDTH - 20, HEIGHT - 500, 20, 500),
                 (WIDTH - 180, HEIGHT - 500, 20, 400)]

#(0, HEIGHT - 20, WIDTH, 20),

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (50, 50, 50)
DARKGREEN = (60, 86, 73)