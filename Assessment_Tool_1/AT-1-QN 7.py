import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg",0)

levels=[256,128,64,32,16]

plt.figure(figsize=(15,4))

plt.subplot(1,6,1)
plt.imshow(img,cmap='gray')
plt.title("Original")
plt.axis("off")

for i,level in enumerate(levels):

    factor=256//level

    quant=(img//factor)*factor

    plt.subplot(1,6,i+2)

    plt.imshow(quant,cmap='gray')

    plt.title(str(level)+" Levels")

    plt.axis("off")

plt.show()
