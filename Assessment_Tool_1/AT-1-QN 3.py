import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

if img is None:
    print("Image not found!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Low sampling
small = cv2.resize(img, (100,100), interpolation=cv2.INTER_NEAREST)

# Enlarged (Aliasing)
alias = cv2.resize(small,
                   (img.shape[1], img.shape[0]),
                   interpolation=cv2.INTER_NEAREST)

# Anti-aliasing
smooth = cv2.resize(img,
                    (img.shape[1]//2, img.shape[0]//2),
                    interpolation=cv2.INTER_AREA)

plt.figure(figsize=(15,5))

plt.subplot(131)
plt.imshow(img)
plt.title("Original")

plt.subplot(132)
plt.imshow(alias)
plt.title("Aliasing")

plt.subplot(133)
plt.imshow(smooth)
plt.title("Anti-Aliasing")

plt.show()
