import cv2
import matplotlib.pyplot as plt

# Load image
img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

if img is None:
    print("Image not found!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Downsample (Improper Sampling)
small = cv2.resize(img, (150, 150))

# Upsample back (Blurred Image)
blurred = cv2.resize(small, (img.shape[1], img.shape[0]))

# Display
titles = ["Original Image", "Blurred Due to Improper Sampling"]

images = [img, blurred]

plt.figure(figsize=(10,5))

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis("off")

plt.show()
