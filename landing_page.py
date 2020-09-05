import pygame
from constants import *
from main import main
from astar_algo import astar
from weighted_dijsktra_algo import weighted_dijkstra
from BFS import bfs
from DFS import dfs

pygame.init()

# setting up a display in the form of a square window
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("AlgoPath Visualizer")

background_image = pygame.image.load("PathFinder.jpg")
text_font = pygame.font.Font("freesansbold.ttf", 18)  # Set font of the text.


def start_page():
    while True:
        WIN.fill(WHITE)
        WIN.blit(background_image, (0, 0))  # Set background image.
        x, y = pygame.mouse.get_pos()

        # Create rectangular buttons of dimensions(100 x 30) starting at (30, 370).
        button1 = pygame.Rect(30, 370, 100, 30)
        pygame.draw.rect(WIN, WHITE, button1, 3)

        button2 = pygame.Rect(30, 420, 100, 30)
        pygame.draw.rect(WIN, WHITE, button2, 3)

        button3 = pygame.Rect(30, 470, 100, 30)
        pygame.draw.rect(WIN, WHITE, button3, 3)

        button4 = pygame.Rect(30, 520, 100, 30)
        pygame.draw.rect(WIN, WHITE, button4, 3)

        astar_text = text_font.render("A-Star", True, WHITE)
        # Render the text at the given coordinates i.e., inside the buttons in this case.
        WIN.blit(astar_text, (55, 375))

        dijkstra_text = text_font.render("Dijkstra", True, WHITE)
        WIN.blit(dijkstra_text, (50, 425))

        dfs_text = text_font.render("DFS", True, WHITE)
        WIN.blit(dfs_text, (57, 475))

        bfs_text = text_font.render("BFS", True, WHITE)
        WIN.blit(bfs_text, (57, 525))

        # If the clicked mouse position falls within the button's domain perform required actions.
        if button1.collidepoint(x, y):
            if click:
                main(WIN, WIDTH, astar)

        if button2.collidepoint(x, y):
            if click:
                main(WIN, WIDTH, weighted_dijkstra)

        if button3.collidepoint(x, y):
            if click:
                main(WIN, WIDTH, dfs)

        if button4.collidepoint(x, y):
            if click:
                main(WIN, WIDTH, astar)

        click = False

        # To loop through all the events that are taking place in pygame.
        for event in pygame.event.get():
            # If close button on the top right corner of window is pressed, stop running the game.
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()  # Quit on pressing ESC.

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()  # Update display everytine screen is rendered.


start_page()
