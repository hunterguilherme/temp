import pygame
from pygame_plays import credits,instructions, guia

class Menu:

    index = 0
    mode = "menu"

    def __init__(self, game):
        self.game = game

        self.image = pygame.image.load('images/cenarios/menu.jpg')
        self.virus = pygame.image.load('images/cenarios/virus.png')

        # self.volume = game.


        self.surf_ind = pygame.Surface([game.width, game.height])
        self.surf_ind.set_alpha(70)
        self.surf_ind.fill((0,0,0))

        self.font = pygame.font.Font("font/a song for jennifer.ttf", 95)

        self.game_name = self.font.render("Prevenção Coronavírus", 1, (255,255,255))
        self.game_name_shadow = self.font.render("Prevenção Coronavírus", 1, (36, 135, 249))

        self.menu_items = [
            game.font.render("Jogar", 1, (255, 255, 255)),
            game.font.render("Guia", 1, (255, 255, 255)),
            game.font.render("Opções", 1, (255, 255, 255)),
            game.font.render("Criadores", 1, (255, 255, 255))
            ]

        self.menu_items_shadow = [
            game.font.render("Jogar", 1, (0, 0, 0)),
            game.font.render("Guia", 1, (0, 0, 0)),
            game.font.render("Opções", 1, (0, 0, 0)),
            game.font.render("Criadores", 1, (0, 0, 0))
            ]

    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    self.game.mixer.play_fx("selection")

                    if event.key == pygame.K_ESCAPE:
                        if self.mode == "menu":
                            exit()
                        else:
                            self.mode = "menu"
                            self.index = 0
                    elif event.key == pygame.K_UP:
                        if self.index > 0:
                            self.index -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.index < 3:
                            self.index += 1
                    elif event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                        # quit
                        if self.mode == "menu" and self.index == 4:
                            running = False
                        # play -> select map
                        elif self.mode == "menu" and self.index == 0:
                            #~ self.mode = "map"
                            self.game.run()
                        elif self.mode == "menu" and self.index == 1:
                            #~ self.mode = "map"
                            guia.Guia()
                        # options
                        elif self.mode == "menu" and self.index == 2:
                            instructions.Instructions()

                        elif self.mode == "menu" and self.index == 3:
                            credits.Credits()


            if running:
                self.draw()

    def draw(self):
        # draw bg

        self.game.screen.blit(self.image, (0, 0))
        self.game.screen.blit(self.surf_ind, (0, 0))
        # draw game name
        self.game.screen.blit(self.game_name_shadow, (145, 54))
        self.game.screen.blit(self.game_name, (154, 50))

        if self.mode == "menu":
            self.game.screen.blit(self.virus, (316, self.index * 97 + 160))

            for ind in range(4):
                self.game.screen.blit(self.menu_items_shadow[ind], (454, 184 + ind * 100))
                self.game.screen.blit(self.menu_items[ind], (450, 180 + ind * 100))
        elif self.mode == "map":
            pass
        elif self.mode == "options":
            pass

        self.game.real_screen.blit(self.game.screen, (0, 0))
        pygame.display.flip()
