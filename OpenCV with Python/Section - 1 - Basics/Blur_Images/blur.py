import cv2
import numpy as np

img = cv2.imread('D:\Computer Vision Library Tutorials and Projects Collection\Computer-Vision\OpenCV with Python\Resources\Photos\cats 2.jpg')
cv2.imshow('Original Image', img)


# 1. Average (Mean) Blur
avg_blur = cv2.blur(img, (5, 5))
# Explanation: Replaces each pixel value with the average value of its neighbors in a 5x5 kernel. Good for basic smoothing and noise reduction.

# 2. Gaussian Blur
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
# Explanation: Uses a weighted average (Gaussian kernel). Better at smoothing and denoising without harsh edge loss.

# 3. Median Blur
median_blur = cv2.medianBlur(img, 5)
# Explanation: Each pixel replaced by the median of its neighbors. Excellent for removing salt-and-pepper noise while preserving edges.

# 4. Bilateral Filter
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)
# Explanation: Smooths the image but keeps edges sharp. Useful for crop disease lesions where edge clarity is important.

# 5. Custom Kernel Blur
kernel = np.ones((5,5), np.float32) / 25
custom_blur = cv2.filter2D(img, -1, kernel)
# Explanation: Applies a custom convolution kernel for smoothing. You can define any kernel shape or size.

# Save results
cv2.imshow('avg_blur.jpg', avg_blur)
cv2.imshow('gaussian_blur.jpg', gaussian_blur)
cv2.imshow('median_blur.jpg', median_blur)
cv2.imshow('bilateral_blur.jpg', bilateral_blur)
cv2.imshow('custom_blur.jpg', custom_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()