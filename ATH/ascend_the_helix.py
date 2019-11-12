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
import Globals
import Player
import Ion
import nucleicAcid

hp = 100.0


class Menu(object):
    def __init__(self):
        TEXT_SIZE = 36
        TEXT_X = 10
        TEXT_Y_LINE1 = 10
        TEXT_Y_LINE2 = 50

        ATH_text_X = 0
        ATH_text_Y = 10
        start_text_X = 275
        start_text_Y = 200
        instruction_text_X = 190
        instruction_text_Y = 300
        size = [Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT]
        self = pygame.display.set_mode(size)


class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    def __init__(self):

        """ Constructor. Create all our attributes and initialize
        the game. """

        # add the laser sound (laser5.ogg file)
        self.sound = pygame.mixer.Sound("lose.ogg")
        self.sound2 = pygame.mixer.Sound("collect.wav")
        self.score = 0
        self.game_over = False

        # Create sprite lists
        self.ion_list = pygame.sprite.Group()
        self.nucleic_acid_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create the nucleic sprites
        for i in range(1):
            adenine = nucleicAcid.Adenine()
            cytosine = nucleicAcid.Cytosine()
            guanine = nucleicAcid.Guanine()
            thymine = nucleicAcid.Thymine()

            # add adenine to the list
            self.nucleic_acid_list.add(adenine)
            self.all_sprites_list.add(adenine)

            # add cytosine to the list
            self.nucleic_acid_list.add(cytosine)
            self.all_sprites_list.add(cytosine)

            # add guanine to the list
            self.nucleic_acid_list.add(guanine)
            self.all_sprites_list.add(guanine)

            # add thymine to the list
            self.nucleic_acid_list.add(thymine)
            self.all_sprites_list.add(thymine)

        # Create the ion sprites
        for i in range(10):
            # create instances of proton, neutron and electron
            proton = Ion.Proton()
            neutron = Ion.Neutron()
            electron = Ion.Electron()

            # create adenine acids
            adenine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
            adenine.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

            # create cytosine acids
            cytosine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
            cytosine.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

            # create guanine acids
            guanine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
            guanine.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

            # create thymine acids
            thymine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
            thymine.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

            # # create proton ions
            proton.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
            proton.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

            # create neutron ions
            neutron.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
            neutron.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

            # create electron ions
            electron.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
            electron.rect.x = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)

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
        self.player = Player.Player()
        self.all_sprites_list.add(self.player)

        self.image = pygame.Surface([Globals.HELIX_WIDTH, Globals.HELIX_HEIGHT])
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

        if not self.game_over:
            global hp
            # Move all the sprites
            self.all_sprites_list.update()
            # See if the player has collided with anything.
            ions_hit_list = pygame.sprite.spritecollide(self.player, self.ion_list, True)
            nucleic_acid_hit_list = pygame.sprite.spritecollide(self.player, self.nucleic_acid_list, True)

            self.score += 1

            # Check the list of collisions.
            for _ in ions_hit_list:
                hp = hp - 10
                print(hp)
                if hp == 0:
                    self.game_over = True
                    self.sound.play()

            for _ in nucleic_acid_hit_list:
                hp = hp + 10
                self.sound2.play()
                if hp >= 100:
                    hp = 100

            # Boundary check for player leaving helix left side
            if self.player.rect.x <= Globals.HELIX_LEFT_BOUNDARY:
                self.player.stop()
                self.player.rect.x = Globals.HELIX_LEFT_BOUNDARY

            # Boundary check for player leaving helix right side
            if self.player.rect.x >= Globals.HELIX_RIGHT_BOUNDARY:
                self.player.stop()
                self.player.rect.x = Globals.HELIX_RIGHT_BOUNDARY

            # Boundary check for player leaving helix bottom
            if self.player.rect.y >= Globals.SCREEN_HEIGHT:
                self.player.stop()
                self.player.rect.y = Globals.SCREEN_HEIGHT - Globals.PLAYER_HEIGHT

            # Boundary check for player leaving helix top
            if self.player.rect.y <= 0:
                self.player.stop()
                self.player.rect.y = 0

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        global hp
        score_str = "Score: " + str(self.score)
        health_str = "Health: " + str(hp)
        screen.fill(Globals.BLACK)

        if self.game_over:
            font = pygame.font.SysFont("georgiattf", 25)
            text = font.render("Game Over! An ion broke down your DNA. Click to restart!", True, Globals.WHITE)
            center_x = (Globals.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (Globals.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
            hp = 100

        if not self.game_over:
            # image = pygame.image.load("blue_helix.png")
            # image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            # screen.blit(image, (0, 0))

            image = pygame.image.load("pairs.png").convert_alpha()
            image = pygame.transform.scale(image, (Globals.HELIX_WIDTH, Globals.HELIX_HEIGHT))
            screen.blit(image, (Globals.HELIX_X, Globals.HELIX_Y))

            self.all_sprites_list.draw(screen)

            # image = pygame.image.load("blue_helix_175.png")
            # image = pygame.transform.scale(image, (175, SCREEN_HEIGHT))
            # screen.blit(image, (0, 0))

            pygame.draw.rect(screen, Globals.BLACK, [0, 0, 175, Globals.SCREEN_HEIGHT], 0)

            font = pygame.font.SysFont('georgiattf', 25, True, False)
            text = font.render(score_str, True, Globals.WHITE)
            screen.blit(text, [10, Globals.SCREEN_WIDTH / 12])

            font = pygame.font.SysFont('georgiattf', 25, True, False)
            text = font.render(health_str, True, Globals.WHITE)
            screen.blit(text, [10, Globals.SCREEN_HEIGHT / 15])

            font = pygame.font.SysFont('georgiattf', 20, False, False)
            text = font.render("Ascend the Helix!", True, Globals.WHITE)
            screen.blit(text, [10, Globals.SCREEN_HEIGHT / 35])
            # Player.do_health(self)
        pygame.display.flip()


def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    size = [Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT]
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
