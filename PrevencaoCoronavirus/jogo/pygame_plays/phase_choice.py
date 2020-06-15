
import pygame
import os

from pygame_plays import platform_scroller,phases_introductions
from main import Mixer

SETTINGS = {
    'fullscreen': False,
}

# because I use relative path ..
REALPATH = os.path.dirname( os.path.realpath( __file__ ) )
os.chdir(REALPATH)

class Choose_phase:
    phase_chosed = 0
    width = 1150
    height = 600
    map_ind = 0
    state = ""
    enemy_timer = 0
    enemy_next_timer = 0
    gameover_delay = 2000
    gameover_timer = 0

    def __init__(self,character_chosed):

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
        pygame.display.set_caption("Prevenção Coronavírus")

        # load game font
        self.font = pygame.font.Font("font/a song for jennifer.ttf", 95)


        # create mixer for fx/music

        # this is the main game menu
        self.menu = Menu_phase(self)

        #~ self.mixer.play_track()
        self.menu.run()

    def init_game(self):
        # init game/player value for new game
        self.state = "play"

    def run(self):
        # main game loop ( need a complete rewrite .. really )
        phases_introductions.Introductions(self.character_chosed, self.phase_chosed)
        # platform_scroller.main()

        self.init_game()
        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.state == "pause":
                            running = False
                        elif self.state == "play":
                            self.state = "pause"
                            self.draw()
                        elif self.state == "waiting":
                            self.state = "menu"
                            running = False
                    elif self.state == "waiting":
                        self.init_game()
                    elif self.state == "pause":
                        self.state = "play"

class Menu_phase:
    y = 0
    index = 0
    mode = "menu"
    character_chosed = 0

    def __init__(self, game):

        self.game = game
        self.has_soundcard = True
        self.mixer = Mixer(self.has_soundcard)

        self.image = pygame.image.load('images/cenarios/menu.jpg')
        self.phase1 = pygame.image.load('images/cenarios/background_choices/fase11.jpg')
        self.phase2 = pygame.image.load('images/cenarios/background_choices/fase22.jpg')
        self.phase3 = pygame.image.load('images/cenarios/background_choices/fase33.jpg')

        self.virus = pygame.image.load('images/cenarios/virus.png')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0, 0, 0))

        self.game_name = game.font.render("Escolha um cenário", 1, (255, 255, 255))
        self.game_name_shadow = game.font.render("Escolha um cenário", 1, (36, 135, 249))

        self.character_list = [self.phase1, self.phase2, self.phase3]

        # self.menu_items_shadow = [
        #     game.font.render("", 1, (0, 0, 0)),
        #     game.font.render("Aperte ENTER para começar escolher o personagem!", 1, (0, 0, 0))
        #     ]

    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    self.mixer.play_fx("selection")
                    if event.key == pygame.K_ESCAPE:
                        if self.mode == "menu":
                            running = False
                        else:
                            self.mode = "menu"
                            self.index = 0
                    elif event.key == pygame.K_UP:
                        if self.y > 0:
                            self.y -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.y < 1 and self.index < 1:
                            self.y += 1
                    elif event.key == pygame.K_LEFT:
                        if self.index > 0:
                            self.index -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.index < 1 and self.y < 1:
                            self.index += 1

                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                        # quit
                        if self.mode == "menu" and self.index == 3:
                            running = False
                        elif self.mode == "menu" and self.index == 0 and self.y == 0:
                            Choose_phase.phase_chosed = 1
                            self.game.run()

                        elif self.mode == "menu" and self.index == 1 and self.y == 0:
                            Choose_phase.phase_chosed = 2
                            self.game.run()

                        elif self.mode == "menu" and self.index == 0 and self.y == 1:
                            Choose_phase.phase_chosed = 3
                            self.game.run()

            if running:
                self.draw()

    def draw(self):
        # draw bg


        self.game.screen.blit(self.image, (0, 0))
        self.game.screen.blit(self.surf_ind, (0, 0))
        self.game.screen.blit(self.phase1, (50, 200))
        self.game.screen.blit(self.phase2, (600, 200))
        self.game.screen.blit(self.phase3, (300, 400))

        # draw game name
        self.game.screen.blit(self.game_name_shadow, (284, 54))
        self.game.screen.blit(self.game_name, (280, 50))

        if self.mode == "menu":
            self.game.screen.blit(self.virus, (self.index * 390 + 190, self.y * 200 + 150))

        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()
