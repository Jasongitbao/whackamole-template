import pygame
import random

from pygame.examples.grid import WINDOW_HEIGHT

SQUARE_SIZE = 25
GRID_WIDTH = 20
GRID_HEIGHT = 19
WIN_WIDTH = GRID_WIDTH * SQUARE_SIZE
WIN_HEIGHT = GRID_HEIGHT * SQUARE_SIZE
def draw_grid(win):
    for j in range(1, GRID_HEIGHT, 1):
        start = (0, j * SQUARE_SIZE)
        end = (WIN_WIDTH, j * SQUARE_SIZE)
        pygame.draw.line(win, (0, 0, 200), start, end)
    for i in range(1, GRID_WIDTH, 1):
        start = (i * SQUARE_SIZE, 0)
        end = (i * SQUARE_SIZE, WIN_WIDTH)
        pygame.draw.line(win, (0, 0, 200), start, end)
def main():
    try:
        pygame.init()

        win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole Game")
        x , y = 0 , 0
        image = pygame.image.load("mole.png")
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    grid_x = mouse_x // SQUARE_SIZE
                    grid_y = mouse_y // SQUARE_SIZE
                    if grid_x == x and grid_y == y:
                        x = random.randint(0, GRID_WIDTH - 1)
                        y = random.randint(0, GRID_HEIGHT - 1)
            win.fill("light green")
            draw_grid(win)
            win.blit(image, image.get_rect(topleft=(x * SQUARE_SIZE,y * SQUARE_SIZE)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
