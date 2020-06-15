"""
Module for managing platforms.
"""
import pygame

from pygame_plays.spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

#PHASE1
GRASS_LEFT            = (576, 720, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)
THIN_GRASS            = (575, 432, 70, 70)



#PHASE2
SAND_LEFT            = (360, 720, 70, 70)
SAND_RIGHT           = (360, 576, 70, 70)
SAND_MIDDLE          = (287, 576, 70, 70)
SAND_PLATFORM_LEFT   = (722, 720, 70, 40)
SAND_PLATFORM_MIDDLE = (720, 290, 70, 40)
SAND_PLATFORM_RIGHT  = (722, 576, 70, 40)

#PHASE3
ICE_LEFT = (287, 0, 80, 70)
ICE_MIDDLE = (144, 792, 70, 70)
ICE_RIGHT = (217, 792, 70, 70)

ICE_PLATFORM_LEFT   = (215, 430, 70, 40)
ICE_PLATFORM_MIDDLE = (218, 505, 70, 40)
ICE_PLATFORM_RIGHT  = (218, 435, 70, 40)
ICE_BLOCK  = (720, 865, 70, 70)
ICE_SMALL_PLATAFORM  = (218, 505, 40, 40)

#PHASE4
CREEPY_LEFT = (143, 430, 80, 70)
CREEPY_MIDDLE = (71, 430, 70, 70)
CREEPY_RIGHT = (145, 286, 70, 70)


CREEPY_PLATFORM_LEFT   = (140, 70, 70, 40)
CREEPY_PLATFORM_MIDDLE = (145, 0 , 70, 40)
CREEPY_PLATFORM_RIGHT  = (70, 865, 70, 40)
CREEPY_BLOCK  = (143, 575, 70, 70)
# SAND_LEFT            = (360, 720, 70, 70)
# SAND_RIGHT           = (360, 576, 70, 70)
# SAND_MIDDLE          = (287, 576, 70, 70)


#ALL_PHASES
FOWARD                = (287, 220, 70, 70)
EXIT_SIGN             = (287, 360, 70, 70)
INVISIBLE_BARRIER     = (1000, 865, 70, 300)
EARTH = (575, 865, 70, 70)
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("images/plataforms/tiles_spritesheet.png ")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3],
                                            )

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
