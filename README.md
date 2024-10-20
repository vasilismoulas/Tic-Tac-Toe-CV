# Upper-Extremity_Mobility_Rehabiliation
 This repository hosts a collection of projects focused on digital hand rehabilitation leveraging the Mediapipe library. Mediapipe provides a versatile framework for real-time multimedia processing, making it ideal for developing interactive applications aimed at improving hand mobility and dexterity.

Table of Contents
---

1. [Abstract](#abstract)

2. [Architecture](#architecture)

3. [File overall operation description](#file-overall-operation-description)
   * [Program.cs](#programcs)
     * [Main function](#Main-funciton)

   * [CodeContainerCompositeConcrete.cs](#codecontainercompositeconcrete.cs)
    
   * [CodeContainerComposite.cs](#codecontainercomposite.cs)
     

   * [C2ASMTranslation.cs]()
     * [C2ASMTranslation class]()

4. Installation instructions 

5.

5. [Glossary]()

5. [Sources](#sources)
<br>

## Abstract
At-Home Rehabilitation and Physical Therapy Scaled Up with Computer Vision Engineering.


#### Game Structure:
##### UI requirements

<ol>
<li>Select gamemode</li>
<ul>
<li>Tic Tac Toe</li>
<li>Choose the shape/Shape-Swarm</li>
<li>Draw The Word</li>
</ul>

<li>Options</li>
<ul> 
<li>Change speed of a game</li>
<li>Volume up/Volume down</li>
<li>Sound up/Sound down</li>
</ul>

<li>Movesets</li>


<li>Exit button</li>
<ul> 
<li>Confirmation</li>
<li>Cancel</li>
</ul>

</ol>

(A sound effect will be triggered when each option is selected)

#### Electron Manual Use:

* Access Developer Tools: 'Ctrl + Shift + I'

## Sources
* (Electron-setup): https://www.electronjs.org/docs/latest/tutorial/quick-start?fbclid=IwAR3d490HZU_U1TkKGVcCv-L0aCZtarqw-CGf9eQk1nvLFlz9GjDzxJcM1Bk

* (Software-Architecture): https://sarrahpitaliya.medium.com/understanding-software-architecture-a-complete-guide-cb8f05900603

* (CSS Transition): https://lukeliutingchun.medium.com/adding-a-transition-effect-for-looping-background-video-with-pure-js-css-354d5961fa08

* (3D game menu): https://web.dev/articles/building/a-3d-game-menu-component

* (Electron— A Complete Guide for building windows executable):
https://blog.canopas.com/electron-a-complete-guide-for-building-windows-executable-a2cca8b52e00

* (Game Architecture): https://www.studytonight.com/3d-game-engineering-with-unity/game-development-architecture

* (XSS attacks preventage): 
1) https://blog.coding.kiwi/electron-csp-local/  
2) https://webpack.js.org/configuration/
3) https://book.hacktricks.xyz/pentesting-web/content-security-policy-csp-bypass

* (Electron App Packaging): 
1) https://www.electronjs.org/docs/latest/tutorial/tutorial-packaging
Errors: 
  * (Squirrel): https://github.com/electron/forge/issues/1818
  * https://github.com/electron/forge/issues/3509

* (How to fix “require is not defined” in JavaScript / Node.js?):
https://codedamn.com/news/javascript/fix-require-is-not-defined

* (Using Preload Scripts): **IMPORTANT(the correct way to import .js files to your electron-app)**
https://www.electronjs.org/docs/latest/tutorial/tutorial-preload

* (How to Access the Webcam in JavaScript):
https://levelup.gitconnected.com/how-to-access-the-webcam-in-javascript-a-beginners-guide-3b5cc4f53b0b

* (How to Get Python and JavaScript to Communicate Using JSON):
https://www.makeuseof.com/tag/python-javascript-communicate-json/

* ():
https://pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/

* (): 
 https://medium.com/red-buffer/integrating-python-flask-backend-with-electron-nodejs-frontend-8ac621d13f72

* (): https://stackoverflow.com/questions/70132291/electron-content-security-policy-error-when-connecting-to-my-api

* (): https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src

* (desktop app icon): https://stackoverflow.com/questions/75941624/how-to-create-a-desktop-shortcut-icon-for-electron-application

* (IPC vs WebSockets): https://www.scriptol.com/javascript/ipc-vs-websocket.php

* (Python Virtual Environment):

* (Flask streaming): https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00

* (Content-Security-Policy(CSP) attributes): https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src

* (Google-Mediapipe for developers): https://github.com/googlesamples/mediapipe/blob/main/examples/gesture_recognizer/python/gesture_recognizer.ipynb

* (MediaPipe GPU Support with CUDA(New programming launguage Python alike: Bend)): https://developers.google.com/mediapipe/framework/getting_started/gpu_support#:~:text=To%20enable%20TensorFlow%20GPU%20inference,software%20on%20your%20Linux%20desktop.&text=Setting%20%24TF_CUDA_PATHS%20is%20the%20way,where%20the%20CUDA%20library%20is. 

* (Image Overlay to VideoCapture(webcam): https://stackoverflow.com/questions/56371365/how-i-can-insert-images-on-captured-video-in-python

* (Gesture Recognition): https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer#models
  Explicit to  that:
  <img src="README media\HandLandmarks.png"></img>

  Gesture classification model bundle
  
  The Gesture classification model bundle can recognize these common hand gestures:
 # Gesture Labels

| ID  | Description          | Label       |
| --- | -------------------- | ----------- |
| 0   | Unrecognized gesture | Unknown     |
| 1   | Closed fist          | Closed_Fist |
| 2   | Open palm            | Open_Palm   |
| 3   | Pointing up          | Pointing_Up |
| 4   | Thumbs down          | Thumb_Down  |
| 5   | Thumbs up            | Thumb_Up    |
| 6   | Victory              | Victory     |
| 7   | Love                 | ILoveYou    |
* (Pre-Build API for Python.MediaPipe initial stage(used in displayV2.py)): https://mediapipe.readthedocs.io/en/latest/solutions/hands.html

* (Bend: a full Python-like language that compiles to CUDA): https://www.reddit.com/r/CUDA/comments/1cu5oce/bend_a_full_pythonlike_language_that_compiles_to/

* (Custom Gesture Recognition): https://www.samproell.io/posts/ai/asl-detector-with-mediapipe-wsl/
  * (MediaPipe Model Maker): https://ai.google.dev/edge/mediapipe/solutions/model_maker

* (Insert png Image): https://stackoverflow.com/questions/75267154/how-do-i-add-an-image-overlay-to-my-live-video-using-cv2

  <img src="README media\Custom Model.png"></img>

* (Electron Linux Instructions): https://www.electronjs.org/docs/latest/development/build-instructions-linux


* (Python Clean Code): https://github.com/zedr/clean-code-python/blob/master/README.md

* (Python code optimization: Cython): https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

<img src="README media\Cython_logo.svg.png"></img>

* (Find if GPU is available): 
 * 1st link: https://hsf-training.github.io/hsf-training-ml-gpu-webpage/02-whichgpu/index.html

 * 2nd link: https://askubuntu.com/questions/633176/how-to-know-if-my-gpu-supports-cuda

 * writing a comprehensive documentation for your software: https://docsfordevelopers.com/table-of-contents/

 * Whats is mediapipe framework ? : https://viso.ai/computer-vision/mediapipe/


## Notes with the things that i want implement:
* (state: ✓) Create a window and fullscreen mode in "OPTIONS" selection.   
* (state: ✓) Create a Transition between the last and first frame of the backround video in main-menu. 
* (state: pending) Pass the modified video by the webcam to frontend by using Flask(.js)
* (state: pending) Modify main-menus UI appearance by resizing and repositioning m.m. buttons.(.js)
* (state: pending) Design each games graphics(Tic-Tac-Toe's board etc...) through Photopea(link: https://www.photopea.com/) so it can match with applications main theme(white-orange. **More details on my phone's notes**.). 

## Smooth Video/Audio Livestreaming from backend to frontend with WebRTC:

* link: https://dev.to/metered-video/webrtc-with-python-and-react-building-a-video-chat-application-mbp


## Problems Occured:
* **preload files**:  
               1) There should be one preload file that exposes APIs to other .js files,by extention,the main world :  
               link 1: https://www.electronjs.org/docs/latest/tutorial/tutorial-preload  
               link 2: https://www.electronjs.org/docs/latest/api/context-bridge

* **CONNECTION-ERROR**: when trying to establish a client-server connection when spawning the python file that hosts the server (Using Flask framework) through **"child_process"** functions **(e.g. : spawn())**.  
Note: Using **"python_shell"** seems that patially manages to solve the problem.Now we have a problem establishing the client-server connection when importing **"mediapipe"** module (sounds weird).The problem may be related tp the fact that i cannot even convert the .py file to an .exe file cause of misconceptions happening in mediapipes paths.

* **Streaming problem using axios module for http requests through Electron**: https://github.com/axios/axios/issues/1474

* **TaskRunner function is false implemented by the developers, as a result causing a non-rational error(display.py gesture_recognition.task)**(fixed): https://stackoverflow.com/questions/75985134/mediapipe-runtime-error-whilst-following-the-hand-landmarker-guide-unable-to-in

* **Rectangle Drawing concurently with the Motion Tracking**(not yet fixed): https://medium.com/@gautamaditee/hand-recognition-using-opencv-a7b109941c88

## Security:
* link: https://www.electronjs.org/docs/latest/tutorial/security#1-only-load-secure-content

## Testing:
* link: https://www.browserstack.com/guide/code-based-testing#:~:text=Developers%20or%20end%20users%20manually,report%20any%20issues%20they%20encounter.

## Update:
* Updating the Application: https://www.electronjs.org/docs/latest/tutorial/updates

## Cross-Platform Techniques:
(First & foremost i'll have to dual boot my Desktop computer in order to check if the app is fully working in Linux Systems as well: https://gcore.com/learning/dual-boot-ubuntu-windows-setup/) 