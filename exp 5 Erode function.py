import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

# Resize image
img = cv2.resize(img, (800,600))

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Erode image
eroded = cv2.erode(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
