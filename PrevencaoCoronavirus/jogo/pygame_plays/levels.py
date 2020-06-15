import pygame

from pygame_plays import constants
from pygame_plays import platforms
from pygame_plays.Itens import virus1, gel
from pygame_plays.Itens import virus2, mascara
from pygame_plays.Itens import vacina, virus3

from pygame_plays.Feedbacks import feedback_phase1

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    fruit_list = None
    letter_list = None
    consonant_list = None
    vogal_list = None


    good_face_list = None
    bad_face_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.fruit_list = pygame.sprite.Group()
        self.letter_list = pygame.sprite.Group()
        self.consonant_list = pygame.sprite.Group()
        self.vogal_list = pygame.sprite.Group()
        self.good_face_list = pygame.sprite.Group()
        self.bad_face_list = pygame.sprite.Group()

        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.fruit_list.update()
        self.letter_list.update()
        self.consonant_list.update()
        self.vogal_list.update()
        self.good_face_list.update()
        self.bad_face_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 7,0))


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.fruit_list.draw(screen)
        self.letter_list.draw(screen)
        self.consonant_list.draw(screen)
        self.vogal_list.draw(screen)
        self.good_face_list.draw(screen)
        self.bad_face_list.draw(screen)


    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for fruit in self.fruit_list:
            fruit.rect.x += shift_x

        for letter in self.letter_list:
            letter.rect.x += shift_x

        for consonant in self.consonant_list:
            consonant.rect.x += shift_x

        for vogal in self.vogal_list:
            vogal.rect.x += shift_x

        for good_face in self.good_face_list:
            good_face.rect.x += shift_x

        for bad_face in self.bad_face_list:
            bad_face.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("./images/cenarios/cenario1.jpg").convert()

        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.INVISIBLE_BARRIER, 45, 300],
                  [platforms.FOWARD, 45, 530],
                  [platforms.GRASS_LEFT, 450, 500],
                  [platforms.GRASS_MIDDLE, 520, 500],
                  [platforms.GRASS_RIGHT, 590, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],

                  [platforms.THIN_GRASS, 2380, 550],
                  [platforms.THIN_GRASS, 2460, 500],
                  [platforms.THIN_GRASS, 2540, 450],
                  [platforms.THIN_GRASS, 2700, 570],

                  [platforms.EARTH, 2770, 530],
                  [platforms.EARTH, 2770, 470],
                  [platforms.GRASS_MIDDLE, 2770, 410],
                  [platforms.EXIT_SIGN, 3622, 530],

                  ]

        good_food_list = [[vacina.vacina, 515, 420],
                          [vacina.vacina, 600, 150],
                          [vacina.vacina, 850, 500],
                          [vacina.vacina, 870, 50],
                          [vacina.vacina, 2000, 100],
                          [vacina.vacina, 2300, 230],
                          [vacina.vacina, 2560, 530],
                 ]

        bad_food_list = [[virus1.virus1, 800, 100],
                         [virus1.virus2, 900, 500],
                         [virus1.virus1, 1500, 510],
                         [virus1.virus2, 1600, 0],
                         [virus1.virus3, 1800, 510],
                         [virus1.virus1, 2100, 510],
                         [virus1.virus3, 2950, 500],

                  ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for good_foods in good_food_list:
            block = gel.Good_food(good_foods[0])
            block.rect.x = good_foods[1]
            block.rect.y = good_foods[2]
            block.player = self.player
            self.fruit_list.add(block)

        for bad_foods in bad_food_list:
            block = virus1.Bad_food(bad_foods[0])
            block.rect.x = bad_foods[1]
            block.rect.y = bad_foods[2]
            block.player = self.player
            self.letter_list.add(block)
            #
            # block1 = letters.Letter1(letter[0])
            # block1.rect1.x = letter[1]
            # block1.rect1.y = letter[2]
            # block1.player = self.player
            # self.letter_list.add(block1)
        # Add a custom moving platform

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        player.rect.x = 340


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("./images/cenarios/cenario2.jpg").convert()
        # self.life = pygame.image.load("images/lifes/umbrella.png")
        # self.life1 = pygame.image.load("images/lifes/umbrella.png")
        # self.life2 = pygame.image.load("images/lifes/umbrella.png")

        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.INVISIBLE_BARRIER, 45, 200],
                  [platforms.FOWARD, 45, 530],

                  [platforms.SAND_PLATFORM_MIDDLE, 300, 400],
                  [platforms.SAND_PLATFORM_LEFT, 500, 560],
                  [platforms.SAND_PLATFORM_MIDDLE, 567, 520],
                  [platforms.SAND_PLATFORM_RIGHT, 635, 480],
                  [platforms.SAND_LEFT, 800, 400],
                  [platforms.SAND_MIDDLE, 869, 400],
                  [platforms.SAND_RIGHT, 939, 400],
                  [platforms.SAND_LEFT, 1010, 500],
                  [platforms.SAND_MIDDLE, 1069, 500],
                  [platforms.SAND_RIGHT, 1139, 500],

                  [platforms.SAND_LEFT, 1625, 280],
                  [platforms.SAND_MIDDLE, 1690, 280],
                  [platforms.SAND_RIGHT, 1760, 280],

                #stairs
                  [platforms.SAND_PLATFORM_LEFT, 1925, 280],
                  [platforms.SAND_PLATFORM_MIDDLE, 1990, 320],
                  [platforms.SAND_PLATFORM_RIGHT, 2060, 360],
                  [platforms.SAND_PLATFORM_LEFT, 2125, 400],
                  [platforms.SAND_PLATFORM_MIDDLE, 2193, 440],
                  [platforms.SAND_PLATFORM_RIGHT, 2260, 480],
                  [platforms.SAND_PLATFORM_MIDDLE, 2320, 520],
                  [platforms.SAND_PLATFORM_RIGHT, 2375, 560],

                  [platforms.EARTH, 2770, 530],
                  [platforms.EARTH, 2770, 470],
                  [platforms.EARTH, 2770, 410],
                  [platforms.EARTH, 2770, 350],
                  [platforms.SAND_MIDDLE, 2770, 290],
                  [platforms.EXIT_SIGN, 3622, 530],
                  ]


        vowels_list = [[virus2.virus4, 300, 100],
                       [virus2.virus5, 700, 490],
                       [virus2.virus6, 1000, 450],
                       [virus2.virus4, 1250, 500],
                       [virus2.virus6, 800, 50],
                       [virus2.virus5, 2100, 500],
                       [virus2.virus4, 1890, 530],
                       [virus2.virus6, 2700, 50],
                 ]

        consonants_list = [[mascara.mascara, 100, 100],
                           [mascara.mascara, 550, 430],
                           [mascara.mascara, 390, 130],
                           [mascara.mascara, 1200, 300],
                           [mascara.mascara, 1400, 50],

                           [mascara.mascara, 1000, 30],
                           [mascara.mascara, 1650, 350],
                           [mascara.mascara, 1890, 350],
                           [mascara.mascara, 2200, 70],
                           [mascara.mascara, 3290, 310],
                 ]



        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for consonants in consonants_list:
            block = mascara.Consonant(consonants[0])
            block.rect.x = consonants[1]
            block.rect.y = consonants[2]
            block.player = self.player
            self.consonant_list.add(block)

        for vowels in vowels_list:
            block = virus2.Vowel(vowels[0])
            block.rect.x = vowels[1]
            block.rect.y = vowels[2]
            block.player = self.player
            self.vogal_list.add(block)



        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.SAND_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block1 = platforms.MovingPlatform(platforms.SAND_PLATFORM_MIDDLE)
        block1.rect.x = 1300
        block1.rect.y = 200
        block1.boundary_top = 100
        block1.boundary_bottom = 300
        block1.change_y = -1
        block1.player = self.player
        block1.level = self
        self.platform_list.add(block1)

        block3 = platforms.MovingPlatform(platforms.SAND_PLATFORM_MIDDLE)
        block3.rect.x = 2700
        block3.rect.y = 300
        block3.boundary_top = 150
        block3.boundary_bottom = 555
        block3.change_y = -1
        block3.player = self.player
        block3.level = self
        self.platform_list.add(block3)


class Level_03(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("./images/cenarios/cenario3.jpg").convert()

        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.INVISIBLE_BARRIER, 45, 0],
                  [platforms.FOWARD, 45, 530],

                  [platforms.CREEPY_BLOCK, 140, 530],
                  [platforms.CREEPY_BLOCK, 140, 470],
                  [platforms.CREEPY_BLOCK, 140, 410],
                  [platforms.CREEPY_BLOCK, 140, 350],
                  [platforms.CREEPY_BLOCK, 140, 290],
                  [platforms.CREEPY_BLOCK, 140, 230],
                  [platforms.CREEPY_MIDDLE, 140, 170],

                  [platforms.CREEPY_BLOCK, 567, 530],
                  [platforms.CREEPY_BLOCK, 567, 470],
                  [platforms.CREEPY_BLOCK, 567, 410],
                  [platforms.CREEPY_BLOCK, 567, 350],
                  [platforms.CREEPY_BLOCK, 567, 290],
                  [platforms.CREEPY_BLOCK, 567, 230],
                  [platforms.CREEPY_MIDDLE, 567, 170],

                  [platforms.CREEPY_PLATFORM_LEFT, 495, 480],
                  [platforms.CREEPY_PLATFORM_LEFT, 495, 260],


                  [platforms.CREEPY_LEFT, 900, 400],
                  [platforms.CREEPY_MIDDLE, 969, 400],
                  [platforms.CREEPY_RIGHT, 1039, 400],
                  [platforms.CREEPY_LEFT, 1200, 500],
                  [platforms.CREEPY_MIDDLE, 1269, 500],
                  [platforms.CREEPY_RIGHT, 1339, 500],

                  [platforms.CREEPY_PLATFORM_MIDDLE, 1400, 250],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 1620, 300],

                  [platforms.CREEPY_LEFT, 1910, 500],
                  [platforms.CREEPY_MIDDLE, 1979, 500],
                  [platforms.CREEPY_RIGHT, 2049, 500],

                  [platforms.CREEPY_PLATFORM_MIDDLE, 2150, 390],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 1940, 330],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 2340, 290],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 2390, 520],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 2540, 400],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 2610, 360],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 2680, 320],


                  [platforms.CREEPY_BLOCK, 2770, 530],
                  [platforms.CREEPY_BLOCK, 2770, 470],
                  [platforms.CREEPY_BLOCK, 2770, 410],
                  [platforms.CREEPY_BLOCK, 2770, 350],
                  [platforms.CREEPY_MIDDLE, 2770, 290],

                  [platforms.CREEPY_PLATFORM_MIDDLE, 2840, 290],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 2910, 330],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 2980, 370],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 3050, 410],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 3120, 450],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 3190, 490],
                  [platforms.CREEPY_PLATFORM_MIDDLE, 3260, 530],

                  [platforms.CREEPY_BLOCK, 2770, 350],
                  [platforms.CREEPY_MIDDLE, 2770, 290],
                  [platforms.EXIT_SIGN, 3622, 530],
                  ]



        good_face_list = [[vacina.vacina, 1450, 350],
                          [vacina.vacina, 600, 150],
                          [vacina.vacina, 870, 50],
                          [vacina.vacina, 1600, 100],
                          ]

        bad_face_list = [[virus3.virus7, 120, 85],
                         [virus3.virus8, 210, 450],
                         [virus3.virus9, 650, 495],
                         [virus3.virus8, 1010, 340],
                         [virus3.virus9, 1430, 520],

                         [virus3.virus7, 1930, 20],
                         [virus3.virus8, 1630, 1500],

                         [virus3.virus9, 3000, 100],
                         ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


        for good_faces in good_face_list:
            block = vacina.Good_face(good_faces[0])
            block.rect.x = good_faces[1]
            block.rect.y = good_faces[2]
            block.player = self.player
            self.good_face_list.add(block)

        for bad_faces in bad_face_list:
            block = virus3.Bad_face(bad_faces[0])
            block.rect.x = bad_faces[1]
            block.rect.y = bad_faces[2]
            block.player = self.player
            self.bad_face_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.CREEPY_PLATFORM_RIGHT)
        block.rect.x = 208
        block.rect.y = 440
        block.boundary_top = 260
        block.boundary_bottom = 510
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block1 = platforms.MovingPlatform(platforms.CREEPY_PLATFORM_MIDDLE)
        block1.rect.x = 640
        block1.rect.y = 400
        block1.boundary_top = 300
        block1.boundary_bottom = 560
        block1.change_y = -1
        block1.player = self.player
        block1.level = self
        self.platform_list.add(block1)

        block3 = platforms.MovingPlatform(platforms.CREEPY_PLATFORM_MIDDLE)
        block3.rect.x = 1430
        block3.rect.y = 500
        block3.boundary_left = 1410
        block3.boundary_right = 1840
        block3.change_x = 1
        block3.player = self.player
        block3.level = self
        self.platform_list.add(block3)
        player.rect.x = 340
