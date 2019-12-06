import pygame
import sys
from pygame.locals import *

# SCREEN_WIDTH = 512
# SCREEN_HEIGHT = 512

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

HELIX_WIDTH = 512
HELIX_HEIGHT = 512
# helix actual width is 512+470 = 982
# helix actual height is 800
# helix actual dimensions are 982x800
# helix width (boundaries) should be 610 (350 to 960)

BLACK = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.draw.rect(screen, RED, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT], 0)

clock = pygame.time.Clock()

helix_img1 = pygame.image.load('pairs.png').convert()
helix_img2 = pygame.image.load('pairs.png').convert()
helix_img1 = pygame.transform.scale(helix_img1, (HELIX_WIDTH+470, SCREEN_HEIGHT))
helix_img2 = pygame.transform.scale(helix_img2, (HELIX_WIDTH+470, SCREEN_HEIGHT))

helix_y1 = -1 * SCREEN_HEIGHT
helix_y2 = 0
center_x = (SCREEN_WIDTH - (HELIX_WIDTH+470)) / 2



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

    # pygame.draw.rect(screen, color, [x, y, width, height], 0)
    # pygame.draw.rect(screen, BLACK, [center_x, 0, SCREEN_WIDTH, SCREEN_HEIGHT], 0)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            sys.exit()

    clock.tick(300)
