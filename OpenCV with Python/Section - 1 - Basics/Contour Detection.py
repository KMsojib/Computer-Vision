import cv2 as cv
import numpy as np

# Image Resize
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # image width
    height = int(frame.shape[0] * scale)  # image height

    dimensions = (width, height)  # new dimensions

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



# Load the image
img = cv.imread('image.jpg')

resize_image = rescaleFrame(img,scale=0.2)
cv.imshow("Resize",resize_image)
img = resize_image
# cv.imshow("Orginal Image ",img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

canny = cv.Canny(img,125,175)
cv.imshow("Canny ",canny)

cv.waitKey(0)
cv.destroyAllWindows()