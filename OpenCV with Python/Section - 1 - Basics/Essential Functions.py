import cv2 as cv
import numpy as np


# Load an image
img = cv.imread('image.jpg')
# cv.imshow('Cats', img)

# # Convert to grayscale
# # cv.COLOR_BGR2GRAY converts the image from BGR to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # # Blur image
# # # cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
edge = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', edge)

# # Dilating the image
# # cv.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])
dilate = cv.dilate(edge, (7, 7), iterations=3)
# cv.imshow('Dilated', dilate)

# Eroding the image
# cv.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])
erode = cv.erode(dilate, (7, 7), iterations=3)
# cv.imshow('Eroded', erode)

# Resize the image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Crop the image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)