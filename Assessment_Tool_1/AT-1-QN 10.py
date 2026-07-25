import cv2
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

low=cv2.resize(img,(100,100))

low=cv2.resize(low,(img.shape[1],img.shape[0]))

high=cv2.resize(img,(800,800))

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(low)
plt.title("Low Resolution")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(high)
plt.title("High Resolution")
plt.axis("off")

plt.show()
