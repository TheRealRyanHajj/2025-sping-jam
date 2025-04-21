import pygame, sys
from states.game import GameState
from states.menu import MenuState
from states.credits import CreditsState

class StateMachine:
    def __init__(self):
        self.state_stack = []
        self.state_lookup = {
            "menu": MenuState,
            "game": GameState,
            "credits":CreditsState
        }
        
        self.state = None

    def change_state(self, new_state:str):
        if new_state in self.state_lookup:
            self.state = self.state_lookup[new_state](self)
        self.state_stack.append(self.state)
        self.state.enter()

    def update(self,window):
        if self.state:
            self.state.update(window)
    
    def exit_state(self):
        self.state.exit()
        self.state_stack.pop()
        self.state = self.state_stack[-1] if self.state_stack else None
        if len(self.state_stack) == 0:
            pygame.quit()
            sys.exit()
