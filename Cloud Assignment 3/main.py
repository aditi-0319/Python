import pygame
import random
import copy

WIDTH, HEIGHT = 50, 50
CELL_SIZE = 15
FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 

def initialize_grid():
    return [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]


def count_live_neighbors(grid, x, y):
    count = 0
    neighbors = [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) if (0 <= i < WIDTH and 0 <= j < HEIGHT and (i != x or j != y))]
    for i, j in neighbors:
        count += grid[j][i]
    return count


def update_grid(grid):
    new_grid = copy.deepcopy(grid)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            live_neighbors = count_live_neighbors(grid, x, y)

            # Apply rules
            if grid[y][x] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[y][x] = 0
            elif grid[y][x] == 0 and live_neighbors == 3:
                new_grid[y][x] = 1

    return new_grid


def draw_grid(screen, grid):
    screen.fill(BLACK)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Game")

    grid = initialize_grid()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        grid = update_grid(grid)
        draw_grid(screen, grid)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
