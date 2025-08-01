import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Reading Images


img = cv.imread('D:\Computer Vision\OpenCV Course - Full Tutorial with Python\Resources\Photos\wl1.jpg')
# Show the image
cv.imshow('wl1', img)
cv.waitKey(0)  # Wait for a key press to close the window
cv.destroyAllWindows()  # Close all OpenCV windows

# Reading Videos
capture = cv.VideoCapture('D:\Computer Vision\OpenCV Course - Full Tutorial with Python\Resources\Videos\cat.mp4')


# Reading Videos

while True:
    isTrue, frame = capture.read() # This video frame by frame and return a boolean value is it capture or not.
    if not isTrue:
        break
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'): # If 'd' is pressed, it will break the loop
        break

capture.release() # Release the video capture object
cv.destroyAllWindows() # Close all OpenCV windows