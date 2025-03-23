import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
# grayscale_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

glur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Cat', glur)
cv.waitKey(0)