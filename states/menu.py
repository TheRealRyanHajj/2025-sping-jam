import pygame,sys
from states.states import State
from util.grefs import grefs

class MenuState(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def enter(self):
        self.window = grefs["main"].window
        self.bigButtonImage = pygame.image.load("assets/images/gui/buttons.png")
        self.buttonImages = [
            self.bigButtonImage.subsurface((0,0,32,16)),
            self.bigButtonImage.subsurface((0,16,32,16)),
            self.bigButtonImage.subsurface((32,0,32,16)),
            self.bigButtonImage.subsurface((32,16,32,16)),
            self.bigButtonImage.subsurface((64,0,32,16)),
            self.bigButtonImage.subsurface((64,16,32,16))
        ]
        self.logo = pygame.image.load("assets/images/gui/logo.png")
        
        self.playRect = pygame.Rect((272,96),(32,16))
        self.creditsRect = pygame.Rect((272,120),(32,16))
        self.exitRect = pygame.Rect((272,144),(32,16))


    def update(self):
        self.window.fill((191, 191, 191))
        self.window.blit(self.logo,(160-self.logo.get_width()/2,8))
        
        mousePos = pygame.mouse.get_pos()
        
        #Play Button
        if self.playRect.collidepoint(mousePos):
            self.window.blit(self.buttonImages[1],self.playRect)
            if pygame.mouse.get_pressed()[0]:
                self.state_machine.change_state("game")
        else:
            self.window.blit(self.buttonImages[0],self.playRect)
        
        #Credits Button
        if self.creditsRect.collidepoint(mousePos):
            self.window.blit(self.buttonImages[3],self.creditsRect)
            if pygame.mouse.get_pressed()[0]:
                self.state_machine.change_state("credits")
        else:
            self.window.blit(self.buttonImages[2],self.creditsRect)
        
        #Exit Button
        if self.exitRect.collidepoint(mousePos):
            self.window.blit(self.buttonImages[5],self.exitRect)
            if pygame.mouse.get_pressed()[0]:
                self.state_machine.exit_state()
        else:
            self.window.blit(self.buttonImages[4],self.exitRect)

        

        
    def exit(self):
        ...