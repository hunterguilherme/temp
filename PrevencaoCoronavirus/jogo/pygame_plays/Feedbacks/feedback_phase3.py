
import pygame
import os
from pygame_plays import platform_scroller
from pygame_plays import phase_choice, character_choice
import main
SETTINGS = {
    'fullscreen': False,
}

# because I use relative path ..
REALPATH = os.path.dirname( os.path.realpath( __file__ ) )
os.chdir(REALPATH)

class Bad_feedback3:

    width = 1150
    height = 600
    map_ind = 0

    def __init__(self,character_chosed,phase_chosed):

        self.character_chosed = character_chosed
        self.phase_chosed = phase_chosed
        if SETTINGS["fullscreen"]:
            flags = pygame.FULLSCREEN
        else:
            flags = 0

        # pygame init
        pygame.init()

        # init "buffer" and real screen
        self.screen = pygame.Surface([self.width, self.height])
        self.real_screen = pygame.display.set_mode([self.width, self.height], flags, 32)
        pygame.display.set_caption("Prevenção Coronavírus")

        # load game font
        self.font = pygame.font.Font("font/a song for jennifer.ttf", 50)

        # this is the main game menu
        self.menu = Bad_Message(self)

        #~ self.mixer.play_track()
        self.menu.run()

    def run_again(self):
        platform_scroller.main(self.character_chosed,self.phase_chosed)


class Bad_Message:

    index = 0
    mode = "menu"

    def __init__(self, game):

        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0, 0, 0))

        self.game_over = game.font.render("GAME OVER", 1, (255, 255, 255))
        self.game_over_shadow = game.font.render("GAME OVER", 1, (75, 140, 215))

        self.menu_items = [
            game.font.render("Essa não! Você pegou muitos vírus!", 1, (255, 255, 255)),
            game.font.render("Mas não se preocupe você pode tentar de novo! ", 1, (255, 255, 255)),
            game.font.render("      Pressione Enter para começar novamente! ", 1, (255, 255, 255))
        ]

        self.menu_items_shadow = [
            game.font.render("Essa não! Você pegou muitos vírus!", 1, (0, 0, 0)),
            game.font.render("Mas não se preocupe você pode tentar de novo!", 1, (0, 0, 0)),
            game.font.render("      Pressione Enter para começar novamente!", 1, (0, 0, 0))
        ]

    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.game.run_again()

            if running:
                self.draw()

    def draw(self):
        # draw bg
        self.game.screen.blit(self.image, (0, 0))
        self.game.screen.blit(self.surf_ind, (0, 0))
        self.game.screen.blit(self.game_over_shadow, (524, 54))
        self.game.screen.blit(self.game_over, (520, 50))

        if self.mode == "menu":

            for ind in range(3):
                self.game.screen.blit(self.menu_items_shadow[ind], (104, 204 + ind * 60))
                self.game.screen.blit(self.menu_items[ind], (100, 200 + ind * 60))


        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()



class Feedback_end_game3:

    width = 1150
    height = 600
    map_ind = 0
    state = ""

    def __init__(self,character_chosed, score, error):
        self.character_chosed = character_chosed
        if SETTINGS["fullscreen"]:
            flags = pygame.FULLSCREEN
        else:
            flags = 0

        # pygame init
        pygame.init()



        # init "buffer" and real screen
        self.screen = pygame.Surface([self.width, self.height])
        self.real_screen = pygame.display.set_mode([self.width, self.height], flags, 32)
        pygame.display.set_caption("Prevenção Coronavirus")

        # load game font
        self.font = pygame.font.Font("font/a song for jennifer.ttf", 60)
        self.font1 = pygame.font.Font("font/a song for jennifer.ttf", 40)
        self.font2 = pygame.font.Font("font/a song for jennifer.ttf", 50)


        # this is the main game menu


        self.message = Phase3_end_perfect(self, score, error)


        #~ self.mixer.play_track()
        self.message.run()

    def init_game(self):
        # init game/player value for new game
        self.state = "play"

    def run_again_menu(self):

        phase_choice.Choose_phase(self.character_chosed)
        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)


class Phase3_end_perfect:

    index = 0
    mode = "menu"

    def __init__(self, game, score,error):

        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0, 0, 0))

        self.congratulations = game.font.render("Você venceu!", 1, (255, 255, 255))
        self.congratulations_shadow = game.font.render("Você venceu!", 1, (75, 140, 215))


        self.menu_items = [
                game.font1.render("Potes de Alcóol em gel: %s"%(score), 1, (255, 255, 255)),
                game.font1.render("Vírus: %s"%(error), 1, (255, 255, 255)),
                game.font1.render("Continue combatendo os vírus!", 1, (255, 255, 255)),
                game.font1.render("Pressione Enter para escolher outro cenário.", 1, (255, 255, 255))
                ]

        self.menu_items_shadow = [
                game.font1.render("Potes de Alcóol em gel: %s"%(score), 1, (0, 0, 0)),
                game.font1.render("Vírus: %s"%(error), 1, (0, 0, 0)),
                game.font1.render("Continue combatendo os vírus", 1, (0, 0, 0)),
                game.font1.render("Pressione Enter para escolher outro cenário.", 1, (0, 0, 0))
                ]


    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.mode == "menu":
                            running = False

                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.game.run_again_menu()

            if running:
                self.draw()

    def draw(self):
        # draw bg
        self.game.screen.blit(self.image, (0, 0))
        self.game.screen.blit(self.surf_ind, (0, 0))
        self.game.screen.blit(self.congratulations_shadow, (524, 54))
        self.game.screen.blit(self.congratulations, (520, 50))

        if self.mode == "menu":

            for ind in range(3):
                self.game.screen.blit(self.menu_items_shadow[ind], (84, 204 + ind * 60))
                self.game.screen.blit(self.menu_items[ind], (80, 200 + ind * 60))


        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()