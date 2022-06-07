import pygame

from constants import *
from models.bottlecap import Bottlecap
class GameController():
    """
    Another FSM for the game states.
        0: INIT,
        1: TURN_1,
        2: TURN_2 (maybe go to 1),
        3: DONE
    """

    def __init__(self):
        self.scores = [0, 0]
        self.state = STATE_GAME_INIT
        self.bottlecaps = [ Bottlecap('Bottlecap1.png', (50, 50), (100, 100)),
                            Bottlecap('Bottlecap1.png', (75, 75), (500, 500)) ]
        self.nPressed = False

    def update(self):
        
        if (self.state == STATE_GAME_INIT):
        
            self.updateKeysPressed()
            if (self.nPressed):
                self.nPressed = False
                self.state = STATE_GAME_TURN_1
        
        elif (self.state == STATE_GAME_TURN_1):

            self.updateMovements(1)
            if (self.nPressed):
                self.nPressed = False
                self.state = STATE_GAME_TURN_2
        
        elif (self.state == STATE_GAME_TURN_2):
            self.updateMovements(2)
    
    def draw(self, view):
        for bottlecap in self.bottlecaps:
            bottlecap.draw(view)
    
    def executeOneTurn(self):
        pass

    def updateKeysPressed(self):
        for event in pygame.event.get():
            # Determine if N is pressed
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                self.nPressed = True
    
    # turn specifies the bottlecap
    def updateMovements(self, turn):
        deltaX = 0
        deltaY = 0
        for event in pygame.event.get():
            # Also check whether to switch players
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
                self.nPressed = True
            elif (event.type == pygame.KEYDOWN):
                print('EVENT')
                if (event.key == pygame.K_LEFT):
                    deltaX -= DELTA_X
                elif (event.key == pygame.K_RIGHT):
                    deltaX += DELTA_X
                elif (event.key == pygame.K_UP):
                    deltaY -= DELTA_Y
                elif (event.key == pygame.K_DOWN):
                    deltaY += DELTA_Y
        
        self.bottlecaps[turn - 1].move([deltaX, deltaY])


