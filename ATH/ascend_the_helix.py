"""
A. Authors: James D'Arpino and Hannah Youssef
B. Version: Alpha 2.0
C. Description of code: This displays the player within the Helix.
The player needs to avoid the falling ions (Proton, Neutron, Electron).
If the player collides with a falling ion, he/she dies and the game is over.
The goal for the alpha, is to get the highest score.
D. Description of how to play: Press the arrow directionals to move.
The goal is to avoid the falling ions and attain the highest score.
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

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40

HELIX_X = SCREEN_WIDTH // 4
HELIX_Y = 0
HELIX_WIDTH = SCREEN_WIDTH // 2
HELIX_HEIGHT = SCREEN_HEIGHT
HELIX_RIGHT_BOUNDARY = SCREEN_WIDTH / 1.4
HELIX_LEFT_BOUNDARY = SCREEN_WIDTH / 4

health = 100.0
maxHealth = 100
healthDashes = 10
# --- Classes ---
# class Game_State(pygame):
# #     def __init__(self):
# #         super().__init__()
# #     def start_screen(self):
# #
# #     def game_screen(self):
# #
# #     def game_over_screen(self):
# #


class Proton(pygame.sprite.Sprite):
    """ This class represents a Proton which the player must dodge. """
    ION_WIDTH = 25
    ION_HEIGHT = 25

    def __init__(self):
        """ Constructor, create the image of the Proton. """
        super().__init__()
        self.image = pygame.Surface([self.ION_WIDTH, self.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("proton.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.ION_WIDTH, self.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """ Shows the range and boundaries of where the ion should be placed. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 2

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Neutron(pygame.sprite.Sprite):
    """ This class represents a Neutron which the player must dodge. """
    ION_WIDTH = 25
    ION_HEIGHT = 25

    def __init__(self):
        """ Constructor, create the image of the Neutron. """
        super().__init__()
        self.image = pygame.Surface([self.ION_WIDTH, self.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("neutron.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.ION_WIDTH, self.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """ Shows the range and boundaries of where the ion should be placed. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
        self.rect.y += 2

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Electron(pygame.sprite.Sprite):
    """ This class represents a Electron which the player must dodge. """
    ION_WIDTH = 25
    ION_HEIGHT = 25

    def __init__(self):
        """ Constructor, create the image of the Electron. """
        super().__init__()
        self.image = pygame.Surface([self.ION_WIDTH, self.ION_HEIGHT])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("electron.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.ION_WIDTH, self.ION_HEIGHT))

    def draw(self, screen):
        """ Maps the image to the rectangle. """
        screen.blit(self.image, self.rect)

    def reset_pos(self):
        """ Shows the range and boundaries of where the ion should be placed. """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)

    def update(self):
        """ Automatically called when we need to move the ion. """
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
        self.rect = self.image.get_rect()
        self.rect.x = self.starting_position_x
        self.rect.y = self.starting_position_y
        # import man climbing image
        self.image = pygame.image.load("man_climbing.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))

    def do_health(self):
        dash_convert = int(maxHealth / healthDashes)
        current_dashes = int(health / dash_convert)

        remaining_health = healthDashes - current_dashes
        health_display = "-" * current_dashes
        remaining_display = " " * remaining_health
        percent = str(int((health / maxHealth) * 100)) + "%"

        print("|" + health_display + remaining_display + "|")  # Print out textbased healthbar
        print("         " + percent)

    def draw(self, screen):
        # blit the image to the screen
        screen.blit(self.image, self.rect)

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
    image = pygame.image.load("pairs.png").convert_alpha()
    image = pygame.transform.scale(image, (HELIX_WIDTH, HELIX_HEIGHT))
    screen.blit(image, (HELIX_X, HELIX_Y))


class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    def __init__(self):

        """ Constructor. Create all our attributes and initialize
        the game. """

        # add the laser sound (laser5.ogg file)
        self.sound = pygame.mixer.Sound("lose.ogg")

        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.ion_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the ion sprites
        for i in range(10):
            # create instances of proton, neutron and electron
            proton = Proton()
            neutron = Neutron()
            electron = Electron()

            # create proton ions
            proton.rect.y = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)
            proton.rect.x = random.randrange(HELIX_WIDTH - Proton.ION_WIDTH)
            proton.rect.y = random.randrange(-300, HELIX_HEIGHT - Proton.ION_WIDTH)

            # create neutron ions
            neutron.rect.y = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)
            neutron.rect.x = random.randrange(HELIX_WIDTH - Neutron.ION_WIDTH)
            neutron.rect.y = random.randrange(-300, HELIX_HEIGHT - Neutron.ION_WIDTH)

            # create electron ions
            electron.rect.y = random.uniform(HELIX_LEFT_BOUNDARY, HELIX_RIGHT_BOUNDARY)
            electron.rect.x = random.randrange(HELIX_WIDTH - Electron.ION_WIDTH)
            electron.rect.y = random.randrange(-300, HELIX_HEIGHT - Electron.ION_WIDTH)

            # add protons to the list
            self.ion_list.add(proton)
            self.all_sprites_list.add(proton)

            # add neutrons to the list
            self.ion_list.add(neutron)
            self.all_sprites_list.add(neutron)

            # add electrons to the list
            self.ion_list.add(electron)
            self.all_sprites_list.add(electron)

        # Create the player
        self.player = Player()
        self.all_sprites_list.add(self.player)

        self.image = pygame.Surface([HELIX_WIDTH, HELIX_HEIGHT])
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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
        global health, healthDashes, maxHealth
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()

            # See if the player has collided with anything.
            ions_hit_list = pygame.sprite.spritecollide(self.player, self.ion_list, True)

            self.score += 1
            # Check the list of collisions.
            for _ in ions_hit_list:
                health = health - 10
                if health == 0:
                    self.game_over = True
                    self.sound.play()

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
        health_str = "Health: " + str(health)
        screen.fill(BLACK)

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("georgiattf", 25)
            text = font.render("Game Over! An ion broke down your DNA. Click to restart!", True, WHITE)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            # image = pygame.image.load("blue_helix.png")
            # image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            # screen.blit(image, (0, 0))

            display_feedback(screen)
            self.all_sprites_list.draw(screen)

            # image = pygame.image.load("blue_helix_175.png")
            # image = pygame.transform.scale(image, (175, SCREEN_HEIGHT))
            # screen.blit(image, (0, 0))

            pygame.draw.rect(screen, BLACK, [0, 0, 175, SCREEN_HEIGHT], 0)

            font = pygame.font.SysFont('georgiattf', 25, True, False)
            text = font.render(score_str, True, WHITE)
            screen.blit(text, [10, SCREEN_HEIGHT / 12])

            font = pygame.font.SysFont('georgiattf', 25, True, False)
            text = font.render(health_str, True, WHITE)
            screen.blit(text, [10, SCREEN_HEIGHT / 7])

            font = pygame.font.SysFont('georgiattf', 20, False, False)
            text = font.render("Ascend the Helix!", True, WHITE)
            screen.blit(text, [10, SCREEN_HEIGHT / 35])
            Player.do_health(self)
        pygame.display.flip()

    # this is the code for the instruction screen
    # def menu_screen(screen):
    #     size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    #     screen = pygame.display.set_mode(size)
    #
    #     # Loop until the user clicks the close button.
    #     done = False
    #
    #     # Used to manage how fast the screen updates
    #     clock = pygame.time.Clock()
    #
    #     # This is a font we use to draw text on the screen (size 36)
    #     font = pygame.font.Font(None, 36)
    #
    #     display_instructions = True
    #     instruction_page = 1
    #
    #     # -------- Instruction Page Loop -----------
    #     while not done and display_instructions:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 done = True
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 instruction_page += 1
    #                 if instruction_page == 3:
    #                     display_instructions = False
    #
    #         # Set the screen background
    #         screen.fill(BLACK)
    #
    #         if instruction_page == 1:
    #             # Draw instructions, page 1
    #             # This could also load an image created in another program.
    #             # That could be both easier and more flexible.
    #
    #             text = font.render("Welcome to Ascend the Helix!", True, WHITE)
    #             screen.blit(text, [10, 10])
    #
    #             text = font.render("Page 1", True, WHITE)
    #             screen.blit(text, [10, 40])
    #
    #         if instruction_page == 2:
    #             # Draw instructions, page 2
    #             text = font.render("This is Page 2 of the menu screen.", True, WHITE)
    #             screen.blit(text, [10, 10])
    #
    #             text = font.render("Page 2", True, WHITE)
    #             screen.blit(text, [10, 40])
    #
    #         # Limit to 60 frames per second
    #         clock.tick(60)
    #
    #         # Go ahead and update the screen with what we've drawn.
    #         pygame.display.flip()


def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Ascend the Helix")
    pygame.mouse.set_visible(True)

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1)

    # Main game loop
    while not done:
        # game.menu_screen()

        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()

        # Update object positions, check for collisions
        game.run_logic()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

        pygame.display.flip()

    # Close window and exit
    pygame.quit()


# Call the main function, start up the game
if __name__ == "__main__":
    main()
