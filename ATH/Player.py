import pygame
import random
import Globals
import ascend_the_helix


class Player(pygame.sprite.Sprite):
    """ This class represents the player. """
    change_x = 0
    change_y = 0
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    starting_position_x = Globals.SCREEN_WIDTH / 2
    starting_position_y = Globals.SCREEN_HEIGHT - Globals.PLAYER_HEIGHT
    health = 100.0
    maxHealth = 100
    healthDashes = 10

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([Globals.PLAYER_WIDTH, Globals.PLAYER_HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = self.starting_position_x
        self.rect.y = self.starting_position_y
        # import man climbing image
        self.image = pygame.image.load("man_climbing.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Globals.PLAYER_WIDTH, Globals.PLAYER_HEIGHT))

    def do_health(self):
        dash_convert = int(self.maxHealth / self.healthDashes)
        current_dashes = int(self.health / dash_convert)

        remaining_health = self.healthDashes - current_dashes
        health_display = "-" * current_dashes
        remaining_display = " " * remaining_health
        percent = str(int((self.health / self.maxHealth) * 100)) + "%"

        print("|" + health_display + remaining_display + "|")  # Print out textbased healthbar
        print("         " + percent)

    def draw(self, screen):
        # blit the image to the screen
        screen.blit(self.image, self.rect)

    def get_hit(self):
        health = self.health
        health = health - 10

    def update(self):
        """ Update the player location. """
        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def go_down(self):
        """called when the user hits the down arrow"""
        self.change_y = 6

    def go_up(self):
        """called when the user hits the up arrow"""
        self.change_y = -6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0
