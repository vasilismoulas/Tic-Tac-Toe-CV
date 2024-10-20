import cv2
import mediapipe as mp
import time
import math as math
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions import drawing_utils
import time
from motion_tracking.hand_tracker import Hand_Tracker
from motion_tracking.gesture_recognizer import Gesture_Recognizer


def main():
        
        ctime = 0
        ptime = 0
        start = True
        cap = cv2.VideoCapture(0)
        gesture_recognizer = Gesture_Recognizer("C:/Users/vasil/OneDrive/Υπολογιστής/tic-tac-toe/models/gesture_recognizer.task").recognizer
        detector = Hand_Tracker()
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()

        while start:
            ret, frame = cap.read()
            # Gesture Recognition
            # Convert the frame received from OpenCV to a MediaPipe’s Image object.
            # (Gesture Recognition OFCOURSE and it must be done before the landmark drawing for lower delay)
            
            #mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            #recognition_result = gesture_recognizer.recognize(mp_image)
            #print(recognition_result) 
           
            # small pause to notice the gesture recognition reliability
            #time.sleep(5.0)
           
            frame = cv2.flip(frame, 1) # flipped frame horizontally
            frame = detector.findFingers(frame)
            lmsList = detector.findPosition(frame)       
            
            if len(lmsList)!=0:
                pass
                #print(lmsList[0])

            ctime = time.time()
            fps =1/(ctime-ptime)
            ptime = ctime

            cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
 
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
            


                
if __name__ == "__main__":
        main()