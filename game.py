import pygame
import random

class Bird:
    def __init__(self):
        self.image = pygame.image.load("assets/bird.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.gravity = 0
        self.jump_power = -8

    def update(self):
        self.gravity += 0.4
        self.rect.y += self.gravity

        if self.rect.y > 600:
            self.rect.y = 600

    def jump(self):
        self.gravity = self.jump_power


class Pipe:
    def __init__(self):
        self.pipe_top = pygame.image.load("assets/pipe_top.png")
        self.pipe_bottom = pygame.image.load("assets/pipe_bottom.png")

        self.x = 450
        self.gap = 200
        self.height = random.randint(50, 350)

        self.top_rect = self.pipe_top.get_rect(midbottom=(self.x, self.height))
        self.bottom_rect = self.pipe_bottom.get_rect(midtop=(self.x, self.height + self.gap))

    def update(self):
        self.top_rect.x -= 3
        self.bottom_rect.x -= 3

    def off_screen(self):
        return self.top_rect.x < -100


def game_loop(screen):
    clock = pygame.time.Clock()

    bird = Bird()
    pipes = []

    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1300)

    running = True
    while running:
        screen.fill((0, 180, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

            if event.type == SPAWNPIPE:
                pipes.append(Pipe())

        bird.update()
        screen.blit(bird.image, bird.rect)

        for pipe in pipes[:]:
            pipe.update()
            screen.blit(pipe.pipe_top, pipe.top_rect)
            screen.blit(pipe.pipe_bottom, pipe.bottom_rect)

            if pipe.off_screen():
                pipes.remove(pipe)

            # collision
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                return "menu"

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    return "quit"

