import pygame
from states.states import State
from util.grefs import grefs

class GameState(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
        
    def enter(self):
        self.window = grefs["main"].window

    def update(self):
        events = grefs["EventMachine"].key_states
        self.window.fill((255,255,255))
        if events["keySPACEDown"] == True:
            self.state_machine.exit_state()

    def exit(self):
        print("Exiting Game")