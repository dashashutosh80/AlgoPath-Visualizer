def reconstruct_path(came_from, current, draw):
    while current in came_from:  # This loop will run and create a path from end node till we reach the node that came from start node i.e., all the nodes in came_from list
        current = came_from[current]
        current.make_path()
        draw()
