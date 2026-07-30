import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\Awaken gojo satoru .png")

# Resize the image
img = cv2.resize(img, (800, 600))

# Create a 5x5 kernel
kernel = np.ones((5,5), np.uint8)

# Dilate the image
dilated = cv2.dilate(img, kernel, iterations=1)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
