# ASCEND THE HELIX

import pygame
import random

# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 127)
TEAL = (0, 128, 128)
BROWN = (165, 42, 42)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


# --- Classes ---

class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """

    # block width and height is 20x20
    WIDTH = 20
    HEIGHT = 20

    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Player(pygame.sprite.Sprite):
    """ This class represents the player. """

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(TEAL)
        self.rect = self.image.get_rect()

    def update(self):
        """ Update the player location. """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    # --- Class attributes.
    # In this case, all the data we need
    # to run our game.

    # Sprite lists
    block_list = None
    all_sprites_list = None
    player = None

    # Other data
    game_over = False
    score = 0

    # --- Class methods
    # Set up the game
    def __init__(self):

        # add the laser sound (laser5.ogg file)
        self.sound = pygame.mixer.Sound("laser5.ogg")

        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the block sprites
        for i in range(50):

            block = Block()

            block.rect.x = random.randrange(SCREEN_WIDTH - Block.WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT - Block.WIDTH)

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

            # See if the player block has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # Check the list of collisions.
            for block in blocks_hit_list:
                self.score += 1
                print(self.score)
                # play the sound when the player block collides with other block
                self.sound.play()

            if len(self.block_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(PINK)

        # displays ladder
        pygame.draw.rect(screen, BROWN, [200, 0, SCREEN_WIDTH / 2, SCREEN_HEIGHT],0)

        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        self.display_feedback(screen)

        pygame.display.flip()

    # add the score to the display
    def display_feedback(self, screen):
        # draw blue rectangle at coordinates (50,400)
        # with a width of 100 and height of 50
        pygame.draw.rect(screen, TEAL, [50, 400, 100, 50], 0)
        # initialize font style
        font = pygame.font.SysFont('Calibri', 25, True, False)
        # render score text
        score_str = font.render("Score: " + str(self.score), True, WHITE)
        # display it in the box at coordinates (62, 416)
        screen.blit(score_str, [60, 416])


def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)

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
