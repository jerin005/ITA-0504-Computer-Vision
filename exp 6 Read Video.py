import cv2

video = cv2.VideoCapture(r"C:\Users\jerin\Videos\Live WP\kakashi-hatake-naruto.3840x2160.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Slow Motion", frame)

    if cv2.waitKey(100) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
