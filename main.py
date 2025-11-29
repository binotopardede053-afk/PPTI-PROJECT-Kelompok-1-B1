import pygame
from menu import main_menu
from game import game_loop

pygame.init()
screen = pygame.display.set_mode((450, 700))
pygame.display.set_caption("Flappy Bird")

while True:
    action = main_menu(screen)
    if action == "start":
        result = game_loop(screen)
        if result == "menu":
            continue
    else:
        break

