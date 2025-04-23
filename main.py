"""Entry Point into the code"""
from states.state_machine import StateMachine
from util.event_machine import EventMachine
from util.grefs import grefs
from util.time_machine import TimeMachine
import pygame

# Initialize Pygame
pygame.init()

class Game:
    def __init__(self):
        pygame.mouse.set_cursor((0,0),pygame.image.load("assets\images\gui\cursor.png"))

        # Making a screen with pygame
        RESOLUTION_X, RESOLUTION_Y = 640,360
        self.window = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y), pygame.FULLSCREEN | pygame.SCALED)
        grefs["main"] = self

        # Machine Usage
        self.state_machine = StateMachine()
        self.state_machine.change_state("menu")
        self.time_machine = TimeMachine()
        self.event_machine = EventMachine(self.state_machine)

    def start(self):
        self.running = True
        while self.running:
            self.event_machine.check_events()
            self.state_machine.update()
            pygame.display.flip()
            self.time_machine.update()

if __name__ == "__main__":
    g = Game()
    g.start()