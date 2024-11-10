
# Example file showing a basic pygame "game loop"
import pygame
import cv2
import numpy as np
import time

from element.Element import cross_symbol, circle_symbol, IElement
from pygame.surface import Surface
from hand_tracker import Hand_Tracker
from gesture_recognizer import Gesture_Recognizer
from cv2.typing import MatLike


def change_surface_position(rect : Surface) -> None:  
    pass
    

def ui() -> None:
    
 # pygame setup
 pygame.init()
 
 pygame.display.set_caption("Tic-Tac-Toe")
 
 # Initialize Clock for FPS
 fps = 30
 clock = pygame.time.Clock()
 font = pygame.font.Font(None, 30)
 
 # video capture
 cap = cv2.VideoCapture(0)
 
 # Create Window/Display
 prev_width, prev_height = 0, 0
 width, height = 640, 480
 window = pygame.display.set_mode(size=(width, height), flags=pygame.RESIZABLE)
 
 # Initialize Hand Detector
 detector = Hand_Tracker()
 
 # Load images
 # tic-tac-toe table
 table = pygame.image.load("./Tic-Tac-Toe-CV/tic-tac-toe-api/src/frontend/ui/assets/table.png").convert_alpha()
 # change table opacity
 table.set_alpha(180)
 # circle
 circle = pygame.image.load("./Tic-Tac-Toe-CV/tic-tac-toe-api/src/frontend/ui/assets/circle.png").convert_alpha()
 # change circle opacity
 circle.set_alpha(180)
 # circle = pygame.transform.scale(circle, (circle_width/2, circle_height/2))
 # xmark
 xmark = pygame.image.load("./Tic-Tac-Toe-CV/tic-tac-toe-api/src/frontend/ui/assets/xmark.png").convert_alpha()
 # change xmark opacity
 xmark.set_alpha(180)
 
 # Main Loop
 start = True   
    
 while start:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            break 
        elif event.type == pygame.VIDEORESIZE:
            # Update the window size
            prev_width, prev_height = width, height
            width, height = event.size
            window = pygame.display.set_mode(size=(width, height), flags=pygame.RESIZABLE)

    if(not start):
       break 
   
    # video frame
    start, frame = cap.read() 

    # resize to match the updated window dimensions
    frame = cv2.resize(frame, (width, height))
    # window.fill([0,0,0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # rotate by 90 degrees clockwise
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # hand detection
    frame = detector.findFingers(frame)
    lmsList, bbox = detector.findPosition(frame)       
            
    if len(lmsList)!=0:
       lmcoordinates = lmsList[8][1:3] 
       print('landmark 8: ', lmsList[8], 'x, y: ', lmcoordinates)
       
       
       # i need to re-coordinate the xmark's rect cause it's supposedly in the upper left corner of the window (0,0)
       if xmark.get_rect().collidepoint(lmcoordinates):
           print("xmark's rectangle position: ", xmark.get_rect())
           print("8th landmark collided with xmark's rectangle")
       
       #time.sleep(5.0)
    
    # convert frame -> pygame.Surface
    frame = pygame.surfarray.make_surface(frame).convert()
    window.blit(frame, (0,0))
    
    # Resize table image to fit the window
    # table and window size ratio change
    ratio = (prev_width/width, prev_height/height)
    resized_table = pygame.transform.scale(table, (table.get_width() + table.get_width()*ratio[0], table.get_height()+ table.get_height()*ratio[1]))
 
    # Draw Images 
    # table
    window.blit(resized_table, (width/2 - resized_table.get_width()/2, height/2 - resized_table.get_height()/2)) 
    # xmark
    window.blit(xmark, (width/2 - xmark.get_width()/2, height/2 - xmark.get_height()/2))
    # circle
    window.blit(circle, (width/2 - circle.get_width()/2, height/2 - circle.get_height()/2))

    # Calculate and display FPS
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (0, 255, 0))
    window.blit(fps_text, (0, 0))
    
    # flip() the display to put your work on window
    pygame.display.flip()
    
    # update display
    pygame.display.update()

    # fps cap/limiter 
    clock.tick(fps)  

 pygame.quit()   
    

if __name__ == "__main__":  
    
    #inter = IElement()
    #print(type(inter))
    ui()
    