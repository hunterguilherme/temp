
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

class Introductions:

    width = 1150
    height = 600
    map_ind = 0

    def __init__(self,character_chosed, phase_chosed):

        self.character_chosed = character_chosed
        self.phase_chosed = phase_chosed
        self.character_name = ""

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
        self.font = pygame.font.Font("font/a song for jennifer.ttf", 39)
        self.font1 = pygame.font.Font("font/a song for jennifer.ttf", 85)


        # this is the main game menu


        if self.character_chosed == 1:
            self.character_name = "Mônica"

        elif self.character_chosed == 2:
            self.character_name = "Cascão"

        if self.phase_chosed == 1:
            self.menu = Introduction_phase1(self,self.character_name)
        elif self.phase_chosed == 2:
            self.menu = Introduction_phase2(self,self.character_name)
        elif self.phase_chosed == 3:
            self.menu = Introduction_phase3(self,self.character_name)

        self.menu.run()

    def run_again(self):
        platform_scroller.main(self.character_chosed,self.phase_chosed)


class Introduction_phase1:

    index = 0
    mode = "menu"

    def __init__(self, game,character_name):

        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0,0,0))

        self.phase_title = game.font1.render("Cenário 1", 1, (255, 255, 255))
        self.phase_title_shadow = game.font1.render("Cenário 1", 1, (36, 135, 249))



        self.menu_items = [
            game.font.render("Cuidados ao Tossir ou espirrar. Você deve cobrir a boca e o nariz ", 1, (255, 255, 255)),
            game.font.render("Por quê? Desse modo, você não deixa que gotículas caiam no ar e", 1, (255, 255, 255)),
            game.font.render("contaminem outra pessoa. Lembre-se tambem de sempre lavar as", 1, (255, 255, 255)),
            game.font.render("mãos com alcool em gel. Vamos praticar?", 1,(255, 255, 255)),
            game.font.render("Colha os potes de alcool em gel e desvie dos virus", 1, (255, 255, 255)),
            game.font.render("", 1, (255, 255, 255)),
            game.font.render("                          Pressione Enter para iniciar o jogo. ", 1, (255, 255, 255))

        ]

        self.menu_items_shadow = [
            game.font.render("Cuidados ao Tossir ou espirrar. Você deve cobrir a boca e o nariz ",1, (0, 0, 0)),
            game.font.render("Por quê? Desse modo, você não deixa que gotículas caiam no ar e", 1, (0, 0, 0)),
            game.font.render("contaminem outra pessoa. Lembre-se tambem de sempre lavar as", 1, (0, 0, 0)),
            game.font.render("mãos com alcool em gel. Vamos praticar? ", 1, (0, 0, 0)),
            game.font.render("Colha os potes de alcool em gel e desvie dos virus", 1, (0, 0, 0)),
            game.font.render("", 1, (255, 255, 255)),
            game.font.render("                          Pressione Enter para iniciar o jogo. ", 1, (0, 0, 0))
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
        self.game.screen.blit(self.phase_title_shadow, (374, 54))
        self.game.screen.blit(self.phase_title, (370, 50))

        if self.mode == "menu":

            for ind in range(len(self.menu_items)):
                self.game.screen.blit(self.menu_items_shadow[ind], (57, 204 + ind * 45))
                self.game.screen.blit(self.menu_items[ind], (50, 200 + ind * 45))

        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()


class Introduction_phase2:

    index = 0
    mode = "menu"

    def __init__(self, game,character_name):

        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0, 0, 0))

        self.game_over = game.font1.render("Cenário 2", 1, (255, 255, 255))
        self.game_over_shadow = game.font1.render("Cenário 2", 1, (36, 135, 249))

        self.menu_items = [
            game.font.render("Evite aglomerações e mantenhas os ambientes limpos e bem venti- ", 1, (255, 255, 255)),
            game.font.render("lados. Por quê? A propagação do vírus é mais fácil em ambientes", 1, (255, 255, 255)),
            game.font.render("fechados com grande número de pessoas. Além disso use máscaras" , 1, (255, 255, 255)),
            game.font.render("sempre que sair na rua. Que tal praticar?", 1,(255, 255, 255)),
            game.font.render("Nesse cenário, você deve colher máscaras e desviar dos vírus.", 1,(255, 255, 255)),
            game.font.render("", 1,(255, 255, 255)),
            game.font.render("                          Pressione Enter para iniciar o jogo. ", 1, (255, 255, 255))

        ]

        self.menu_items_shadow = [
            game.font.render("Evite aglomerações e mantenhas os ambientes limpos e bem venti-",1, (0, 0, 0)),
            game.font.render("lados. Por quê? A propagação do vírus é mais fácil em ambientes", 1, (0, 0, 0)),
            game.font.render("fechados com grande número de pessoas. Além disso use máscaras" , 1, (0, 0, 0)),
            game.font.render("sempre que sair na rua. Que tal praticar? ", 1, (0, 0, 0)),
            game.font.render("Nesse cenário, você deve colher máscaras e desviar dos vírus.", 1, (0, 0, 0)),
            game.font.render("", 1, (0, 0, 0)),
            game.font.render("                          Pressione Enter para iniciar o jogo. ", 1, (0, 0, 0))
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
        self.game.screen.blit(self.game_over_shadow, (374, 54))
        self.game.screen.blit(self.game_over, (370, 50))

        if self.mode == "menu":

            for ind in range(len(self.menu_items)):
                self.game.screen.blit(self.menu_items_shadow[ind], (57, 204 + ind * 45))
                self.game.screen.blit(self.menu_items[ind], (50, 200 + ind * 45))

        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()

class Introduction_phase3:

    index = 0
    mode = "menu"

    def __init__(self, game,character_name):

        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')

        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0, 0, 0))

        self.game_over = game.font1.render("Cenário 3", 1, (255, 255, 255))
        self.game_over_shadow = game.font1.render("Cenário 3", 1, (36, 135, 249))

        self.menu_items = [
            game.font.render("Em breve teremos uma cura! Mas enquanto isso não acontece", 1, (255, 255, 255)),
            game.font.render("fique em casa, principalmente se você está com sintomas", 1, (255, 255, 255)),
            game.font.render("de gripe, por 14 dias, como orienta o Ministério da Saúde.", 1, (255, 255, 255)),
            game.font.render("Por quê? Assim você evita a superlotação dos hospitais e  ", 1, (255, 255, 255)),
            game.font.render("ajuda no combate ao Coronavírus. ", 1,(255, 255, 255)),
            game.font.render("Nesse ultimo cenário, você deve tentar achar a cura. Boa sorte! ", 1, (255, 255, 255)),
            game.font.render("", 1, (255, 255, 255)),
            game.font.render("                          Pressione Enter para iniciar o jogo. ", 1, (255, 255, 255))

        ]

        self.menu_items_shadow = [
            game.font.render("Em breve teremos uma cura! Mas enquanto isso não acontece",1, (0, 0, 0)),
            game.font.render("fique em casa, principalmente se você está com sintomas", 1, (0, 0, 0)),
            game.font.render("de gripe, por 14 dias, como orienta o Ministério da Saúde.", 1, (0, 0, 0)),
            game.font.render("Por quê? Assim você evita a superlotação dos hospitais e", 1, (0, 0, 0)),
            game.font.render("ajuda no combate ao Coronavírus.", 1, (0, 0, 0)),
            game.font.render("Nesse ultimo cenário, você deve tentar achar a cura. Boa sorte!", 1, (0, 0, 0)),
            game.font.render("", 1, (255, 255, 255)),
            game.font.render("                          Pressione Enter para iniciar o jogo. ", 1, (0, 0, 0))
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
        self.game.screen.blit(self.game_over_shadow, (374, 54))
        self.game.screen.blit(self.game_over, (370, 50))

        if self.mode == "menu":

            for ind in range(len(self.menu_items)):
                self.game.screen.blit(self.menu_items_shadow[ind], (57, 204 + ind * 45))
                self.game.screen.blit(self.menu_items[ind], (50, 200 + ind * 45))

        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()

