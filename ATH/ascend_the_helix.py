"""
A. Authors: James D'Arpino and Hannah Youssef

B. Version: Patch 3.0

C. Description of code: This displays the player within the Helix.
The player needs to avoid the falling ions (Proton, Neutron, Electron).
If the player collides with a falling ion, he/she loses 10 health points.
Once the player gets to 0 health points they die. In order to survive,
the player must collect nucleic acids (Adenine, Guanine, Thymine, and Cytosine).
Each acid collected restores 10 health points. The goal is to survive as long
as possible and keep trying to beat your highest score.

D. Description of how to play: Press the arrow directionals to move.
Avoid the falling ions, while collecting the nucleic acids. Try to Survive for
as long as possible
"""

import pygame
import random
import Globals
import Player
import Ion
import nucleicAcid
import Helix

import sys
from pygame.locals import *

hp = 100
score = 0
game_state = "menu"
screen = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
clock = pygame.time.Clock()

print(pygame.font.get_fonts())


def game_over_screen():
    global screen, hp, game_state, score

    while game_state == "game_over":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    hp = 100
                    score = 0
                    game_state = "game"
                    main()

        # draw images on the screen
        screen.fill(Globals.BLACK)

        background_game_over = pygame.image.load("background.png").convert_alpha()
        background_game_over = pygame.transform.scale(background_game_over, (Globals.SCREEN_WIDTH + 300,
                                                                             Globals.SCREEN_HEIGHT))
        screen.blit(background_game_over, (-200, 0))

        character_death = pygame.image.load("character_death.png").convert_alpha()
        character_death = pygame.transform.scale(character_death, (300, 300))
        screen.blit(character_death, (550, 250))

        grave = pygame.image.load("rip.png").convert_alpha()
        grave = pygame.transform.scale(grave, (150, 200))
        screen.blit(grave, (900, 350))

        game_over_text = pygame.image.load("game_over.png").convert_alpha()
        game_over_text = pygame.transform.scale(game_over_text, (900, 300))
        screen.blit(game_over_text, (250, 75))

        pygame.display.flip()
        clock.tick(60)


def victory_screen():
    global screen, hp, game_state, score

    while game_state == "victory":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    hp = 100
                    score = 0
                    quit()

        # draw images on the screen
        screen.fill(Globals.BLACK)

        background_victory = pygame.image.load("classroom.jpg").convert_alpha()
        background_victory = pygame.transform.scale(background_victory, (Globals.SCREEN_WIDTH + 300,
                                                                         Globals.SCREEN_HEIGHT))
        screen.blit(background_victory, (-200, 0))

        frizzle = pygame.image.load("ms_frizzle.png").convert_alpha()
        frizzle = pygame.transform.scale(frizzle, (300, 300))
        screen.blit(frizzle, (300, 350))

        win = pygame.image.load("win.png").convert_alpha()
        win = pygame.transform.scale(win, (900, 300))
        screen.blit(win, (250, 75))

        pygame.display.flip()
        clock.tick(60)


def how_to_play_screen():
    global game_state, screen

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
        background = pygame.image.load("background.png").convert_alpha()
        background = pygame.transform.scale(background, (Globals.SCREEN_WIDTH + 300, Globals.SCREEN_HEIGHT))
        screen.blit(background, (-200, 0))

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


def credits_screen():
    global game_state, screen

    while game_state == "credits":
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
        background = pygame.image.load("background.png").convert_alpha()
        background = pygame.transform.scale(background, (Globals.SCREEN_WIDTH + 300, Globals.SCREEN_HEIGHT))
        screen.blit(background, (-200, 0))

        logo = pygame.image.load("logo.png").convert_alpha()
        logo = pygame.transform.scale(logo, (Globals.LOGO_WIDTH, Globals.LOGO_HEIGHT))
        screen.blit(logo, (Globals.LOGO_X, Globals.LOGO_Y))

        back_button = pygame.image.load("back.png").convert_alpha()
        back_button = pygame.transform.scale(back_button, (Globals.BACK_BUTTON_WIDTH, Globals.BACK_BUTTON_HEIGHT))
        screen.blit(back_button, (Globals.BACK_BUTTON_X, Globals.BACK_BUTTON_Y))

        author = pygame.image.load("authors.png").convert_alpha()
        author = pygame.transform.scale(author, (600, 200))
        screen.blit(author, (Globals.HOW_TO_PLAY_X - 200, Globals.HOW_TO_PLAY_Y + 100))

        pygame.display.flip()
        clock.tick(60)


def game_intro():
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
                    how_to_play_screen()
                if event.key == pygame.K_3:
                    game_state = "credits"
                    credits_screen()

        screen.fill(Globals.BLACK)

        # draw images on the screen
        background = pygame.image.load("background.png").convert_alpha()
        background = pygame.transform.scale(background, (Globals.SCREEN_WIDTH + 300, Globals.SCREEN_HEIGHT))
        screen.blit(background, (-200, 0))

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

        credits_page = pygame.image.load("credits.png").convert_alpha()
        credits_page = pygame.transform.scale(credits_page, (Globals.HOW_TO_PLAY_WIDTH, Globals.HOW_TO_PLAY_HEIGHT))
        screen.blit(credits_page, (Globals.HOW_TO_PLAY_X - 10, Globals.HOW_TO_PLAY_Y + 100))

        pygame.display.flip()
        clock.tick(60)


def scrolling_helix(surface):
    # center_x = HELIX_START_X = (SCREEN_WIDTH - HELIX_IMG_WIDTH) / 2
    # helix_y1 = HELIX_Y_OFF_SCREEN = -1 * SCREEN_HEIGHT
    # helix_y2 =  HELIX_Y = 0

    image = pygame.image.load("pairs.png").convert()

    # surface.blit(image, (center_x, Globals.HELIX_Y))
    # surface.blit(image, (center_x, (Globals.HELIX_Y - Globals.HELIX_IMG_HEIGHT)))

    for _ in range(1):
        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         pygame.quit()
        #         quit()
        surface.blit(image, (Globals.HELIX_START_X, Globals.HELIX_Y_OFF_SCREEN))
        surface.blit(image, (Globals.HELIX_START_X, Globals.HELIX_Y))

        Globals.HELIX_Y_OFF_SCREEN += Globals.SCROLL_SPEED
        Globals.HELIX_Y += Globals.SCROLL_SPEED

        if Globals.HELIX_Y_OFF_SCREEN == Globals.SCREEN_HEIGHT:
            Globals.HELIX_Y_OFF_SCREEN = Globals.HELIX_Y - Globals.SCREEN_HEIGHT
            Globals.HELIX_Y = 0
        if Globals.HELIX_Y == Globals.SCREEN_HEIGHT:
            Globals.HELIX_Y = Globals.HELIX_Y_OFF_SCREEN - Globals.SCREEN_HEIGHT
            Globals.HELIX_Y_OFF_SCREEN = 0

        # Globals.HELIX_Y += 2.5


# pygame.display.update()


# background_surface = pygame.surface.Surface(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
# def scrolling_helix(surface):
#
#     # starts above the screen at -800
#     helix_y1 = -1 * Globals.SCREEN_HEIGHT
#     # starts at the top of the screen at 0
#     helix_y2 = 0
#     # center width to put helix
#     center_x = (Globals.SCREEN_WIDTH - Globals.HELIX_IMG_WIDTH) / 2
#
#     # load images for both
#     helix_img1 = helix_img2 = pygame.image.load('pairs.png').convert()
#     # helix_img2 = pygame.image.load('pairs.png').convert()
#
#     done = False
#     while not done:
#         # renders helix images to above the screen and at 0
#         surface.blit(helix_img1, (center_x, helix_y1))
#         surface.blit(helix_img2, (center_x, helix_y2))
#
#         # moves helix down 1 pixel per frame
#         helix_y1 += 1
#         helix_y2 += 1
#
#         # if first image goes off the screen, place second image on top of it
#         if helix_y1 == Globals.SCREEN_HEIGHT:
#             helix_y1 = helix_y2 - Globals.SCREEN_HEIGHT
#             helix_y2 = 0
#         if helix_y2 == Globals.SCREEN_HEIGHT:
#             helix_y2 = helix_y1 - Globals.SCREEN_HEIGHT
#             helix_y1 = 0
#
#         # update screen
#         pygame.display.update()
#
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 quit()


class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """

        # add the sound files
        self.sound = pygame.mixer.Sound("lose.ogg")
        self.sound2 = pygame.mixer.Sound("collect.wav")
        self.sound3 = pygame.mixer.Sound("WAHOO.wav")

        self.game_over = False

        # Create sprite lists
        self.ion_list = pygame.sprite.Group()
        self.nucleic_acid_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        # self.background_list = pygame.sprite.Group()

        # Create the nucleic sprites
        for i in range(1):
            self.create_nucleic_acids()

        # Create the ion sprites
        for i in range(10):
            self.create_ions()

        # for i in range(100000):
        #     self.create_helix()

        # Create the player
        self.player = Player.Player()
        self.all_sprites_list.add(self.player)

        # self.helix = Helix.Helix()
        # self.background_list.add(self.helix)

        self.image = pygame.Surface([Globals.HELIX_WIDTH, Globals.HELIX_HEIGHT])
        # self.image = pygame.Surface([Globals.HELIX_IMG_WIDTH, Globals.HELIX_IMG_HEIGHT])
        # self.image = pygame.Surface([610, 800])
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # surface.blit(self.scrolling_helix(screen))

    # def create_helix(self):
    #     # helix = Helix.helix()
    #     center_x = (Globals.SCREEN_WIDTH - Globals.HELIX_IMG_WIDTH) / 2
    #     helix_y1 = -1 * Globals.SCREEN_HEIGHT
    #     helix_y2 = 0
    #     helix_img1 = helix_img2 = pygame.image.load('pairs.png').convert()
    #     while True:
    #
    #         # renders helix images to above the screen and at 0
    #         screen.blit(helix_img1, (center_x, helix_y1))
    #         screen.blit(helix_img2, (center_x, helix_y2))
    #
    #         # moves helix down 1 pixel per frame
    #         helix_y1 += 1
    #         helix_y2 += 1
    #
    #         # if first image goes off the screen, place second image on top of it
    #         if helix_y1 == Globals.SCREEN_HEIGHT:
    #             helix_y1 = helix_y2 - Globals.SCREEN_HEIGHT
    #             helix_y2 = 0
    #         if helix_y2 == Globals.SCREEN_HEIGHT:
    #             helix_y2 = helix_y1 - Globals.SCREEN_HEIGHT
    #             helix_y1 = 0
    #
    #         # update screen
    #         pygame.display.update()
    #
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 quit()

    def create_nucleic_acids(self):
        adenine = nucleicAcid.Adenine()
        cytosine = nucleicAcid.Cytosine()
        guanine = nucleicAcid.Guanine()
        thymine = nucleicAcid.Thymine()

        # create adenine acids
        adenine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
        adenine.rect.y = random.randrange(-300, Globals.HELIX_HEIGHT - Globals.NUCLEIC_ACID_WIDTH)

        # create cytosine acids
        cytosine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
        cytosine.rect.y = random.randrange(-300, Globals.HELIX_HEIGHT - Globals.NUCLEIC_ACID_WIDTH)

        # create guanine acids
        guanine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
        guanine.rect.y = random.randrange(-300, Globals.HELIX_HEIGHT - Globals.NUCLEIC_ACID_WIDTH)

        # create thymine acids
        thymine.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
        thymine.rect.y = random.randrange(-300, Globals.HELIX_HEIGHT - Globals.NUCLEIC_ACID_WIDTH)

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

        # create proton ions
        proton.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
        proton.rect.y = random.randrange(-300, Globals.HELIX_HEIGHT - Globals.ION_WIDTH)

        # create neutron ions
        neutron.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
        neutron.rect.y = random.randrange(-300, Globals.HELIX_HEIGHT - Globals.ION_WIDTH)

        # create electron ions
        electron.rect.y = random.uniform(Globals.HELIX_LEFT_BOUNDARY, Globals.HELIX_RIGHT_BOUNDARY)
        electron.rect.y = random.randrange(-300, Globals.HELIX_HEIGHT - Globals.ION_WIDTH)

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        global hp, game_state, score

        # Move all the sprites
        self.all_sprites_list.update()

        # See if the player has collided with anything.
        ions_hit_list = pygame.sprite.spritecollide(self.player, self.ion_list, True)
        nucleic_acid_hit_list = pygame.sprite.spritecollide(self.player, self.nucleic_acid_list, True)

        score += 10
        if score >= 50000:
            self.sound3.play()
            game_state = "victory"

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

            if hp > 100:
                score += 1000

            if hp >= 100:
                hp = 100

            if len(self.nucleic_acid_list) == 0:
                self.create_nucleic_acids()

        # Boundary check for player leaving helix left side
        if self.player.rect.x <= Globals.HELIX_LEFT_BOUNDARY:
            self.player.stop()
            self.player.rect.x = Globals.HELIX_LEFT_BOUNDARY + 5

        # Boundary check for player leaving helix right side
        if self.player.rect.x >= Globals.HELIX_RIGHT_BOUNDARY:
            self.player.stop()
            self.player.rect.x = Globals.HELIX_RIGHT_BOUNDARY - 5

        # Boundary check for player leaving helix bottom
        if self.player.rect.y >= Globals.SCREEN_HEIGHT:
            self.player.stop()
            self.player.rect.y = Globals.SCREEN_HEIGHT - Globals.PLAYER_HEIGHT

        # Boundary check for player leaving helix top
        if self.player.rect.y <= 0:
            self.player.stop()
            self.player.rect.y = 0

    # def scrolling_helix(self, surface):
    #
    #     # background_surface = pygame.Surface(Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
    #
    #     # starts above the screen at -800
    #     helix_y1 = -1 * Globals.SCREEN_HEIGHT
    #     # starts at the top of the screen at 0
    #     helix_y2 = 0
    #     # center width to put helix
    #     center_x = (Globals.SCREEN_WIDTH - Globals.HELIX_IMG_WIDTH) / 2
    #
    #     # load images for both
    #     helix_img1 = helix_img2 = pygame.image.load('pairs.png').convert()
    #
    #
    #     while True:
    #         # renders helix images to above the screen and at 0
    #         screen.blit(helix_img1, (center_x, helix_y1))
    #         screen.blit(helix_img2, (center_x, helix_y2))
    #
    #         # moves helix down 1 pixel per frame
    #         helix_y1 += 1
    #         helix_y2 += 1
    #
    #         # if first image goes off the screen, place second image on top of it
    #         if helix_y1 == Globals.SCREEN_HEIGHT:
    #             helix_y1 = helix_y2 - Globals.SCREEN_HEIGHT
    #             helix_y2 = 0
    #         if helix_y2 == Globals.SCREEN_HEIGHT:
    #             helix_y2 = helix_y1 - Globals.SCREEN_HEIGHT
    #             helix_y1 = 0
    #
    #         # update screen
    #         pygame.display.update()
    #
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 quit()

    def display_frame(self, surface):
        """ Display everything to the screen for the game. """
        global hp, game_state
        score_str = "Score: " + str(score)
        health_str = "Health: " + str(hp)
        surface.fill(Globals.BLACK)

        if game_state == "game":

            scrolling_helix(surface)
            self.all_sprites_list.draw(surface)

            pygame.draw.rect(surface, Globals.BLACK, [0, 0, 175, Globals.SCREEN_HEIGHT], 0)

            # "Your Statistics" rendered text
            font = pygame.font.SysFont('dubai', 40, True, False)
            text = font.render("Your Statistics:", True, Globals.WHITE)
            surface.blit(text, [10, Globals.SCREEN_HEIGHT - 780])

            # "Health: " out of 100 rendered text
            # if health gets below 40, make text red, bold, and have exclamation points
            if 0 <= hp <= 40:
                font = pygame.font.SysFont('dubai', 35, True, False)
                text = font.render(health_str + " / 100 !!!", True, Globals.RED)
                surface.blit(text, [10, Globals.SCREEN_HEIGHT - 730])

                # words of encouragement in corresponding color
                font = pygame.font.SysFont('dubai', 20, False, False)
                text = font.render("Oh no! Catch more base pairs!", False, Globals.RED)
                surface.blit(text, [10, Globals.SCREEN_HEIGHT - 680])

            # if health is 60, make text yellow
            elif hp == 60:
                font = pygame.font.SysFont('dubai', 35, False, False)
                text = font.render(health_str + " / 100", True, Globals.YELLOW)
                surface.blit(text, [10, Globals.SCREEN_HEIGHT - 730])

                # words of encouragement in corresponding color
                font = pygame.font.SysFont('dubai', 20, False, False)
                text = font.render("Just a little more, you can do it!", False, Globals.YELLOW)
                surface.blit(text, [10, Globals.SCREEN_HEIGHT - 680])

            # if health is 80 or above, make text green
            elif 80 <= hp <= 100:
                font = pygame.font.SysFont('dubai', 35, False, False)
                text = font.render(health_str + " / 100", True, Globals.GREEN)
                surface.blit(text, [10, Globals.SCREEN_HEIGHT - 730])

                # words of encouragement in corresponding color
                font = pygame.font.SysFont('dubai', 20, False, False)
                text = font.render("Wow! You're doing great!", False, Globals.GREEN)
                surface.blit(text, [10, Globals.SCREEN_HEIGHT - 680])

            # "Score: " rendered text
            font = pygame.font.SysFont('dubai', 35, False, False)
            text = font.render(score_str, True, Globals.BLUE)
            surface.blit(text, [10, Globals.SCREEN_HEIGHT - 645])

            # text to show goal score
            font = pygame.font.SysFont('dubai', 20, False, False)
            text = font.render("Reach a score of 50,000 to win!", False, Globals.BLUE)
            surface.blit(text, [10, Globals.SCREEN_HEIGHT - 600])

        pygame.display.flip()


def main():
    global screen, score

    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()

    pygame.display.set_caption("Ascend the Helix")
    pygame.mouse.set_visible(True)

    # Create an instance of the Game class
    game = Game()

    # add background music
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play(-1)

    # Main game loop
    while game_state == "game":

        # Process events (keystrokes, mouse clicks, etc)
        game.process_events()

        # Update object positions, check for collisions
        game.run_logic()
        if hp == 0:
            game_over_screen()

        if score <= 50000:
            victory_screen()

        # Draw the current frame
        game.display_frame(screen)

        # scrolling_helix(screen)

        # Pause for the next frame
        clock.tick(60)

        pygame.display.flip()


# Call the main function, start up the game
if __name__ == "__main__":
    # calls the menu screen before loop so that menu appears first
    game_intro()
    main()
