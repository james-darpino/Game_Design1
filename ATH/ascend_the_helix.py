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

hp = 10.0

game_state = "menu"
screen = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
clock = pygame.time.Clock()

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
            self.create_nucleic_acids()

        # Create the ion sprites
        for i in range(10):
            self.create_ions()

        # Create the player
        self.player = Player.Player()
        self.all_sprites_list.add(self.player)

        self.image = pygame.Surface([Globals.HELIX_WIDTH, Globals.HELIX_HEIGHT])
        self.rect = self.image.get_rect()

    def game_intro(self):
        global game_state, screen

        while game_state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_state = "game"
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_2:
                        game_state = "how_to_play"
                        self.how_to_play_screen()

            screen.fill(Globals.BLACK)
            # draw images on the screen
            logo = pygame.image.load("logo.png").convert_alpha()
            logo = pygame.transform.scale(logo, (Globals.LOGO_WIDTH, Globals.LOGO_HEIGHT))
            screen.blit(logo, (Globals.LOGO_X, Globals.LOGO_Y))

            start_text = pygame.image.load("start.png").convert_alpha()
            start_text = pygame.transform.scale(start_text, (Globals.START_WIDTH, Globals.START_HEIGHT))
            screen.blit(start_text, (Globals.START_X, Globals.START_Y))

            how_to_play_text = pygame.image.load("how_to_play.png").convert_alpha()
            how_to_play_text = pygame.transform.scale(how_to_play_text, (Globals.HOW_TO_PLAY_WIDTH,
                                                                         Globals.HOW_TO_PLAY_HEIGHT))
            screen.blit(how_to_play_text, (Globals.HOW_TO_PLAY_X, Globals.HOW_TO_PLAY_Y))

            pygame.display.flip()
            clock.tick(60)

    def how_to_play_screen(self):
        global game_state, screen
        clock = pygame.time.Clock()

        while game_state == "how_to_play":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_state = "menu"
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

            screen.fill(Globals.BLACK)

            # draw images on the screen
            logo = pygame.image.load("logo.png").convert_alpha()
            logo = pygame.transform.scale(logo, (Globals.LOGO_WIDTH, Globals.LOGO_HEIGHT))
            screen.blit(logo, (Globals.LOGO_X, Globals.LOGO_Y))

            rules = pygame.image.load("rules.png").convert_alpha()
            rules = pygame.transform.scale(rules, (Globals.RULES_WIDTH, Globals.RULES_HEIGHT))
            screen.blit(rules, (Globals.RULES_X, Globals.RULES_Y))

            move_rule = pygame.image.load("movement_rule.png").convert_alpha()
            move_rule = pygame.transform.scale(move_rule, (Globals.MOVE_RULE_WIDTH, Globals.MOVE_RULE_HEIGHT))
            screen.blit(move_rule, (Globals.MOVE_RULE_X, Globals.MOVE_RULE_Y))

            ion_rule = pygame.image.load("ion_rule.png").convert_alpha()
            ion_rule = pygame.transform.scale(ion_rule, (Globals.ION_RULE_WIDTH, Globals.ION_RULE_HEIGHT))
            screen.blit(ion_rule, (Globals.ION_RULE_X, Globals.ION_RULE_Y))

            hp_regen_rule = pygame.image.load("health_regen_rule.png").convert_alpha()
            hp_regen_rule = pygame.transform.scale(hp_regen_rule, (Globals.HP_REGEN_RULE_WIDTH,
                                                                   Globals.HP_REGEN_RULE_HEIGHT))
            screen.blit(hp_regen_rule, (Globals.HP_REGEN_RULE_X, Globals.HP_REGEN_RULE_Y))

            survive_rule = pygame.image.load("survive_rule.png").convert_alpha()
            survive_rule = pygame.transform.scale(survive_rule,
                                                  (Globals.SURVIVE_RULE_WIDTH, Globals.SURVIVE_RULE_HEIGHT))
            screen.blit(survive_rule, (Globals.SURVIVE_RULE_X, Globals.SURVIVE_RULE_Y))

            back_button = pygame.image.load("back.png").convert_alpha()
            back_button = pygame.transform.scale(back_button, (Globals.BACK_BUTTON_WIDTH, Globals.BACK_BUTTON_HEIGHT))
            screen.blit(back_button, (Globals.BACK_BUTTON_X, Globals.BACK_BUTTON_Y))

            pygame.display.flip()
            clock.tick(60)

    def game_over_screen(self):
        global screen, hp, game_state
        print(game_state)
        while game_state == "game_over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        hp = 100
                        game_state = "game"

            # draw images on the screen
            screen.fill(Globals.BLACK)
            logo = pygame.image.load("logo.png").convert_alpha()
            logo = pygame.transform.scale(logo, (Globals.LOGO_WIDTH, Globals.LOGO_HEIGHT))
            screen.blit(logo, (Globals.LOGO_X, Globals.LOGO_Y))

            game_over_text = pygame.image.load("game_over.png").convert_alpha()
            game_over_text = pygame.transform.scale(game_over_text, (900, 300))
            screen.blit(game_over_text, (250, 300))

            pygame.display.flip()
            clock.tick(60)


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def create_nucleic_acids(self):
        adenine = nucleicAcid.Adenine()
        cytosine = nucleicAcid.Cytosine()
        guanine = nucleicAcid.Guanine()
        thymine = nucleicAcid.Thymine()

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

    def create_ions(self):
        # create instances of proton, neutron and electron
        proton = Ion.Proton()
        neutron = Ion.Neutron()
        electron = Ion.Electron()

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

    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
        while game_state == "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

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
        global hp, game_state

        # Move all the sprites
        self.all_sprites_list.update()
        # See if the player has collided with anything.
        ions_hit_list = pygame.sprite.spritecollide(self.player, self.ion_list, True)
        nucleic_acid_hit_list = pygame.sprite.spritecollide(self.player, self.nucleic_acid_list, True)

        self.score += 1

        # Check the list of collisions.
        for _ in ions_hit_list:
            hp = hp - 10
            self.create_ions()
            if hp == 0:
                self.sound.play()
                game_state = "game_over"

        for _ in nucleic_acid_hit_list:
            hp = hp + 10
            self.sound2.play()

            if hp >= 100:
                hp = 100

            if len(self.nucleic_acid_list) == 0:
                print("Done")
                self.create_nucleic_acids()

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

    # def DISPLAY_BACKGROUND(self):
    #     screen = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
    #     background = pygame.image.load("Space 2.png").convert_alpha()
    #     background = pygame.transform.scale(background, (Globals.SCREEN_WIDTH + 300, Globals.SCREEN_HEIGHT))
    #     screen.blit(background, (-200, 0))

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        global hp, game_state
        score_str = "Score: " + str(self.score)
        health_str = "Health: " + str(hp)
        screen.fill(Globals.BLACK)
        # self.DISPLAY_BACKGROUND()

        if game_state == "game":
            image = pygame.image.load("pairs.png").convert_alpha()
            image = pygame.transform.scale(image, (Globals.HELIX_WIDTH + 600, Globals.HELIX_HEIGHT))
            screen.blit(image, (Globals.HELIX_X - 250, Globals.HELIX_Y))

            self.all_sprites_list.draw(screen)

            pygame.draw.rect(screen, Globals.BLACK, [0, 0, 175, Globals.SCREEN_HEIGHT], 0)

            font = pygame.font.SysFont('georgiattf', 25, True, False)
            text = font.render(score_str, True, Globals.WHITE)
            screen.blit(text, [10, Globals.SCREEN_WIDTH / 18])

            font = pygame.font.SysFont('georgiattf', 25, True, False)
            text = font.render(health_str, True, Globals.WHITE)
            screen.blit(text, [10, Globals.SCREEN_HEIGHT / 15])

            font = pygame.font.SysFont('georgiattf', 20, False, False)
            text = font.render("Ascend the Helix!", True, Globals.WHITE)
            screen.blit(text, [10, Globals.SCREEN_HEIGHT / 35])

        pygame.display.flip()


def main():
    global screen

    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    pygame.display.set_caption("Ascend the Helix")
    pygame.mouse.set_visible(True)

    # Create our objects and set the data
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()
    done = False
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play(-1)

    # calls the menu screen before loop so that menu appears first
    game.game_intro()

    # Main game loop
    while game_state == "game":

        # Process events (keystrokes, mouse clicks, etc)
        game.process_events()

        # Update object positions, check for collisions
        game.run_logic()
        if hp == 0:

            game.game_over_screen()

        # Draw the current frame
        game.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

        pygame.display.flip()


# Call the main function, start up the game
if __name__ == "__main__":
    main()
