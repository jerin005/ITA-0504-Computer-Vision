import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

if img is None:
    print("Image not found!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Pixel Resolution
low_res = cv2.resize(img,(150,150))
low_res = cv2.resize(low_res,(img.shape[1],img.shape[0]))

# Intensity Resolution
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

levels = 16

quantized = np.floor(gray/(256/levels))*(256/levels)
quantized = quantized.astype(np.uint8)

plt.figure(figsize=(15,5))

plt.subplot(131)
plt.imshow(img)
plt.title("Original")

plt.subplot(132)
plt.imshow(low_res)
plt.title("Low Pixel Resolution")

plt.subplot(133)
plt.imshow(quantized,cmap='gray')
plt.title("16 Gray Levels")

plt.show()
