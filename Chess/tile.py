import pygame
from random import randint

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (220,220,220)


# Open a new window
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")


class Pawn(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

def draw_tile(x,y,colour):
    pygame.draw.rect(screen,colour,(x,y,100,100))

board = [
         ['r','k','b','k','q','b','r','k'],
         ['p','p','p','p','p','p','p','p'],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         ['p','p','p','p','p','p','p','p'],
         ['r','k','b','q','k','b','r','k'],
         ]


tiles = [
         ['w','b','w','b','w','b','w','b'],
         ['b','w','b','w','b','w','b','w'],
         ['w','b','w','b','w','b','w','b'],
         ['b','w','b','w','b','w','b','w'],
         ['w','b','w','b','w','b','w','b'],
         ['b','w','b','w','b','w','b','w'],
         ['w','b','w','b','w','b','w','b'],
         ['b','w','b','w','b','w','b','w']
        ]

piece = Pawn(BLACK,100,100)
piece.rect.x = 100
piece.rect.y = 100





# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add thepaddles to the list of sprites
all_sprites_list.add(piece)
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False


    # --- Game logic should go here
    all_sprites_list.update()


    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(WHITE)
    # Draw the net

    # for i in range(8):
    #     for j in range(8):
    #         if tiles[i][j] == 'w':
    #             draw_tile(i*100,j*100,WHITE)
    #         else:
    #             draw_tile(i*100,j*100,GREY)
    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()