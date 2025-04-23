import pygame
from states.states import State
from util.grefs import grefs
import classes.soft_body

class GameState(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
        
    def enter(self):
        self.events = grefs["EventMachine"].key_states
        self.window = grefs["main"].window
        self.softbody = classes.soft_body.SoftBody((350,10),20,80)

        self.surface = pygame.Surface((640, 400), pygame.SRCALPHA)
        self.surface.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surface, (255, 255, 255), (-100, 350, 840, 50))
        pygame.draw.rect(self.surface, (255, 255, 255), (400, 200, 100, 100))
        pygame.draw.polygon(self.surface,(255,255,255),((200,350),(400,200),(400,350)))
        self.ground_mask = pygame.mask.from_surface(self.surface)

        self.dt = grefs["TimeMachine"].dt
        self.goBigCooldown = 0


    def update(self):
        self.window.fill((0,0,0))
        if self.events["keySPACEDown"] and self.goBigCooldown <= 0:
            self.goBigCooldown = 0.3
            self.softbody.toggleBig()
        if self.events["keyDDown"] and not self.softbody.isBig:
            self.softbody.apply_velocity(0.3,0)
        elif self.events["keyADown"] and not self.softbody.isBig:
            self.softbody.apply_velocity(-0.3,0)
        
        #Cooldown update
        self.goBigCooldown -= self.dt
        

        self.window.blit(self.surface,(0,0))
        self.softbody.update(self.ground_mask)
        self.softbody.draw(self.window)
        

    def exit(self):
        ...