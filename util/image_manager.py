import pygame

class ImageManager:
    images = {}

    def load_image(path):
        if path not in ImageManager.images:
            ImageManager.images[path] = pygame.image.load(path)
        return ImageManager.images[path]

    @staticmethod
    def createFrames(spritesheet: pygame.Surface, width: int, height: int, offsetX:int = 0, offsetY:int = 0) -> list:
        """Extracts individual frames from a sprite sheet.

        Args:
            spritesheet (pygame.Surface): The sprite sheet image.
            width (int): The width of each frame.
            height (int): The height of each frame.
            offsetX (int): optional addional X offset.
            offsetY (int): optional addional Y offset.

        Returns:
            list: A list of pygame.Surface objects representing the frames.
        """

        framesInAWidth = spritesheet.get_width() // width  # Number of frames per row
        framesInAHeight = spritesheet.get_height() // height  # Number of frames per column

        frames = []  # List to store extracted frames

        for y in range(framesInAHeight):
            for x in range(framesInAWidth):
                # Extract each frame from the sprite sheet
                frames.append(spritesheet.subsurface((x * width, y * height), (width, height)))

        return frames


    def createFramesWithStates(spritesheet:pygame.Surface, width:int, height:int,stateName:str,frames:dict=None)->dict:
        """Takes a spritesheet and returns a list of frames"""
        framesInAWidth = spritesheet.get_width()/width
        framesInAHeight = spritesheet.get_height()/height
        
        if frames == None:
            frames = {} # Dict of frames
        
        for y in range(framesInAHeight):
            for x in range(framesInAWidth):
                """↑↑ y = direction like the DIRECTIONS LISTED ABOVE ↑↑"""
                frames[(stateName,x,y)] = spritesheet.subsurface((x*width,y*height),(width,height))
        return frames
    
    def createPlayerFrames():
        image = pygame.image.load("assets\images\entites\player\Blue/run.png")
        width = 16
        height = 17

        framesInAWidth = 8
        framesInAHeight = 4
        
        frames = {} # Dict of frames
        
        for y in range(framesInAHeight):
            for x in range(framesInAWidth):
                frames[("Run",x,y)] = image.subsurface((x*width,y*height),(width,height))
        
        image = pygame.image.load("assets\images\entites\player\Blue/idle.png")
        height = 16

        for y in range(framesInAHeight):
            for x in range(framesInAWidth):
                frames[("Idle",x,y)] = image.subsurface((x*width,y*height),(width,height))
        
        return frames