import cv2 as cv
import numpy as np

## Read image
img = cv.imread('image.jpg')
cv.imshow('Cat', img)

## Function for Image Translation

""" 
-x --> left
-y --> up
+x --> Right
+y --> Down
"""
def imgTranslation(image, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1],image.shape[0])
    return cv.warpAffine(image, transMat,dimensions)

tranlated = imgTranslation(img, 100,100) # (-100,-100),(-100,100),(100,-100)
cv.imshow("Translated Image : ", tranlated)


## Image Rotation
""" 
    * Image is input & the rotation angel, the point about which to rotate
    if case:
        *If no rotation point is provided, sets it to the center of the image.
    Uses OpenCV’s getRotationMatrix2D to create a 2x3 rotation matrix.
        * rotPoint: center of rotation.
        * angle: rotation in degrees.
        * 1.0: scale factor (no scaling).
    dimension is the height and weight
    
    Return :
        Applies the roation to the iamge using OpenCv's warpAffine function & return
"""
def Rotated(img, angle, rotPoint=None):
    (height, weight) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (weight//2,height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (weight,height)
    
    return cv.warpAffine(img,rotMat,dimensions)


Rotated = Rotated(img, -90)  # Rotate by 45 degrees
cv.imshow("Rotated Image : ", Rotated)


# Image Resizing
def Resized(image, scale=0.5):
    dimensions = (int(image.shape[1] * scale), int(image.shape[0] * scale))
    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

resized = Resized(img, 0.5)  # Resize to 50% of original size
cv.imshow("Resized Image : ", resized)


# flip Image
flip = cv.flip(img, 1)  # 0 for vertical, 1 for horizontal, -1 for both
cv.imshow("Flipped Image : ", flip)

# Crop image
cropped = img[200:300, 100:200]  # Crop a region of interest (ROI)
cv.imshow("Cropped Image : ", cropped)

cv.waitKey(0)
cv.destroyAllWindows()