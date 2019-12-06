
import pygame
import random
import Globals


class Adenine(pygame.sprite.Sprite):
    """ This class represents an Adenine which the player must collect. """

    def __init__(self):
        """ Constructor, create the image of the Adenine. """
        super().__init__()
        self.image = pygame.Surface([Globals.ION_WIDTH, Globals.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("adenine.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.ION_WIDTH,
                                                         Globals.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """Shows the range and boundaries of where the ion should be placed."""
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY,
                                     Globals.HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 5

        if self.rect.y > Globals.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Cytosine(pygame.sprite.Sprite):
    """ This class represents an Adenine which the player must collect. """

    def __init__(self):
        """ Constructor, create the image of the Adenine. """
        super().__init__()
        self.image = pygame.Surface([Globals.ION_WIDTH, Globals.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("cytosine.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.ION_WIDTH,
                                                         Globals.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """Shows the range and boundaries of where the ion should be placed."""
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY,
                                     Globals.HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 5

        if self.rect.y > Globals.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Guanine(pygame.sprite.Sprite):
    """ This class represents an Adenine which the player must collect. """

    def __init__(self):
        """ Constructor, create the image of the Adenine. """
        super().__init__()
        self.image = pygame.Surface([Globals.ION_WIDTH, Globals.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("Guanine.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.ION_WIDTH,
                                                         Globals.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """Shows the range and boundaries of where the ion should be placed."""
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY,
                                     Globals.HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 5

        if self.rect.y > Globals.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Thymine(pygame.sprite.Sprite):
    """ This class represents an Adenine which the player must collect. """

    def __init__(self):
        """ Constructor, create the image of the Adenine. """
        super().__init__()
        self.image = pygame.Surface([Globals.ION_WIDTH, Globals.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("thymine.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.ION_WIDTH,
                                                         Globals.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """Shows the range and boundaries of where the ion should be placed."""
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY,
                                     Globals.HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 5

        if self.rect.y > Globals.SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()
