from models.button import Button
from constants import *
class MenuController():

    def __init__(self):
        self.buttons = [ Button("Single Player", (SIZE[0]/2, SIZE[1]/4)), 
                         Button("Multiplayer", (SIZE[0]/2, 2 * SIZE[1]/4)),
                         Button("Quit", (SIZE[0]/2, 3 * SIZE[1]/4)) ]
    
    def update(self):
        pass
    
    def draw(self, view):
        for button in self.buttons:
            button.draw(view)