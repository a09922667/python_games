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

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))


    grid(100,1)
    

    pygame.display.update()
    clock.tick(60)

pygame.quit()


