import pygame
import random
from visuals_class import Floor, PickSafe, PickCoin, PickPotion, End, Walls
from constants import maze_1, maze_2, spriteSize

class MazeCreation(pygame.sprite.Sprite):
    """Class to create a maze and display it on screen"""
    def __init__(self, allSprites, wallsSprites, floorSprites, enemySprites, pickSprites):
        pygame.sprite.Sprite.__init__(self)
        self.mazeList = [maze_1, maze_2]
        self.allSprites = allSprites
        self.wallsSprites = wallsSprites
        self.floorSprites = floorSprites
        self.enemySprites = enemySprites
        self.pickSprites = pickSprites

    def draw(self):
        maze_choice = random.choice(self.mazeList)
        mazing = []
        for line in maze_choice.split('\n'):
            line = list(line)
            mazing.append(line)

        y = 0
        objects_to_display = 0
        counting_sprites = 0
        for line in mazing:
            x = 0
            for sprite in line:
                if sprite == '0':
                    aSprite = Floor(x * spriteSize, y * spriteSize)
                    self.floorSprites.add(aSprite)
                    self.allSprites.add(aSprite)

                    if counting_sprites > 60 and objects_to_display <= 2:
                        x_pick = x * spriteSize
                        y_pick = y * spriteSize
                        list_toBePicked = [PickPotion(x_pick, y_pick),
                                           PickCoin(x_pick, y_pick),
                                           PickSafe(x_pick, y_pick)]
                        choose_toBePicked = random.choice(list_toBePicked)
                        self.pickSprites.add(choose_toBePicked)
                        self.allSprites.add(choose_toBePicked)
                        objects_to_display += 1
                    counting_sprites += 1

                elif sprite == 'm':
                    aSprite = Walls(x * spriteSize, y * spriteSize)
                    self.wallsSprites.add(aSprite)
                    self.allSprites.add(aSprite)
                elif sprite == 'a':
                    aSprite = End(x * spriteSize, y * spriteSize)
                    backgroundSprite = Floor(x * spriteSize, y * spriteSize)
                    self.enemySprites.add(aSprite)
                    self.allSprites.add(backgroundSprite, aSprite)
                x += 1
            y += 1
