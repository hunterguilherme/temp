
import pygame
import os

import pygame_plays.menu as menu
from pygame_plays import character_choice

SETTINGS = {
    'music_volume': 50,
    'fx_volume': 90,
    'fullscreen': False,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'jump': pygame.K_SPACE
}


# because I use relative path ..
REALPATH = os.path.dirname( os.path.realpath( __file__ ) )
os.chdir(REALPATH)


class Mixer:

    def __init__(self, has_soundcard=False, volume = False):

        self.has_soundcard = has_soundcard
        pygame.mixer.music.load("sfx\som.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)


        self.set_music_volume(volume)

        if has_soundcard:
            self.fx = {
                "jump": pygame.mixer.Sound("./sfx/jump.wav"),
                "crunch": pygame.mixer.Sound("./sfx/crunch.wav"),
                "flip": pygame.mixer.Sound("./sfx/flip.wav"),
                "no": pygame.mixer.Sound("./sfx/no.wav"),
                "error": pygame.mixer.Sound("./sfx/error.wav"),
                "selection": pygame.mixer.Sound("./sfx/selection.wav"),

            }

        #~ self.track = pygame.mixer.Sound("./sfx/track_1.wav")

    def play_fx(self, name):
        if self.has_soundcard:
            self.fx[name].set_volume(SETTINGS["fx_volume"]/100.0)
            self.fx[name].play()

    def play_track(self):
        if self.has_soundcard:
            self.track.set_volume(SETTINGS["music_volume"]/100.0)
            self.track.play()

    def set_music_volume(self, ligado):
        self.volume = 1
        self.ligado = ligado

        if self.ligado:
            self.volume = 1
        else:
            self.volume = 0
        return self.volume
    def set_sound_volume(self, volume):

        return volume

class Game:

    width = 1150
    height = 600
    map_ind = 0
    state = ""
    enemy_timer = 0
    enemy_next_timer = 0
    gameover_delay = 2000
    gameover_timer = 0

    def __init__(self, ligado):
        if SETTINGS["fullscreen"]:
            flags = pygame.FULLSCREEN
        else:
            flags = 0
        # self.volume = True
        self.ligado = ligado
        #
        # if self.ligado:
        #     self.volume = 1
        # else:
        #     self.volume = 0



        # pygame init
        pygame.init()

        try:
            pygame.mixer.init()
            self.has_soundcard = True
        except:
            self.has_soundcard = False
        pygame.mouse.set_visible(0)

        # init "buffer" and real screen
        self.screen = pygame.Surface([self.width, self.height])
        self.real_screen = pygame.display.set_mode([self.width, self.height], flags, 32)
        pygame.display.set_caption("Prevenção Coronavírus")

        # load game font
        self.font = pygame.font.Font("font/a song for jennifer.ttf", 70)


        # create mixer for fx/music
        self.mixer = Mixer(self.has_soundcard, self.ligado)

        # this is the main game menu
        self.menu = menu.Menu(self)


        #~ self.mixer.play_track()
        self.menu.run()

    def init_game(self):
        # init game/player value for new game
        self.state = "play"

    def run(self):

        character_choice.Choose_character(self)
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



if __name__ == "__main__":

    game = Game(False)
    pygame.quit()
