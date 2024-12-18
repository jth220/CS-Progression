#Code has been generated by ChatGPT for educational purposes

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the image
image = cv2.imread('road_image.jpg')  # Replace with your file path
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

# 2. Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(grayscale, (5, 5), 1.5)  # Smoothing

# 3. Apply Canny Edge Detection
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)  # Detect edges

# 4. Hough Line Transform (on full image)
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50,
                        minLineLength=100, maxLineGap=50)

# 5. Draw Detected Lines on the Original Image
output = image.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]  # Line endpoints
        cv2.line(output, (x1, y1), (x2, y2), (0, 255, 0), 3)  # Draw line in green

# 6. Display Results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1), plt.imshow(edges, cmap='gray'), plt.title('Edge Detection')
plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB)), plt.title('Lane Detection')
plt.show()
