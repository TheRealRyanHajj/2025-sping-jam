import pygame
pygame.init()
from util.grefs import grefs

class TimeMachine:
    def __init__(self):
        grefs["TimeMachine"] = self
        self.clock = pygame.time.Clock()

    def update(self):
        self.dt = self.clock.tick(60)/1000