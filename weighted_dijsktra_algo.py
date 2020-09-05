import pygame
import math
from queue import PriorityQueue
from node import Node
from reconstruct_path import reconstruct_path


def edge_weight(p):  # Calculate edge weight of reaching a node.
    x, y = p
    return abs(y * 2 - x * 2)


def weighted_dijkstra(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()

    open_set.put((0, count, start))

    came_from = {}
    # Initially set weight of all nodes except start node to infinity. Store the info in a dictionary.
    weight = {node: float("inf") for row in grid for node in row}
    weight[start] = 0

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]  # Pop out the node from the priority queue
        open_set_hash.remove(current)  

        if current == end: 
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_weight = weight[current] + edge_weight(neighbor.get_pos())

            # If a lower weight for the neighbor is found based on the current path, then update it's weight and add this to the queue and hash.
            if temp_weight < weight[neighbor]:
                came_from[neighbor] = current
                weight[neighbor] = temp_weight
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((weight[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False 