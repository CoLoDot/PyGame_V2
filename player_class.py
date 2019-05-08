import pygame
from pygame.math import Vector2


class Macgyver(pygame.sprite.Sprite):
    """Macgyver Class"""
    def __init__(self, x, y, wallsMaze):
        """x, y = Player positions
            wallsMaze = group of sprites"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/macgyver.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.macgyverPosition = Vector2(x, y)
        self.macgyverVelocity = Vector2(0, 0)
        self.walls = wallsMaze

    def update(self):
        """Function to update player's position by adding velocity
            and check collisions"""
        self.macgyverPosition += self.macgyverVelocity
        self.playerCollisions()

    def playerCollisions(self):
        """Function to check if player collides walls"""

        self.rect.centerx = self.macgyverPosition.x
        for wall in pygame.sprite.spritecollide(self, self.walls, False):
            if self.macgyverVelocity.x > 0:
                self.rect.right = wall.rect.left
            elif self.macgyverVelocity.x < 0:
                self.rect.left = wall.rect.right
            self.macgyverPosition.x = self.rect.centerx

        self.rect.centery = self.macgyverPosition.y
        for wall in pygame.sprite.spritecollide(self, self.walls, False):
            if self.macgyverVelocity.y > 0:
                self.rect.bottom = wall.rect.top
            elif self.macgyverVelocity.y < 0:
                self.rect.top = wall.rect.bottom
            self.macgyverPosition.y = self.rect.centery
