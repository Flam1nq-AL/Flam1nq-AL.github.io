import pygame
from pawn import Pawn
from rook import Rook
from bishop import Bishop
from king import King
from queen import Queen
from knight import Knight


pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (220,220,220)



size = (800, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chess")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

black_pawn = pygame.image.load('Chess/Images/B_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (100, 100))
        
        

def draw_tile(x,y,colour):
    pygame.draw.rect(screen,colour,(x,y,100,100))

board = [
         ['r','kn','b','ki','q','b','kn','r'],
         ['p','p','p','p','p','p','p','p'],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         ['p','p','p','p','p','p','p','p'],
         ['r','kn','b','q','ki','b','kn','r']
         ]
print(board[0][1])

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

# pawn = Pawn(BLACK,50,50)
# pawn.rect.x = 200
# pawn.rect.y = 200

all_sprites_list = pygame.sprite.Group()

white = False
for i in range(8):
    for j in range(8):
        if board[i][j] != ' ':
            if white == False:
                if board[i][j] == 'p':
                    piece = Pawn(BLACK,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'r':
                    piece = Rook(BLACK,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'b':
                    piece = Bishop(BLACK,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'kn':
                    piece = Knight(BLACK,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'ki':
                    piece = King(BLACK,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'q':
                    piece = Queen(BLACK,50,50)
                    board[i][j] = piece
                piece.rect.x = j*100
                piece.rect.y = i*100
                all_sprites_list.add(piece)
            else:
                if board[i][j] == 'p':
                    piece = Pawn(WHITE,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'r':
                    piece = Rook(WHITE,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'b':
                    piece = Bishop(WHITE,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'kn':
                    piece = Knight(WHITE,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'ki':
                    piece = King(WHITE,50,50)
                    board[i][j] = piece
                elif board[i][j] == 'q':
                    piece = Queen(WHITE,50,50)
                    board[i][j] = piece
                piece.rect.x = j*100
                piece.rect.y = i*100
                all_sprites_list.add(piece)
                
        else:
            white = True   
print(board)
# all_sprites_list.add(pawn)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    all_sprites_list.update()
    screen.fill(WHITE)
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here
    for i in range(8):
        for j in range(8):
            if tiles[i][j] == 'w':
                draw_tile(i*100,j*100,WHITE)
            else:
                draw_tile(i*100,j*100,GREY)
    
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ' and board[i][j].colour == BLACK:
                screen.blit(black_pawn,(board[i][j].rect.x,board[i][j].rect.y))
                
    
                
    
    
         
    all_sprites_list.draw(screen)      
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()