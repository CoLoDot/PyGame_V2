"""Docstring"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*
#pylint: disable=no-member

import logging as lg # logging's library
import pygame # import pygame's library

from mgclasses import *


lg.basicConfig(level=lg.DEBUG)

pygame.init() # initialize pygame

#####################
####### ABOUT #######
#####################


#Developer : CoLoDot // https://github.com/CoLoDot

#Music : Soundbay - Epic Movie from https://www.jamendo.com
#Images : Jesse Freeman https://www.jessefreeman.com/


#PROJECT : Help Macgyver to get out of the maze !
#		  Developed with Python3
#          Player : Macgyver
#          Ennemy : Murdoc
#          Macgyver has to pick every items and
#          presents himself to Murdoc in order to win.

#####################
#### CONSTANTES #####
#####################

SIZE_OF_SPRITE = 30 # variable size of sprites in pixels
NUMBER_OF_SPRITE = 15 # variable number of sprites in a side of the window
WINDOW_SIZE = NUMBER_OF_SPRITE * SIZE_OF_SPRITE # variable size of window's game
SCREEN = pygame.display.set_mode((WINDOW_SIZE, 480)) # pygame function to display the screen
BACKGROUND = pygame.image.load('images/background.png').convert_alpha()
#pygame.mixer.music.load("music/soundbay_Epic_Movie.wav") # background music


#####################
######## MAIN #######
#####################

def main():
    """ Main Loop of the Game """

    gameplay_on = True

    #pygame.mixer.music.play()
    # music player during gameplay
    pygame.display.set_caption("Help Macgyver getting out of the Maze !")
    # window's title

    labyrinthe = Maze()
    labyrinthe.creating_level()
    # method generating the structure of the level
    labyrinthe.displaying_level(SCREEN)
    # methode displaying level on screen

    player = Macgyver(labyrinthe)
    # class Macgyver with Maze as an argurment

    objects = Pickittowin()
    objects.display_object(SCREEN)
    # method to display objects randomly on the Maze

    potion_unpicked = True
    coffre_unpicked = True
    monnaie_unpicked = True

    while gameplay_on:
    # main loop of the game

        for event in pygame.event.get():
        # loop to control each event

            if event.type == pygame.QUIT:
                gameplay_on = False
                # game stop
            elif event.type == KEYDOWN:
                # arrows' events
                if event.key == K_RIGHT:
                    # right arrow
                    player.make_move_macgyver('right')
                elif event.key == K_LEFT:
                    # left arrow
                    player.make_move_macgyver('left')
                elif event.key == K_UP:
                    # up arrow
                    player.make_move_macgyver('up')
                elif event.key == K_DOWN:
                    # down arrow
                    player.make_move_macgyver('down')


        SCREEN.blit(BACKGROUND, (0, 0))
        # display background on screen
        labyrinthe.displaying_level(SCREEN)
        # display the maze on screen
        player.make_move_macgyver(SCREEN)
        # display movements of Macgyver
        SCREEN.blit(player.character_direction,
                    (player.position_character_in_pixel_y,
                     player.position_character_in_pixel_x))
                     # display position of Macgyver

        if potion_unpicked:
        # Loop to pick the Potion
            SCREEN.blit(objects.potion, (objects.x_potion * SIZE_OF_SPRITE,
                                         objects.y_potion * SIZE_OF_SPRITE))
                                         # display POTION and converts it into sprite
        if (player.position_character_in_pixel_y,
                player.position_character_in_pixel_x) == (objects.x_potion * SIZE_OF_SPRITE,
                                                          objects.y_potion * SIZE_OF_SPRITE):
            potion_unpicked = False
            # remove POTION image
            SCREEN.blit(objects.potion, (180, 450))
            # on the bottombar of the window's game
            lg.debug('potion picked')

        if coffre_unpicked:
        # Loop to pick the Coffre
            SCREEN.blit(objects.coffre, (objects.x_coffre * SIZE_OF_SPRITE,
                                         objects.y_coffre * SIZE_OF_SPRITE))
                                         # display COFFRE and converts it into sprite
        if (player.position_character_in_pixel_y,
                player.position_character_in_pixel_x) == (objects.x_coffre * SIZE_OF_SPRITE,
                                                          objects.y_coffre * SIZE_OF_SPRITE):
            coffre_unpicked = False
            SCREEN.blit(objects.coffre, (210, 451))
            lg.debug('coffre picked')

        if monnaie_unpicked:
        # Loop to pick the monnaie
            SCREEN.blit(objects.monnaie, (objects.x_monnaie * SIZE_OF_SPRITE,
                                          objects.y_monnaie * SIZE_OF_SPRITE))
                                          # display MONNAIE and converts it into sprite
        if (player.position_character_in_pixel_y,
                player.position_character_in_pixel_x) == (objects.x_monnaie * SIZE_OF_SPRITE,
                                                          objects.y_monnaie * SIZE_OF_SPRITE):
            monnaie_unpicked = False
            SCREEN.blit(objects.monnaie, (240, 450))
            lg.debug('monnaie picked')

        # Loop to win or loose the game
        if labyrinthe.level_structure[
                player.position_character_in_sprite_x][
                    player.position_character_in_sprite_y] == 'a':
            # if PLAYER on sprite 'a'/Murdoc
            if monnaie_unpicked is False and coffre_unpicked is False and potion_unpicked is False:
                gameplay_on = False # game stops
                lg.debug('WINNER !!! You picked all items')
            if monnaie_unpicked is True or coffre_unpicked is True or potion_unpicked is True:
                gameplay_on = False 
                lg.debug('LOSER ! Try again ! You have to picked all items')


        pygame.display.flip()
        # refresh screen

if __name__ == '__main__':# Encapsulation of main function
    main()

pygame.quit()
# Pygame stops
