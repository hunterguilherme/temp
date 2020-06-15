"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""

from pygame_plays import constants

from pygame_plays.platforms import MovingPlatform
from pygame_plays.Itens.gel import *
from pygame_plays.Feedbacks.feedback_phase1 import *
from pygame_plays.Feedbacks.feedback_phase2 import *
from pygame_plays.Feedbacks.feedback_phase3 import *

from pygame_plays.character_choice import *
from main import Mixer
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None
    # food = None
    # -- Methods

    def __init__(self,character_chosed,phase_chosed):
        try:
            pygame.mixer.init()
            self.has_soundcard = True
        except:
            self.has_soundcard = False

        """ Constructor function """
        self.dead =False
        self.error1 = 0
        self.error2 = 0
        self.error3 = 0
        self.error4 = 0

        self.score = 0

        self.character_chosed = character_chosed
        self.phase_chosed = phase_chosed
        self.mixer = Mixer(self.has_soundcard)

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        if character_chosed == 1:

            sprite_sheet = SpriteSheet("images/personagens/nurse.png")
            image = sprite_sheet.get_image(0, 145, 40, 72.6)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(50, 145, 40, 72.6)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(100, 145, 40, 72.6)
            self.walking_frames_r.append(image)

            # Load all the right facing images, then flip them
            # to face left.
            image = sprite_sheet.get_image(0, 145, 40, 72.6)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)
            image = sprite_sheet.get_image(50, 145, 40, 72.6)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)
            image = sprite_sheet.get_image(100, 145, 40, 72.6)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)

        elif character_chosed == 2:
            sprite_sheet = SpriteSheet("images/personagens/nurse1.png")
            image = sprite_sheet.get_image(0, 145, 40, 72.6)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(50, 145, 40, 72.6)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(100, 145, 40, 72.6)
            self.walking_frames_r.append(image)

            # Load all the right facing images, then flip them
            # to face left.
            image = sprite_sheet.get_image(0, 145, 40, 72.6)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)
            image = sprite_sheet.get_image(50, 145, 40, 72.6)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)
            image = sprite_sheet.get_image(100, 145, 40, 72.6)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)


        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        good_food_hit_list = pygame.sprite.spritecollide(self, self.level.fruit_list, False)
        bad_food_hit_list = pygame.sprite.spritecollide(self, self.level.letter_list, False)
        consonant_hit_list = pygame.sprite.spritecollide(self, self.level.consonant_list, False)
        vogal_hit_list = pygame.sprite.spritecollide(self, self.level.vogal_list, False)
        good_face_hit_list = pygame.sprite.spritecollide(self, self.level.good_face_list, False)
        bad_face_hit_list = pygame.sprite.spritecollide(self, self.level.bad_face_list, False)


        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        for good_food in good_food_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0 or self.change_x < 0 or self.change_y > 0 or self.change_y < 0:
                self.mixer.play_fx("crunch")

                self.level.fruit_list.remove(good_food)
                self.score+=1
                print(self.score)

        for bad_food in bad_food_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0 or self.change_x < 0 or self.change_y > 0 or self.change_y < 0:
                self.mixer.play_fx("error")

                self.level.letter_list.remove(bad_food)
                self.error1+=1

                print(self.score)

        for consonant in consonant_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0 or self.change_x < 0 or self.change_y > 0 or self.change_y < 0:
                self.mixer.play_fx("crunch")

                self.level.consonant_list.remove(consonant)
                self.score+=1

        for vogal in vogal_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0 or self.change_x < 0 or self.change_y > 0 or self.change_y < 0:
                self.mixer.play_fx("error")

                self.level.vogal_list.remove(vogal)
                self.error2+=1


                print(self.score)

        for good_face in good_face_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0 or self.change_x < 0 or self.change_y > 0 or self.change_y < 0:
                self.mixer.play_fx("crunch")

                self.level.good_face_list.remove(good_face)
                self.score += 1

        for bad_face in bad_face_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0 or self.change_x < 0 or self.change_y > 0 or self.change_y < 0:
                self.mixer.play_fx("error")

                self.level.bad_face_list.remove(bad_face)
                self.error3 += 1
        self. error4 += self.error1 + self.error2 + self.error3
        # Move up/down
        self.rect.y += self.change_y

        if self.error1 == 3 and self.error4 != 3:
            self.is_dead()

        elif self.error2 == 3 and self.error4 != 3:
            self.is_dead()

        elif self.error3 == 3 and self.error4 != 3:
            self.is_dead()

        elif self.error3 == 4:
            self.is_dead()

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x


            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

        if self.rect.x == 0 and self.change_x >= 0:
            self.change_x = 0

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants. SCREEN_HEIGHT:
            self.change_y = -9

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -9
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 8
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def is_dead(self):
        if self.error1 == 3 and self.error4 != 3:
            Bad_feedback(self.character_chosed,self.phase_chosed)

        elif self.error2 == 3 and self.error4 != 3:
            Bad_feedback2(self.character_chosed,self.phase_chosed)

        elif self.error3 == 3 and self.error4 != 3:
            Bad_feedback3(self.character_chosed,self.phase_chosed)

        elif self.error4 == 3:
            Bad_feedback3(self.character_chosed,self.phase_chosed)


    def general_feedback(self,phase_choosed):
        if phase_choosed == 1:
            Feedback_end_game(self.character_chosed, self.score, self.error1)

        elif phase_choosed == 2:
            Feedback_end_game2(self.character_chosed, self.score, self.error2)

        elif phase_choosed == 3:
            Feedback_end_game3(self.character_chosed, self.score, self.error3)

        elif phase_choosed == 4:
            Feedback_end_game4(self.character_chosed, self.score, self.error4)