import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')#(height, width, channels)
img = cv.imread('Resources/Photos/cat.jpg')
# blank[100:200, 300:400]= 126,52,150
cv.putText(blank, "$601", (0, 250), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 150), 1)
cv.imshow("Blank", blank)
cv.waitKey(0)