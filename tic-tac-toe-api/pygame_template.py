
# Example file showing a basic pygame "game loop"
import pygame
import cv2
import numpy as np

# pygame setup
pygame.init()

# Create Window/Display
width, height = 640, 480
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Tic-Tac-Toe")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# video capture
cap = cv2.VideoCapture(0)

# Main Loop
start = True

while start:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # video frame
    start, frame = cap.read() # start variable will be modified by cap.read() as well in case any error with the video capturing part happen so we can stop the loop.


    # window.fill([0,0,0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    window.blit(frame, (0,0))
    
    # add text
    font = pygame.font.Font(None, 100)
    text = font.render("Tic-Tac-Toe", True, (50,50,50))
    window.blit(text, (0,0))
    
    # add shapes
     # add shapes
    shape_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.polygon(shape_surface, color=(255, 0, 0), points=[(0, 0), (0, 30), (30, 30)])
    window.blit(shape_surface, (0, 0))
    
    # flip() the display to put your work on window
    pygame.display.flip()
    
    # update display
    pygame.display.update()

    # fps cap/limiter 
    clock.tick(fps)  

pygame.quit()