import pygame

CELL_SIZE = 30

def draw(grid, agent, goal):
    pygame.init()
    size = len(grid)

    screen = pygame.display.set_mode((size * CELL_SIZE, size * CELL_SIZE))
    pygame.display.set_caption("Autonomous Navigation Simulation")

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # draw grid
        for i in range(size):
            for j in range(size):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if grid[i][j] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), rect)

                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        # draw goal
        pygame.draw.rect(screen, (255, 0, 0),
                         (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE,
                          CELL_SIZE, CELL_SIZE))

        # draw agent
        pygame.draw.rect(screen, (0, 255, 0),
                         (agent.position[1]*CELL_SIZE,
                          agent.position[0]*CELL_SIZE,
                          CELL_SIZE, CELL_SIZE))

        agent.move()

        pygame.display.update()

    pygame.quit()