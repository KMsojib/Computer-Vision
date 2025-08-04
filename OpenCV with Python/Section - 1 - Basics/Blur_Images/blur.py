import cv2 as cv
import numpy as np

# laod image
img = cv.imread('D:\Computer Vision Library Tutorials and Projects Collection\Computer-Vision\OpenCV with Python\Resources\Photos\Bacterial leaf blight\DSC_01.JPG')



# Function to rescale frames
# This function works only images, videos & live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # image width
    height = int(frame.shape[0] * scale)  # image height
    
    dimensions = (width, height)  # new dimensions

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



# Rescale the image
image_resized = rescaleFrame(img, scale = 0.10)


# Display the original and resized image
cv.imshow('Original Image', img)
cv.imshow('Rescaled Image', image_resized)



img = image_resized

# 1. Average (Mean) Blur
avg_blur = cv.blur(img, (5, 5))
# Explanation: Replaces each pixel value with the average value of its neighbors in a 5x5 kernel. Good for basic smoothing and noise reduction.


# 2. Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)
# Explanation: Uses a weighted average (Gaussian kernel). Better at smoothing and denoising without harsh edge loss.


# 3. Median Blur
median_blur = cv.medianBlur(img, 5)
# Explanation: Each pixel replaced by the median of its neighbors. Excellent for removing salt-and-pepper noise while preserving edges.


# 4. Bilateral Filter
bilateral_blur = cv.bilateralFilter(img, 9, 75, 75)
# Explanation: Smooths the image but keeps edges sharp. Useful for crop disease lesions where edge clarity is important.


# 5. Custom Kernel Blur
kernel = np.ones((5,5), np.float32) / 25
custom_blur = cv.filter2D(img, -1, kernel)
# Explanation: Applies a custom convolution kernel for smoothing. You can define any kernel shape or size.

# Save results
cv.imshow('avg_blur.jpg', avg_blur)
cv.imshow('gaussian_blur.jpg', gaussian_blur)
cv.imshow('median_blur.jpg', median_blur)
cv.imshow('bilateral_blur.jpg', bilateral_blur)
cv.imshow('custom_blur.jpg', custom_blur)


cv.waitKey(0)
cv.destroyAllWindows()