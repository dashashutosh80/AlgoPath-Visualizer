import pygame
import math
from constants import *
from node import Node


def make_grid(rows, width):
    grid = []  # 2-d list to store the nodes/cubes in each row
    gap = width // rows  # gives the width of each small cube/node
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # Draw horizontal gridlines extending from extreme left to right only shifting along every row downwards
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        # Draw vertical gridlines extending from top to bottom only shifting along every column towards right
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(GREY)  # At the beginning of every frame redraw the screen

    for row in grid:
        for node in row:
            # Call draw method of Node class in order to draw those nodes/cubes for every row
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


# Returns grid position corresponding to the position where mouse is clicked.
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width, algorithm):
    grid = make_grid(ROWS, width)

    start = None
    end = None
    # On pressing of ESC key or close button, execution of main is finished and control passes back to landing page.
    run = True

    while run:  # This loop will keep running while algorithm is running.

        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If close button on the top right corner of window is pressed, stop running the game
                run = False

            # To handle events on pressing/clicking of left mouse button.
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                # If no start node has been selected yet, make the clicked position as the start node.
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                # If clicked position does not point to either the start or end node make it a barrier.
                elif node != start and node != end:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # For right mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None

                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                # To update neighbors list of every node provided we have a start and end node (else algorithm will crash) and on press of SPACE key
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width),
                              grid, start, end)

                if event.key == pygame.K_c:  # Clear screen and reset.
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_ESCAPE: 
                    run = False
