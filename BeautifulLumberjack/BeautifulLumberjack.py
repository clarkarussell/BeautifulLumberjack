##Beautiful Lumberjack
##Visual User Logger for Raspberry Pi
##Author: Clark Russell
##Date Started: March 13, 2017

import io
import picamera
import cv2
import numpy

#Create a memory stream so the photos don't need to be saved in a file
stream = io.BytesIO()

#Get the picture (low resolutio, so it should be fast)
#Here you can also specify other parameters (like camera rotation)
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

#convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Create an OpenCV image
image = cv2.imdecode(buff, 1)

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/home/pi/github/BeautifulLumberjack/haarcascade_frontalface_default.xml')

#Convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print("Found "+str(len(faces))+" face(s)")

#Draw a rectange around every found face
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

#Save the result image
    cv2.imwrite('result.jpg',image)
