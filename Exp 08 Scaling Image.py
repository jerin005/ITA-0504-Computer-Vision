import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jerin\OneDrive\Pictures\Saved Pictures\tree.jpg")

small = cv2.resize(img, None, fx=0.5, fy=0.5)
large = cv2.resize(img, None, fx=2, fy=2)

def show(img1, text):
    img1 = cv2.resize(img1, (300,300))
    cv2.putText(img1, text, (20,25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (0,255,0), 2)
    return img1

out = np.hstack((
    show(img, "Original"),
    show(small, "50%"),
    show(large, "200%")
))

cv2.imshow("Scaling", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
