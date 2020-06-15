import pygame
import os
from pygame_plays import menu,character_choice
import main


SETTINGS = {
    'fullscreen': False,
}



REALPATH = os.path.dirname( os.path.realpath( __file__ ) )
os.chdir(REALPATH)

class Instructions:

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
        self.font = pygame.font.Font("font/a song for jennifer.ttf", 55)
        self.font1 = pygame.font.Font("font/a song for jennifer.ttf", 100)


        # this is the main game menu
        self.menu_credits = Instructions_Message(self)

        #~ self.mixer.play_track()
        self.menu_credits.run()

    def back_to_menu(self, ligado):
        # pass
        main.Game(ligado)
        # menu.Menu()


class Instructions_Message:

    index = 0
    mode = "menu"

    def __init__(self, game):

        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0, 0, 0))

        self.game_instructions = game.font1.render("Opções", 1, (255, 255, 255))
        self.game_instructions_shadow = game.font1.render("Opções", 1, (36, 135, 249))

        self.menu_items = [
            game.font.render("Pressione 'd' para desligar o música", 1, (255, 255, 255)),
            game.font.render("Pressione 'l' para ligar a música ", 1, (255, 255, 255)),
            game.font.render("          Pressione a tecla V para voltar ao menu", 1, (255, 255, 255)),
            ]

        self.menu_items_shadow = [
            game.font.render("Pressione 'd' para desligar o música", 1, (0, 0, 0)),
            game.font.render("Pressione 'l' para ligar a música ", 1, (0, 0, 0)),
            game.font.render("          Pressione a tecla V para voltar ao menu", 1, (0, 0, 0)),
            ]

    def run(self):

        clock = pygame.time.Clock()
        running = True
        self.ligado = False
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.ligado = False
                        pygame.mixer.music.pause()

                    if event.key == pygame.K_l:
                        self.ligado =True
                        pygame.mixer.music.load("sfx\som.mp3")
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(1)



                    elif event.key == pygame.K_v:
                        self.game.back_to_menu(self.ligado)

            if running:
                self.draw()

    def draw(self):
        # draw bg
        self.game.screen.blit(self.image, (0, 0))
        self.game.screen.blit(self.surf_ind, (0, 0))

        self.game.screen.blit(self.game_instructions_shadow, (424, 54))
        self.game.screen.blit(self.game_instructions, (420, 50))

        if self.mode == "menu":
            pass

            for ind in range(len(self.menu_items)):
                self.game.screen.blit(self.menu_items_shadow[ind], (57, 204 + ind * 70))
                self.game.screen.blit(self.menu_items[ind], (50, 200 + ind * 70))


        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()

