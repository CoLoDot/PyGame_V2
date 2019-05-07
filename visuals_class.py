import pygame

class Walls(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.win = pygame.display.get_surface().get_rect()
        self.image = pygame.image.load('images/walls.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class Floor(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.win = pygame.display.get_surface().get_rect()
        self.image = pygame.image.load('images/floor.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class End(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.win = pygame.display.get_surface().get_rect()
        self.image = pygame.image.load('images/murdoc.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class PickPotion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.win = pygame.display.get_surface().get_rect()
        self.image = pygame.image.load('images/potion.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class PickCoin(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.win = pygame.display.get_surface().get_rect()
        self.image = pygame.image.load('images/monnaie.png')
        self.rect = self.image.get_rect(topleft=(x, y))


class PickSafe(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.win = pygame.display.get_surface().get_rect()
        self.image = pygame.image.load('images/coffre.png')
        self.rect = self.image.get_rect(topleft=(x, y))