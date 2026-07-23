import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

noise=np.random.normal(0,25,img.shape).astype(np.uint8)

noisy=cv2.add(img,noise)

median=cv2.medianBlur(noisy,5)

gaussian=cv2.GaussianBlur(noisy,(5,5),0)

plt.figure(figsize=(12,4))

titles=["Original","Noisy","Median Filter","Gaussian Filter"]

images=[img,noisy,median,gaussian]

for i in range(4):

    plt.subplot(1,4,i+1)

    plt.imshow(images[i])

    plt.title(titles[i])

    plt.axis("off")

plt.show()
