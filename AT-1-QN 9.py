import cv2
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,100,200)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("Input Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(edges,cmap="gray")
plt.title("Feature Extraction")
plt.axis("off")

plt.show()
