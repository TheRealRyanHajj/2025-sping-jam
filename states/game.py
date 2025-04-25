import pygame
from states.states import State
from util.grefs import grefs
import classes.soft_body
from classes.camera import Camera
from classes.level import Level

class GameState(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
        
    def enter(self):
        self.events = grefs["EventMachine"].key_states
        self.window = grefs["main"].window
        self.softbody = classes.soft_body.SoftBody((350,10),20,80)
        self.Camera = Camera()

        self.Level = Level()
        self.Level.createImage(1)

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
        

        self.Level.draw()
        self.softbody.update()

        self.Camera.updatePos(self.softbody)

        self.softbody.draw(self.window)
        

    def exit(self):
        ...