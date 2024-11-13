import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

VisionRunningMode = mp.tasks.vision.RunningMode

class Gesture_Recognizer:
     """Gesture Recognition object""" 
        
     def __init__(self, model_file_path: str)-> None:
        self.model_file_path = model_file_path
        self.model_file = open(self.model_file_path, "rb")
        self.model_data = self.model_file.read()
        self.base_options = python.BaseOptions(model_asset_buffer=self.model_data)
        self.options = vision.GestureRecognizerOptions(base_options=self.base_options)
        self.recognizer = vision.GestureRecognizer.create_from_options(self.options)
         
     
         




