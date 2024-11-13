import cv2
import mediapipe as mp
import time
import math as math
from mediapipe.python.solutions.hands import Hands
from mediapipe.python.solutions import drawing_utils
from cv2.typing import MatLike # different modules use different custom made classes for image encapsulation (Surface for pygame or MatLike for opencv a.k.a cv2)
from typing import Tuple, List, Any

class Hand_Tracker:
    """Hand Tracking object"""
    
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5)-> None:
        self.__mode__   =  mode
        self.__maxHands__   =  maxHands
        self.__detectionCon__   =   detectionCon
        self.__trackCon__   =   trackCon
        self.handsMp = mp.solutions.hands
        self.hands = Hands()
        self.mpDraw= drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findFingers(self, frame : MatLike, draw : bool=True)-> MatLike:
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  
        if self.results.multi_hand_landmarks: 
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms,self.handsMp.HAND_CONNECTIONS)

        return frame

    def findPosition( self, frame: MatLike, handNo: int=0, draw: bool=True)-> Tuple[List[List[int]], List[int]]:
        xList =[]
        yList =[] 
        bbox = [] # contains box's 4 vertexes
        self.lmsList=[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
            
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmsList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame,  (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xmin, xmax = (min(xList), max(xList))
            ymin, ymax = (min(yList), max(yList))
            bbox = (xmin, ymin, xmax, ymax)
            #print("Hands Keypoint")
            #print(bbox)
            if draw:
                cv2.rectangle(frame, (xmin - 20, ymin - 20),(xmax + 20, ymax + 20),
                               (0, 255 , 0) , 2)

        return self.lmsList, bbox
    
    def findFingerUp(self)-> List[int]:
         fingers=[]

         if self.lmsList[self.tipIds[0]][1] > self.lmsList[self.tipIds[0]-1][1]:
              fingers.append(1)
         else:
              fingers.append(0)

         for id in range(1, 5):            
              if self.lmsList[self.tipIds[id]][2] < self.lmsList[self.tipIds[id]-2][2]:
                   fingers.append(1)
              else:
                   fingers.append(0)
        
         return fingers

    def findDistance(self, p1, p2, frame, draw= True, r=15, t=3)-> Tuple[float, Any, List[int]]:
         
        x1 , y1 = self.lmsList[p1][1:]
        x2, y2 = self.lmsList[p2][1:]
        cx , cy = (x1+x2)//2 , (y1 + y2)//2

        if draw:
              cv2.line(frame,(x1, y1),(x2,y2) ,(255,0,255), t)
              cv2.circle(frame,(x1,y1),r,(255,0,255),cv2.FILLED)
              cv2.circle(frame,(x2,y2),r, (255,0,0),cv2.FILLED)
              cv2.circle(frame,(cx,cy), r,(0,0.255),cv2.FILLED)
        len= math.hypot(x2-x1,y2-y1)

        return len, frame , [x1, y1, x2, y2, cx, cy]