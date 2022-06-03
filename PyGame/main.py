import pygame
import time

from constants import *
from controllers.menuController import *
from controllers.gameController import *

class Main():

    def __init__(self):
        pygame.init()
        pygame.mouse.set_visibil(False)
        
        self.view = pygame.display.set_mode(SIZE)
        self.state = STATE_MENU
        self.menuController = MenuController()
        self.gameController = GameController()
        self.startTime = 0
        self.currentTime = 0

    def run(self, runTime = 10):
        self.startTime = time.time()

        while (self.currentTime - self.stateTime < runTime):
            time.sleep(1 / FPS)
            self.update()
            self.draw()
    
    def update(self):
        
        if (self.state == STATE_MENU):
            self.updateStateMenu()
        elif (self.state == STATE_PLAY):
            self.updateStatePlay()
        elif (self.state == STATE_DONE):
            self.updateStateDone()

    def updateStateMenu(self):
        pass
    
    def updateStatePlay(self):
        pass
    
    def updateStateDone(self):
        pass