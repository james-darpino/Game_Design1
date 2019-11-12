import pygame
import random
import Globals


class Proton(pygame.sprite.Sprite):
    """ This class represents a Proton which the player must dodge. """

    def __init__(self):
        """ Constructor, create the image of the Proton. """
        super().__init__()
        self.image = pygame.Surface([Globals.ION_WIDTH, Globals.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("proton.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.ION_WIDTH, Globals.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """ Shows the range and boundaries of where the ion should be placed. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 2

        if self.rect.y > Globals.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Neutron(pygame.sprite.Sprite):
    """ This class represents a Neutron which the player must dodge. """

    def __init__(self):
        """ Constructor, create the image of the Neutron. """
        super().__init__()
        self.image = pygame.Surface([Globals.ION_WIDTH, Globals.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("neutron.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.ION_WIDTH, Globals.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """ Shows the range and boundaries of where the ion should be placed. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 5

        if self.rect.y > Globals.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Electron(pygame.sprite.Sprite):
    """ This class represents a Electron which the player must dodge. """

    def __init__(self):
        """ Constructor, create the image of the Electron. """
        super().__init__()
        self.image = pygame.Surface([Globals.ION_WIDTH, Globals.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("electron.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.ION_WIDTH, Globals.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """ Shows the range and boundaries of where the ion should be placed. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 7

        if self.rect.y > Globals.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()
