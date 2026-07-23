import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

if img is None:
    print("Image not found!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Low-light simulation
low = (img * 0.3).astype("uint8")

# CLAHE Enhancement
lab = cv2.cvtColor(low, cv2.COLOR_RGB2LAB)
l, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=3.0)
l = clahe.apply(l)

enhanced = cv2.merge((l,a,b))
enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2RGB)

plt.figure(figsize=(15,5))

plt.subplot(131)
plt.imshow(img)
plt.title("Original")

plt.subplot(132)
plt.imshow(low)
plt.title("Low Light")

plt.subplot(133)
plt.imshow(enhanced)
plt.title("Enhanced")

plt.show()
