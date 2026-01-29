import sys
import pygame
pygame.init()


def grid(size):
    """
    size - размер клетки
    """
    for i in range(HEIGHT // size):
        pygame.draw.line(screen, (211, 211, 211), (0, i * size), (WIDTH, i * size), 1)

    for i in range(WIDTH // size):
        pygame.draw.line(screen, (211, 211, 211), (i * size, 0), (i * size, HEIGHT), 1)


def car():
    pygame.draw.aalines(
        screen,
        (0, 0, 0),
        True,
        [
            (80, 520),
            (80, 500),
            (90, 500),
            (90, 480),
            (120, 440),
            (240, 440),
            (300, 480),
            (360, 480),
            (360, 500),
            (370, 500),
            (370, 520)
        ]
    )

    pygame.draw.circle(screen, (0, 0, 0), (140, 520), 30, 1)
    pygame.draw.circle(screen, (0, 0, 0), (140, 520), 15, 1)
    pygame.draw.circle(screen, (0, 0, 0), (140, 520), 5)

    pygame.draw.circle(screen, (0, 0, 0), (310, 520), 30, 1)
    pygame.draw.circle(screen, (0, 0, 0), (310, 520), 15, 1)
    pygame.draw.circle(screen, (0, 0, 0), (310, 520), 5)
    
    pygame.draw.aaline(screen, (0, 0, 0), (120, 480), (260, 480))


SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    grid(20)
    car()
    pygame.display.update()
    clock.tick(30)
