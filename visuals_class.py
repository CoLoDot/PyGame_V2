import pygame


class Walls(pygame.sprite.Sprite):
    """Class to create Walls' surface"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/walls.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class Floor(pygame.sprite.Sprite):
    """Class to create Floor's surface"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/floor.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class End(pygame.sprite.Sprite):
    """Class to create End's surface"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/murdoc.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class PickPotion(pygame.sprite.Sprite):
    """Class to create PickPotion's surface"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/potion.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class PickCoin(pygame.sprite.Sprite):
    """Class to create PickCoin's surface"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/monnaie.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class PickSafe(pygame.sprite.Sprite):
    """Class to create PickSafe's surface"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/coffre.png')
        self.rect = self.image.get_rect(topleft=(x, y))
