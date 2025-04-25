import pygame
from util.grefs import grefs

class Camera:
    def __init__(self):
        grefs["Camera"] = self
        self.offsetX = 0
        self.offsetY = 0
        self.margin = 100  # Margin around the screen before the camera moves

        # Defer window size retrieval until display is initialized
        self.update_window_size()

    def update_window_size(self):
        self.screenWidth, self.screenHeight = pygame.display.get_window_size()

    def updatePos(self, target):
        self.update_window_size()  # In case window was resized

        right_edge = self.screenWidth - self.margin
        left_edge = self.margin
        bottom_edge = self.screenHeight - self.margin
        top_edge = self.margin

        # Horizontal camera movement
        if target.x - self.offsetX > right_edge:
            self.offsetX = target.x - right_edge
        elif target.x - self.offsetX < left_edge:
            self.offsetX = target.x - left_edge

        # Vertical camera movement
        if target.y - self.offsetY > bottom_edge:
            self.offsetY = target.y - bottom_edge
        elif target.y - self.offsetY < top_edge:
            self.offsetY = target.y - top_edge
