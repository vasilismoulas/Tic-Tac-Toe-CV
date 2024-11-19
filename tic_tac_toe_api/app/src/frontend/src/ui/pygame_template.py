import pygame
import cv2
import numpy as np
import time
#from .tic_tac_toe_api.src. import
from element.Element import Tsymbol, symbolType
from pygame.surface import Surface
from hand_tracker import Hand_Tracker
from gesture_recognizer import Gesture_Recognizer
from tic_tac_toe_api.app.src.frontend.src.ui.SymbolTable.symbol_table import Symbol_Table
from cv2.typing import MatLike
from Helper.surface_editor import SurfaceEditor


def change_surface_position(rect : Surface) -> None:  
    pass

def load_image(image_path: str)-> Surface:
    image = pygame.image.load(image_path).convert_alpha()
    image.set_alpha(180)
    return image 
    
def ui() -> None:
 
 # Initiate pygame 
 pygame.init()
 pygame.display.set_caption("Tic-Tac-Toe")

 # Frame-rate cap
 fps = 30
 clock = pygame.time.Clock()
 font = pygame.font.Font(None, 30)
 
 # Video Capture camera frames
 cap = cv2.VideoCapture(0)
  
 prev_width, prev_height = 0, 0
 width, height = 640, 480
 window = pygame.display.set_mode(size=(width, height), flags=pygame.RESIZABLE)
 
 # Create Hand Tracker
 detector = Hand_Tracker()

 #gesture_recognizer = Gesture_Recognizer('./tic_tac_toe_api/resources/models/gesture_recognizer.task').recognizer

 # Load images
 table = load_image("./tic_tac_toe_api/app/src/frontend/src/ui/assets/table.png")
 
 # Default symbols
 cross_symbol  = Tsymbol(load_image("./tic_tac_toe_api/app/src/frontend/src/ui/assets/cross.png"),
                         symbolType.ST_CROSS_SYMBOL.name)
 circle_symbol = Tsymbol(load_image("./tic_tac_toe_api/app/src/frontend/src/ui/assets/circle.png"), 
                         symbolType.ST_CIRCLE_SYMBOL.name)
 
 # Symbol Table
 symbol_table = Symbol_Table({cross_symbol.symbol_type: cross_symbol, 
                              circle_symbol.symbol_type: circle_symbol}) # Note: initialise the symbol table with the tow default symbols

 # Symbol table look up
 cross  = symbol_table.lookup(f"{symbolType.ST_CROSS_SYMBOL.name}_1")
 circle = symbol_table.lookup(f"{symbolType.ST_CIRCLE_SYMBOL.name}_2")

 print(cross.rect)
 print(circle.rect)
 

 # Game Loop
 start = True       
 while start:
 
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

    # Get next frame
    videocap, frame = cap.read() 

    if(not videocap):
       raise Exception("Error.No videoframe found to capture")
    

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
       print('landmark 8: ', lmsList[8], 'x, y: ', lmcoordinates) # this is going to be replaced by the gesture recognition obj.
       
       
       # i need to re-coordinate the cross's rect cause it's supposedly in the upper left corner of the window (0,0)
       # Check collisions
       cross_collided = cross.surface.get_rect().collidepoint(lmcoordinates)
       circle_collided = circle.surface.get_rect().collidepoint(lmcoordinates)

       if cross_collided or circle_collided:
          print("cross's rectangle position: ", cross.surface.get_rect())
            
          if cross_collided:
             print("8th landmark collided with cross's rectangle")
            
          if circle_collided:
             print("8th landmark collided with circle's rectangle")
       
       #time.sleep(5.0)
    
    # convert frame -> pygame.Surface
    frame = pygame.surfarray.make_surface(frame).convert()
    window.blit(frame, (0, 0))
    
    # Resize table image to fit the window
    # table and window size ratio change
    ratio = (prev_width/width, prev_height/height)
    resized_table = pygame.transform.scale(table, (table.get_width() + table.get_width()*ratio[0], table.get_height()+ table.get_height()*ratio[1]))
 
    # Draw Images 
    # window center coordination = (width/2 - resized_table.get_width()/2, height/2 - resized_table.get_height()/2)
    window.blit(resized_table, (width/2 - resized_table.get_width()/2, height/2 - resized_table.get_height()/2)) 
    
    # Fixed positions
    window.blit(circle.surface, (0, 0))
    window.blit(cross.surface,  (0, circle.rect.height))

    # Calculate and display FPS
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (0, 255, 0))
    window.blit(fps_text, (0, 0))
    
    # flip() the display to put work on window
    pygame.display.flip()
    
    # update display
    pygame.display.update()

    # fps cap/limiter 
    clock.tick(fps)  

 pygame.quit()   
    

if __name__ == "__main__":  
    ui()
    