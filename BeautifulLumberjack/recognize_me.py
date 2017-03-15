##Face Recognizer using OpenCV3.2.0
##Author: Clark Russell
##Date Started: March 14, 2017 (pi day!)

import cv2
import numpy as np
#import matplotlib.pyplot as plt

#define image and convert to grayscale. Grayscale can also be 'cv2.0'.
img = cv2.imread('liveframe/foo'+str(i)+'.jpg', cv2.IMREAD_GRAYSCALE)

#Use imshow to show image then press any key to exit. Saves the image to liveframe.
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('liveframe/foo'+str(i)+".jpg', img)

#displays the image in matplotlib with coordinates.
#plt.imshow(img, cmap='gray', interpolation='bicubic'
#plt.plot([50,100],[80,100], 'c', linewidth=5)
#plt.show()

