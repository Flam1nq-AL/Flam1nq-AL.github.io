import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

class Bishop(pygame.sprite.Sprite):
    
    def __init__(self,colour,width,height):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.colour = colour
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, BLACK, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()