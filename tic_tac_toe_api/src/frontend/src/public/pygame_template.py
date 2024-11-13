
# Example file showing a basic pygame "game loop"
import pygame
import cv2
import numpy as np
import memory_profiler
from hand_tracker import Hand_Tracker
from gesture_recognizer import Gesture_Recognizer
from cv2.typing import MatLike




def main() -> None:
    
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
 
 # center
 #center = 
 
 # Load images
 # tic-tac-toe table
 table = pygame.image.load("./Tic-Tac-Toe-CV/tic-tac-toe-api/src/frontend/ui/assets/table.png").convert_alpha()
 table.set_alpha(235)
 table_width = table.get_width()
 table_height = table.get_height()
 # circle
 circle = pygame.image.load("./Tic-Tac-Toe-CV/tic-tac-toe-api/frontend/ui/assets/circle.png").convert_alpha()
 circle.set_alpha(235)
 circle_width = circle.get_width()
 circle_height = circle.get_height()
 # circle = pygame.transform.scale(circle, (circle_width/2, circle_height/2))
 # xmark
 xmark = pygame.image.load("./Tic-Tac-Toe-CV/tic-tac-toe-api/frontend/ui/assets/xmark.png").convert_alpha()
 xmark.set_alpha(168)
 xmark_width = xmark.get_width()
 xmark_height = xmark.get_height()
 # xmark = pygame.transform.scale(xmark, (xmark_width/2, xmark_height/2))
 
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
    # Note: need to apply LUT to videocapture
    start, frame = cap.read() # start variable will be modified by cap.read() as well in case any error with the video capturing part happen so we can stop the loop.

    # resize to match the updated window dimensions
    frame = cv2.resize(frame, (width, height))

    # window.fill([0,0,0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # frame = np.rot90(frame)
    # Using cv2.rotate() method
    # Using cv2.ROTATE_90_CLOCKWISE rotate
    # by 90 degrees clockwise
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # hand detection
    frame = detector.findFingers(frame)
    lmsList = detector.findPosition(frame)       
            
    if len(lmsList)!=0:
        pass
        #print(lmsList[0])
    
    # convert frame -> pygame.Surface
    frame = pygame.surfarray.make_surface(frame)
    window.blit(frame, (0,0))
    
    # add text
    # font = pygame.font.Font(None, 100)
    # text = font.render("Tic-Tac-Toe", True, (50,50,50))
    # window.blit(text, (0,0))
    
    # add shapes
    # add shapes
    # shape_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    # pygame.draw.circle(surface=shape_surface, color=(255, 0, 0), center=(30,30), radius=15.0)
    # window.blit(shape_surface, (0, 0))
    
    # Resize table image to fit the window
    # table and window size ratio change
    ratio = (prev_width/width, prev_height/height)
    resized_table = pygame.transform.scale(table, (table_width + table_width*ratio[0], table_height+ table_height*ratio[1]))
    
    # ** Needs to be fixed **
    # if(prev_width < width and prev_height < height):
    #   ratio = (prev_width/width, prev_height/height)
    #   resized_table = pygame.transform.scale(table, (table_width + table_width*ratio[0], table_height+ table_height*ratio[1]))
    #   table_width, table_height = table_width + table_width*ratio[0], table_height+ table_height*ratio[1]
    
    # elif(prev_width > width and prev_height > height):
    #   ratio = (width/prev_width, height/prev_height)
    #   resized_table = pygame.transform.scale(table, (table_width - table_width*ratio[0], table_height - table_height*ratio[1]))
    #   table_width, table_height = table_width - table_width*ratio[0], table_height - table_height*ratio[1]
    
    # add images 
    # table
    window.blit(resized_table, (width/2 - resized_table.get_width()/2, height/2 - resized_table.get_height()/2))
    
    # Shapes
    
    
    # xmark
    window.blit(xmark, (width/2 - xmark.get_width()/2, height/2 - xmark.get_height()/2))
    # circle
    window.blit(circle, (width/2 - circle.get_width()/2, height/2 - circle.get_height()/2))
    # circle's rectangle
    pygame.draw.rect(window, (255,0,0), circle.get_rect())
    
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
    main()