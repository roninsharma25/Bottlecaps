import pygame
import time
import os

from constants import *
from controllers.menuController import *
from controllers.gameController import *

class Main():

    def __init__(self):
        os.putenv("SDL_MOUSEDEV", "/dev/input/touchscreen")
        pygame.init()
        pygame.mouse.set_visible(False)
        
        self.view = pygame.display.set_mode(SIZE)
        self.state = STATE_MENU
        self.menuController = MenuController()
        self.gameController = GameController()
        self.startTime = 0
        self.currentTime = 0

    def run(self, runTime = 3):
        self.startTime = time.time()

        while (self.currentTime - self.startTime < runTime):
            time.sleep(1 / FPS)
            #self.update()
            self.draw()
            self.currentTime = time.time()
        
        pygame.quit()
    
    def update(self):
        
        if (self.state == STATE_MENU):
            self.updateStateMenu()
        elif (self.state == STATE_PLAY):
            self.updateStatePlay()
        elif (self.state == STATE_DONE):
            self.updateStateDone()

    def updateStateMenu(self):
        self.menuController.update()
    
    def updateStatePlay(self):
        pass
    
    def updateStateDone(self):
        pass
    
    def draw(self):
        self.view.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit')
        
        if (self.state == STATE_MENU):
            self.menuController.draw(self.view)
        elif (self.state == STATE_PLAY):
            self.gameController.draw(self.view)

        pygame.display.flip()

if __name__ == "__main__":
    game = Main()
    game.run()