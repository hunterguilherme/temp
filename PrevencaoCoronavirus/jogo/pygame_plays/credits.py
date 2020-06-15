import pygame
import os
from pygame_plays import menu,character_choice
import main


SETTINGS = {
    'fullscreen': False,
}

REALPATH = os.path.dirname( os.path.realpath( __file__ ) )
os.chdir(REALPATH)

class Credits:

    width = 1150
    height = 600

    def __init__(self):

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



        # this is the main game menu
        self.menu_credits = Credits_Message(self)

        #~ self.mixer.play_track()
        self.menu_credits.run()

    def back_to_menu(self,ligado):
        # pass

        main.Game(ligado)
        # menu.Menu()


class Credits_Message:

    index = 0
    mode = "menu"

    def __init__(self, game):


        self.font = pygame.font.Font("font/a song for jennifer.ttf", 100)
        self.font2 = pygame.font.Font("font/a song for jennifer.ttf", 55)

        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0,0,0))


        self.game_over = self.font.render("Criadores", 1, (255,255,255))
        self.game_over_shadow = self.font.render("Criadores", 1, (36, 135, 249))

        self.menu_items = [
            self.font2.render("NOMES                                        TIA", 1, (255, 255, 255)),
            self.font2.render("Gabriel Henrique dos Santos      3181642-8", 1, (255, 255, 255)),
            self.font2.render("Leonardo Cozzi Foleto               3182582-6", 1, (255, 255, 255)),
            self.font2.render("Sandra Pereira Costa                 3174751-5", 1, (255, 255, 255)),
            self.font2.render("         Pressione a tecla V para voltar", 1, (255, 255, 255))
            ]

        self.menu_items_shadow = [
            self.font2.render("NOMES                                        TIA", 1, (36, 135, 249)),
            self.font2.render("Gabriel Henrique dos Santos      3181642-8", 1, (0, 0, 0)),
            self.font2.render("Leonardo Cozzi Foleto               3182582-6", 1, (0, 0, 0)),
            self.font2.render("Sandra Pereira Costa                 3174751-5", 1, (0, 0, 0)),
            self.font2.render("         Pressione a tecla V para voltar", 1, (0, 0, 0))
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
                    if event.key == pygame.K_d:
                        self.ligado = False

                    elif event.key == pygame.K_v:
                        self.game.back_to_menu(0)

            if running:
                self.draw()

    def draw(self):
        # draw bg
        self.game.screen.blit(self.image, (0, 0))

        self.game.screen.blit(self.surf_ind, (0, 0))

        self.game.screen.blit(self.game_over_shadow, (345, 54))
        self.game.screen.blit(self.game_over, (354, 50))

        if self.mode == "menu":

            for ind in range(len(self.menu_items)):
                self.game.screen.blit(self.menu_items_shadow[ind], (54, 204 + ind * 80))
                self.game.screen.blit(self.menu_items[ind], (50, 200 + ind * 80))


        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()

