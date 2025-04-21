import pygame
from util.grefs import grefs

class Entity:
    def __init__(self,cords:tuple,size:tuple,image:pygame.Surface):
        """Spawns an entity that has basic varibles:"""
        self.x = cords[0]
        self.y = cords[1]
        self.width = size[0]
        self.height = size[1]
        self.image = image
    
    def draw(self,offsetX:int,offsetY:int):
        """Draws the self.image to the window"""
        grefs["window"].blit(self.image,(self.x+offsetX,self.y+offsetY))
        