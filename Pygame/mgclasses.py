"""Docstring"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*
#pylint: disable=no-member


import random # Importation of random's library to display objects randomly on the maze
import logging as lg # Importation of logging's library to debug the functions
import pygame # Importation of pygame's library to create a graphic game

from pygame.locals import *
from mggame import *

lg.basicConfig(level=lg.DEBUG) # Congiguration of logging's library

pygame.init() # initializing pygame


#####################
####### MAZE ########
#####################

class Maze:
    """ CLASS MAZE IS CREATING AND DISPLAYING
    THE MAZE IN WICH THE CHARACTER (MACGYVER) WILL MOVE """

    level_structure = []

    def __init__(self):
        """ constructor of class Maze """
        self.level = 'level.txt'
        # calling file level.txt, it contains the structure of the maze
        self.level_structure = 0
        # create list of the structure's level


    def creating_level(self):
        """ method to create the structure of the level """
        with open(self.level, "r") as level:
            create_structure_level = []
            # create a list of the file level.txt
            for line in level:
            # read each line in level.txt
                line_of_level = []
                # create a list for each line (y)
                for sprite in line:
                # read each sprite in lines of level.txt
                    if sprite != "\n":
                    # ignore "\n"
                        line_of_level.append(sprite)
                        # add each sprite to line
                create_structure_level.append(line_of_level)
                # add each line (y) to create_structure_level
            self.level_structure = create_structure_level
            # save the structure in create_structure_level

            #  LEVEL_STRUCTURE IS AN ARRAY
            # y represents lines
            # x represents columns

    def displaying_level(self, SCREEN):
        """ method to display the level on screen """
        walls = pygame.image.load('images/walls.png').convert_alpha()
        departure = pygame.image.load('images/depart.png').convert_alpha()
        murdoc = pygame.image.load('images/murdoc.png').convert_alpha()
        floor = pygame.image.load('images/floor.png').convert_alpha()


        line_of_level_default = 0 # default position of a line
        for line in self.level_structure: # read each line in level_structure
            column_of_level_default = 0 # default position of a case
            for sprite in line: # read each sprite in line_of_level_default
                sprite_position_x = column_of_level_default * SIZE_OF_SPRITE
                # default position in pixel on x
                sprite_position_y = line_of_level_default * SIZE_OF_SPRITE
                # default position in pixel on y
                # add corresponding image to each sprite
                #depending of it's type (wall, departure, arrival)
                if sprite == "m": # if sprite is 'm' in level.txt
                    SCREEN.blit(walls, (sprite_position_x, sprite_position_y))
                    # display sprite_wall in the corresponding position_x and position_y
                elif sprite == "d": # if sprite is 'd' in level.txt
                    SCREEN.blit(departure, (sprite_position_x, sprite_position_y))
                    # display sprite_departure in the corresponding position_x and position_y
                elif sprite == "a": # if sprite is 'a' in level.txt
                    SCREEN.blit(murdoc, (sprite_position_x, sprite_position_y))
                    # display sprite_arrival in the corresponding position_x and position_y
                elif sprite == "0":
                    SCREEN.blit(floor, ((sprite_position_x, sprite_position_y)))
                column_of_level_default += 1 # add it to column_of_level_default
            line_of_level_default += 1# add it to line_of_level_default

#####################
##### MACGYVER ######
#####################

class Macgyver:
    """CLASS MACGYVER : MAIN CHARACTER OF THE GAME.
    THIS CLASS CREATE THE CHARACTER AND ALLOW HIM TO MOVE IN THE MAZE """

    def __init__(self, character_place):
        """ constructor of class Macgyver """
        self.character = pygame.image.load("images/macgyver.png").convert_alpha()
        self.position_character_in_sprite_x = 0 # Character's position in sprite x default
        self.position_character_in_sprite_y = 0 # Character's position in sprite y default
        self.position_character_in_pixel_x = 0 # Character's position in pixel y default
        self.position_character_in_pixel_y = 0 # Character's position in pixel y default
        self.character_direction = self.character # Macgyver looks like this
        self.character_place = character_place # where is Macgyver

    def make_move_macgyver(self, character_direction):
        """ method to make the character move in the Maze """

        if character_direction == 'right': # if going right
            if self.position_character_in_sprite_y < (NUMBER_OF_SPRITE - 1):
            # Character doesn't get out of the window's game
                if self.character_place.level_structure[
                        self.position_character_in_sprite_x][
                            self.position_character_in_sprite_y+ 1] != "m":
                            # checking the destition is empty (no wall)
                            #by reading level structure
                    self.position_character_in_sprite_y += 1
                    # Make move the character by one sprite
                    # change his position_character_in_pixel_y and position_character_in_sprite_x
                    self.position_character_in_pixel_y = self.position_character_in_sprite_y * 30
            lg.debug('Character is going to the right')

        if character_direction == 'down': # if going down
            if self.position_character_in_sprite_x < (NUMBER_OF_SPRITE - 1):
            # Character doesn't get out of the window's game
                if self.character_place.level_structure[
                        self.position_character_in_sprite_x+1][
                            self.position_character_in_sprite_y] != "m":
                            # checking the destination is empty (no wall)
                            #by reading level structure's sprites
                    self.position_character_in_sprite_x += 1
                    # Make move the character by one sprite on x, for right +1 on x
                    self.position_character_in_pixel_x = self.position_character_in_sprite_x * 30
                    # change his position_character_in_pixel_x
            lg.debug('Character is going down')

        if character_direction == 'left': # if going left
            if self.position_character_in_sprite_y > 0:
            # Character doesn't get out of the window's game
                if self.character_place.level_structure[
                        self.position_character_in_sprite_x][
                            self.position_character_in_sprite_y-1] != "m":
                            # checking the destition is empty (no wall)
                            #by reading level structure
                    self.position_character_in_sprite_y -= 1
                    # Make move the character by one sprite -1 on y
                    self.position_character_in_pixel_y = self.position_character_in_sprite_y * 30
                    #change his position_character_in_pixel_y
            lg.debug('Character is going to the left')

        if character_direction == 'up': #if going up
            if self.position_character_in_sprite_x > 0:
            # Character doesn't get out of the window's game
                if self.character_place.level_structure[
                        self.position_character_in_sprite_x-1][
                            self.position_character_in_sprite_y] != "m":
                            # checking the destition is empty (no wall)
                            #by reading level structure
                    self.position_character_in_sprite_x -= 1
                    # Make move the character by one sprite , for left -1 on x
                    self.position_character_in_pixel_x = self.position_character_in_sprite_x * 30
                    #change his position_character_in_pixel_x
            lg.debug('Character is going up')

#####################
###### TO PICK ######
#####################


class Pickittowin:
    """ OBJECTS TO PICK TO MAKE FALL ASLEEP MURDOC THE GUARDIAN
    AND WIN THE GAME ! """

    level_structure = []

    def __init__(self):
        """ constructor of class Pick_it_to_win """
        self.level = 'level.txt' # calling level.txt, it contains the structure of the maze
        self.level_structure = 0 # create list of the structure's level
        self.x_potion = 0 # init x position for potion
        self.x_coffre = 0 # init x position for coffre
        self.x_monnaie = 0 # init x position for monnaie
        self.y_potion = 0 # init y position for potion
        self.y_coffre = 0 # init y position for coffre
        self.y_monnaie = 0 # init y position for monnaie

        # y represents a line on the level structure (array)
        # x represents a column on the level structure (array)

    def display_object(self, SCREEN):
        """ Function to display on screen objects to pick """
        self.potion = pygame.image.load('images/potion.png').convert_alpha() # object to picked
        self.coffre = pygame.image.load('images/coffre.png').convert_alpha() # object to picked
        self.monnaie = pygame.image.load('images/monnaie.png').convert_alpha() # object to picked

        # Reading structure of the Maze Level_structure
        with open(self.level, "r") as level:
            create_structure_level = [] # create a list of the file level.txt
            for line in level: # read each line in level.txt
                line_of_level = [] # create a list for each line
                for sprite in line: # read each sprite in lines of level.txt
                    if sprite != "\n": # ignore "\n"
                        line_of_level.append(sprite) # add each sprite to line
                create_structure_level.append(line_of_level)
                # add each line to create_structure_level
            self.level_structure = create_structure_level

        # Generating random position lines for each items to display
        self.y_potion = random.randint(0, 14) # choice a random position line for potion
        self.y_coffre = random.randint(0, 14) # choice a random position line for coffre
        self.y_monnaie = random.randint(0, 14) # choice a random position line for coffre

        # Loop to define position of POTION
        while self.x_potion == 0: # x position for potion is not defined yet
            test_x_potion = random.randint(0, 14) # testing a random position for x potion
            if self.level_structure[self.y_potion][test_x_potion] == '0':
            # condition, if in the level's structure random test,
            #if the sprite is empty, choose it to display potion
                self.x_potion = test_x_potion

        # Loop to define position of COFFRE
        while self.x_coffre == 0:
            test_x_coffre = random.randint(0, 14)
            if self.level_structure[self.y_coffre][test_x_coffre] == '0':
                self.x_coffre = test_x_coffre

        # Loop to define position of MONNAIE
        while self.x_monnaie == 0:
            test_x_monnaie = random.randint(0, 14)
            if self.level_structure[self.y_monnaie][test_x_monnaie] == '0':
                self.x_monnaie = test_x_monnaie
