import pygame
pygame.init()

def grid(size):
    """
    size - 100
    """
    for i in range(HEIGHT // size):
        pygame.draw.line(screen , (211, 211, 211), (0, i * size), (WIDTH, i * size), 1)

    for i in range(WIDTH // size):
        pygame.draw.line(screen , (211, 211, 211), (i * size, 0), (i * size, HEIGHT), 1)


SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
COLS=3
ROWS=1
CELL_W = WIDTH // COLS
CELL_H = HEIGHT // ROWS
clock = pygame.time.Clock()
running = True

colors=[(200, 0, 0), (0, 200, 0), (0, 0, 200)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))
    grid = [[colors[i] for i in range(COLS)] for _ in range(ROWS)]




    for row in range(1):
      for col in range(3):
        rect = pygame.Rect(
            col * CELL_W,
            row * CELL_H,
            CELL_W,
            CELL_H
        )
        pygame.draw.rect(screen, grid[row][col], rect)

    

    pygame.display.update()
    clock.tick(60)

pygame.quit()


