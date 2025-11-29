import pygame
import sys

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont("arial", size, True)
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x, y))

def main_menu(screen):
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 120, 250))
        draw_text(screen, "FLAPPY BIRD", 60, 80, 150)
        draw_text(screen, "Press SPACE to Start", 30, 110, 300)
        draw_text(screen, "Press ESC to Quit", 30, 150, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "start"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

