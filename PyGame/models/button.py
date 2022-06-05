import pygame

from constants import *

class Button():
    def __init__(self, text, position):
        font = pygame.font.Font(None, 50)
        self.text = font.render(text, True, WHITE)
        self.text_rect = self.text.get_rect(center = position)
    
    def draw(self, view):
        view.blit(self.text, self.text_rect)
