import pygame

from constants import *

class Bottlecap(pygame.sprite.Sprite):
    def __init__(self, imageFile, size, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(f'assets/{imageFile}'), size)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def draw(self, view):
        view.blit(self.image, self.rect)
    
    def move(self, change):
        self.rect.x += change[0]
        self.rect.y += change[1]
