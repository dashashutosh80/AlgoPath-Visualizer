import pygame
import math
from node import Node
from collections import deque
from reconstruct_path import reconstruct_path


def dfs(draw, grid, start, end):
    # A stack to perform iterative DFS without recursion. 
    # DFS uses a stack in order to always traverse depth-wise.

    open_set = deque()  
    open_set.append(start)

    came_from = {}

    visited = []
    visited.append(start)

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.pop()
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
            current.make_closed()  # To mark the current node as visited.

    return False  # No path has been found.
