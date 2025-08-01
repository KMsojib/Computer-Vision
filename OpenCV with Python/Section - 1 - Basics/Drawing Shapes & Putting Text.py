import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# Create blank image
blank = np.zeros((500, 500, 3), dtype='uint8') 
cv.imshow('Blank', blank) 

# # 1. making coloring images
blank[:] = 0,0,255
cv.imshow("Yellow", blank)

# # 2. point an image in certain color
blank[200:300, 300:400] = 0, 0, 0
cv.imshow("Green ", blank)

# 3. draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1] //2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

# 4. draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (255, 0, 0), thickness=-1)  # -1 fills the circle
cv.imshow("Circle", blank)


# 5. draw a line
cv.line(blank, (0, 0), (blank.shape[1], blank.shape[0]), (155, 255, 255), thickness=3)
cv.imshow("Line", blank)

# 6. write text
font = cv.FONT_HERSHEY_SIMPLEX
# (img, 'text', org, fontFace, fontScale, color, thickness, lineType)
cv.putText(blank, 'Hello ! my name is Kawsar', (200, 250), font, 1, (255, 255, 255), thickness=2)
cv.imshow("Text", blank)
cv.waitKey(0)