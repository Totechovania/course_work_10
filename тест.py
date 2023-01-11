import pygame
import sys






if __name__ == '__main__':
    screen_height = 800
    screen_weight = 1200
    FPS = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_weight, screen_height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        screen.fill((255, 255, 255))


        pygame.display.flip()
        clock.tick(FPS)