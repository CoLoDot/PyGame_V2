import pygame
from pygame.math import Vector2


class Macgyver(pygame.sprite.Sprite):
    def __init__(self, x, y, wallsMaze):
        pygame.sprite.Sprite.__init__(self)
        self.win = pygame.display.get_surface().get_rect()
        self.image = pygame.image.load("images/macgyver.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.macgyverPosition = Vector2(x, y)
        self.macgyverVelocity = Vector2(0, 0)
        self.walls = wallsMaze

    def update(self):
        self.macgyverPosition += self.macgyverVelocity
        self.detectCollisions()

    def detectCollisions(self):
        """Check if Macygyver collided walls"""

        # WALLS
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
