import pygame
import math
from node import Node
from reconstruct_path import reconstruct_path


def bfs(draw, grid, start, end):
    open_set = []
    open_set.append(start)

    came_from = {}
    # Push start node into visited list.
    visited = []
    visited.append(start)

    while open_set: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.pop(0)  # Pop out the first node from the queue everytime and traverse it's neighbors.

        if current == end:  
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        # Traverse all the un-visited neigbors of the current node and subsequently add them to open_set and mark them as visited.
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                came_from[neighbor] = current
                open_set.append(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False  