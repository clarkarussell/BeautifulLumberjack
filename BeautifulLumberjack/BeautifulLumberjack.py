##Beautiful Lumberjack
##Visual User Logger for Raspberry Pi
##Author: Clark Russell
##Date Started: March 13, 2017

from os import remove
from time import sleep
from picamera import PiCamera

#Set camera options
camera = PiCamera()
camera.resolution = (1024, 768)

#Take a series of pictures every half second, convert each to grayscale
#and save for processing.

camera.start_preview()
sleep (2) #gives the camera time to adjust to lighting conditions.

#Take a picture every half second, process it, identify the face
#log the result, and delete the picture.

for i in range (5): #1209600 is the humber of half seconds in a week.
    sleep(0.5)
    #camera.capture('liveframe/foo.jpg')
    camera.capture('liveframe/foo'+str(i)+'.jpg')
    #insert face recognition code here
    #insert logger code here
    remove('liveframe/foo'+str(i)+'.jpg')
camera.stop_preview()    
    
