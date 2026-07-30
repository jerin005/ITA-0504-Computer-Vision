import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

# Rotate image
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
anticlockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Resize for display
img = cv2.resize(img, (300, 300))
clockwise = cv2.resize(clockwise, (300, 300))
anticlockwise = cv2.resize(anticlockwise, (300, 300))

# Combine images
output = np.hstack((img, clockwise, anticlockwise))

# Display
cv2.imshow("Original | Clockwise | Counter Clockwise", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
