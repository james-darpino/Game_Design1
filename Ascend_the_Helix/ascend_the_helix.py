"""
A. Authors: James D'Arpino and Hannah Youssef

B. Version: Alpha 1.0

C. Description of code: This displays the player within
the brown block(ladder). The player needs to avoid
the falling blocks. If the player collides with a
falling block, he/she dies. The goal for the alpha,
is to get the highest score.

D. Description of how to play: Press the arrow directionals
to move. The goal is to avoid the falling blocks and
attain the highest score.

E. What's not working: The boundary on the right side of the
ladder is a bit off, we need to work on that.

F. What's left to work on: We need to add several elements to the game,
such as, multiple types of falling blocks,indicator for blocks falling
from the top power ups, health, health indicator and an indicator for the
current power-ups the player has.
"""

import pygame
import random

# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_BLUE = (8, 163, 208)
BLUE = (0, 0, 255)
PURPLE = (75, 0, 130)
RED = (255, 0, 0)
BROWN = (77, 38, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20

HELIX_X = SCREEN_WIDTH / 4
HELIX_WIDTH = SCREEN_WIDTH / 2
HELIX_HEIGHT = SCREEN_HEIGHT
HELIX_RIGHT_BOUNDARY = SCREEN_WIDTH / 1.4
HELIX_LEFT_BOUNDARY = SCREEN_WIDTH / 4


# --- Classes ---


class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
    BLOCK_WIDTH = 20
    BLOCK_HEIGHT = 20

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([self.BLOCK_WIDTH, self.BLOCK_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 2

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Player(pygame.sprite.Sprite):
    """ This class represents the player. """
    change_x = 0
    change_y = 0
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    starting_position_x = SCREEN_WIDTH / 2
    starting_position_y = SCREEN_HEIGHT - PLAYER_HEIGHT

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = self.starting_position_x
        self.rect.y = self.starting_position_y

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


def display_feedback(screen):
    # displays ladder (surface, color, [x, y, width, height], border thickness
    pygame.draw.rect(screen, BROWN, [HELIX_X, 0, HELIX_WIDTH, HELIX_HEIGHT], 0)


class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    def __init__(self):

        """ Constructor. Create all our attributes and initialize
        the game. """

        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the block sprites
        for i in range(5):
            block = Block()

            block.rect.x = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_y = 0
                    self.player.go_left()
                if event.key == pygame.K_RIGHT:
                    self.player.change_y = 0
                    self.player.go_right()
                if event.key == pygame.K_UP:
                    self.player.change_x = 0
                    self.player.go_up()
                if event.key == pygame.K_DOWN:
                    self.player.change_x = 0
                    self.player.go_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.change_x < 0:
                    self.player.stop()
                if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                    self.player.stop()
                if event.key == pygame.K_UP and self.player.change_y < 0:
                    self.player.stop()
                if event.key == pygame.K_DOWN and self.player.change_y > 0:
                    self.player.stop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

        return False

    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
            print(self.player.rect.y)

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, False)

            self.score += 1
            # Check the list of collisions.
            for _ in blocks_hit_list:
                self.game_over = True

            # Boundary check for player leaving helix left side
            if self.player.rect.x <= HELIX_LEFT_BOUNDARY:
                self.player.stop()
                self.player.rect.x = HELIX_LEFT_BOUNDARY

            # Boundary check for player leaving helix right side
            if self.player.rect.x >= HELIX_RIGHT_BOUNDARY:
                self.player.stop()
                self.player.rect.x = HELIX_RIGHT_BOUNDARY

            # Boundary check for player leaving helix bottom
            if self.player.rect.y >= SCREEN_HEIGHT:
                self.player.stop()
                self.player.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT

            # Boundary check for player leaving helix top
            if self.player.rect.y <= 0:
                self.player.stop()
                self.player.rect.y = 0

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        score_str = "Score: " + str(self.score)
        screen.fill(BLACK)
        display_feedback(screen)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(score_str, True, WHITE)
        screen.blit(text, [0, SCREEN_HEIGHT / 12])

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, WHITE)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(True)

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # Main game loop
    while not done:
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

    # Close window and exit
    pygame.quit()


# Call the main function, start up the game
if __name__ == "__main__":
    main()
