import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

rows, cols = img.shape[:2]

# Translation Matrix (Move Right 100 px and Down 50 px)
M = np.float32([[1, 0, 100],
                [0, 1, 50]])

# Apply Translation
translated = cv2.warpAffine(img, M, (cols, rows))

# Resize for display
img = cv2.resize(img, (300, 300))
translated = cv2.resize(translated, (300, 300))

# Display in one window
output = np.hstack((img, translated))

cv2.imshow("Original | Translated Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
