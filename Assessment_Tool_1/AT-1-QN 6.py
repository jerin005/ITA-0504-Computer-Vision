import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Simulate low light
dark = (img * 0.4).astype(np.uint8)

# Add Gaussian Blur
blur = cv2.GaussianBlur(dark, (9,9), 0)

# Enhance image
enhanced = cv2.convertScaleAbs(blur, alpha=1.8, beta=30)

plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(dark)
plt.title("Low Light")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(blur)
plt.title("Blurred")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(enhanced)
plt.title("Enhanced")
plt.axis("off")

plt.show()
