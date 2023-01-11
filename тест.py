import pygame
import sys
import random


class Cell:
    def __init__(self, start_energy, start_organic ,light_to_energy, soil_to_organic, movement, attack, reproduction, mind):
        self.energy = start_energy
        self.organic = start_organic
        self.efficiency = {
            'свет в энергию': light_to_energy,
            'почва в вещество': soil_to_organic,
            'движение': movement,
            'атака': attack,
            'размножение': reproduction
        }
        self.mind = mind


class Field:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.lst = [[0] * width for i in range(height)]










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