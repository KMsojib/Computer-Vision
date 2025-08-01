import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Function to rescale frames
# This function works only images, videos & live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # image width
    height = int(frame.shape[0] * scale)  # image height

    dimensions = (width, height)  # new dimensions

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Load live video from webcam
def rescaleLiveVideo(weidth,heght):
    cpature.set(3, weidth)  # set width
    cpature.set(4, heght)  # set height

# Load videos
cpature = cv.VideoCapture('D:\Computer Vision\OpenCV Course - Full Tutorial with Python\Resources\Videos\cat.mp4')

while True:
    isTrue, frame = cpature.read()  # read frame by frame

    frame_resized = rescaleFrame(frame, scale=0.1)  # rescale frame

    cv.imshow('Video', frame)  # show original frame
    cv.imshow('Rescaled Video', frame_resized)  # show rescaled frame

    if cv.waitKey(20) & 0xFF == ord('d'):  # wait for 'd' key to exit
        break

# Release the video capture object and close all OpenCV windows
cpature.release()
cv.destroyAllWindows()
plt.close()  # close matplotlib windows if any


# Load Image

img = cv.imread('D:\Computer Vision\OpenCV Course - Full Tutorial with Python\Resources\Photos\cats 2.jpg')
# Rescale the image
image_resized = rescaleFrame(img, scale = 0.2)
# Display the original and resized image
cv.imshow('Original Image', img)
cv.imshow('Rescaled Image', image_resized)

cv.waitKey(0)  # Wait for a key press to close the window
cv.destroyAllWindows()  # Close all OpenCV windows