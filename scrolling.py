import pygame
import sys
from pygame.locals import *

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

# HELIX_IMG_WIDTH = HELIX_RIGHT_BOUNDARY - HELIX_LEFT_BOUNDARY
HELIX_IMG_WIDTH = 610
# HELIX_IMG_HEIGHT = SCREEN_HEIGHT
HELIX_IMG_HEIGHT = 800

BLACK = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

helix_img1 = pygame.image.load('pairs.png').convert()
helix_img2 = pygame.image.load('pairs.png').convert()
helix_img1 = pygame.transform.scale(helix_img1, (HELIX_IMG_WIDTH, SCREEN_HEIGHT))
helix_img2 = pygame.transform.scale(helix_img2, (HELIX_IMG_WIDTH, SCREEN_HEIGHT))

helix_y1 = -1 * SCREEN_HEIGHT
helix_y2 = 0
center_x = (SCREEN_WIDTH - HELIX_IMG_WIDTH) / 2

while True:

    screen.blit(helix_img1, (center_x, helix_y1))
    screen.blit(helix_img2, (center_x, helix_y2))

    helix_y1 += 1
    helix_y2 += 1

    if helix_y1 == SCREEN_HEIGHT:
        helix_y1 = helix_y2 - SCREEN_HEIGHT
        helix_y2 = 0
    if helix_y2 == SCREEN_HEIGHT:
        helix_y2 = helix_y1 - SCREEN_HEIGHT
        helix_y1 = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            sys.exit()

    clock.tick(300)
