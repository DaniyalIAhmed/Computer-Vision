# Open CV Cheat Sheet
#### Prepared by Daniyal Ahmed

## **Importing the Package**
```
import cv2 as cv
```
## **1. Reading Images in Open CV**
```
img = cv.imread('path/to/image') #Returns image as a 2D matrix
cv.imshow('name_of_the_window_eg_cat', img)
cv.waitKey(0) #wait for infinite time for a key to be pressed on the keyboard
```
## **2. Reading Videos in Open CV**
```
capture = cv.VideoCapture('path/to/video' || 0) #Returns image as a 2D matrix
while True:
    isTrue, frame = capture.read() #Reads frame but frame and returns if a frame is read successfully along with the frame
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
```

## **3. Resizing Functions in OpenCV**
```
def rescaleFrame(frame, scale=0.75): #Works for images, videos and live videos
    height = int(frame.shape[0] *scale)
    width = int(frame.shape[1] *scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height): #Live videos only
    capture.set(3, height)
    capture.set(4, width)
```
## **4. Drawing on images/videos in OpenCV**
#### 4.1 Creating a rectangle
```
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')# Initialized an array of zeros of (height, width, channels) and dType as image 
# blank[100:200, 300:400]= 126,52,150
cv.rectangle(blank, (0, 0), (250,250), (126,52,150), thickness=2)# draw rectangle
cv.imshow("Blank", blank)
cv.waitKey(0)
```
#### 4.2 Creating a circle
```
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.circle(blank, (250,250), 50, (126,52,150), thickness=4)# draw circle

cv.imshow("Blank", blank)
cv.waitKey(0)
```
#### 4.3 Creating a line
```
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.line(blank, (0, 0), (250,250), (126,52,150), thickness=2, lineType=cv.LINE_AA)

cv.imshow("Blank", blank)
cv.waitKey(0)
```
#### 4.4 Writing Text on an image
```
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.putText(blank, "$601", (0, 250), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 150), 1)

cv.imshow("Blank", blank)
cv.waitKey(0)
```
## **5. Essential functions in OpenCV**
#### 5.1 Changing Color
```
import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')

grayscale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Cat', grayscale_image)
cv.waitKey(0)
```
#### 5.2 Bluring
```
import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')

glur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)

cv.imshow('Cat', glur)
cv.waitKey(0)
```