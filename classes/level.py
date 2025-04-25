import pygame
from util.grefs import grefs

class Level:
    def __init__(self):
        grefs["Level"] = self

    def createImage(self,level):
        self.collideMask = pygame.mask.from_surface(pygame.image.load(f"assets\images\levels\lev{level}\colide.png"))
        self.hurtMask = pygame.mask.from_surface(pygame.image.load(f"assets\images\levels\lev{level}\hurt.png"))
        self.ontop = pygame.image.load(f"assets\images\levels\lev{level}\ontop.png")

    def draw(self):
        grefs["main"].window.blit(self.ontop,(-grefs["Camera"].offsetX,-grefs["Camera"].offsetY))
    