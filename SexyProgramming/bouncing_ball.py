import pygame
import pymunk
import pymunk.pygame_util
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 900  # Pixels per second squared
HEXAGON_RADIUS = 200
ROTATION_SPEED = 0.5  # Radians per second
BALL_RADIUS = 20
FRICTION = 0.9

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Spinning Hexagon")
clock = pygame.time.Clock()

# Create physics space
space = pymunk.Space()
space.gravity = (0, GRAVITY)

draw_options = pymunk.pygame_util.DrawOptions(screen)

# Create hexagon walls
# Create hexagon walls
def create_hexagon(space, radius, position):
    angle_step = math.pi / 3
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = position

    space.add(body)  # Add body before shapes

    walls = []
    for i in range(6):
        a = (radius * math.cos(i * angle_step), radius * math.sin(i * angle_step))
        b = (radius * math.cos((i + 1) * angle_step), radius * math.sin((i + 1) * angle_step))
        shape = pymunk.Segment(body, a, b, 5)
        shape.elasticity = 0.8
        shape.friction = FRICTION
        space.add(shape)
        walls.append(shape)

    return body, walls


hexagon_body, hexagon_walls = create_hexagon(space, HEXAGON_RADIUS, (WIDTH // 2, HEIGHT // 2))

# Create ball
def create_ball(space, position):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, BALL_RADIUS))
    body.position = position
    shape = pymunk.Circle(body, BALL_RADIUS)
    shape.elasticity = 0.8
    shape.friction = FRICTION
    space.add(body, shape)
    return body

ball_body = create_ball(space, (WIDTH // 2, HEIGHT // 4))

# Game loop
running = True
angle = 0
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rotate hexagon
    angle += ROTATION_SPEED / FPS
    hexagon_body.angle = angle
    
    # Update physics
    space.step(1 / FPS)
    
    # Draw
    space.debug_draw(draw_options)
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
